import preprocessing as pre
import intensifiers as ints
import lexicon
from pattern.en import wordnet
from pattern.en import NOUN, VERB, ADJECTIVE, ADVERB

SWN_PRIOR_POLARITY = 0
SWN = 1
SUBJECTIVITY_CLUES = 2

swn_prior_polarity = lexicon.SentiWords()


def start(bow_sentences):
    pass


def is_negation():
    """Detects when a bigram (e.g. not good) or trigam (e.g. not very good) is negated"""
    pass


def negation_polarity():
    pass


def word_prior_polarity(word, pos_tag=None):

    pos_tag = "n" if pos_tag in pre.POS_TAGS.NOUNS else pos_tag
    pos_tag = "v" if pos_tag in pre.POS_TAGS.VERBS else pos_tag
    pos_tag = "r" if pos_tag in pre.POS_TAGS.ADVS else pos_tag
    pos_tag = "a" if pos_tag in pre.POS_TAGS.ADJS else None

    if pos_tag is None:
        pos_tag = 'a'

    prior_polarity_score = swn_prior_polarity.get_entry_by_name_and_pos(
        word, pos_tag)
    if prior_polarity_score is None:
        return None

    return (prior_polarity_score['prior_polarity_score'], 0)


def word_swn_polarity(word, pos_tag=None):
    """returns a (polarity, subjectivity)-tuple for the given word from SENTIWORDNET.
    If there is no synsets for the given word, None will be returned
    The word can be NOUN, VERB, ADJECTIVE, ADVERB"""

    pos_tag = "NOUN" if pos_tag in pre.POS_TAGS.NOUNS else pos_tag
    pos_tag = "VERB" if pos_tag in pre.POS_TAGS.VERBS else pos_tag
    pos_tag = "ADVERB" if pos_tag in pre.POS_TAGS.ADVS else pos_tag
    pos_tag = "ADJECTIVE" if pos_tag in pre.POS_TAGS.ADJS else None

    TAGS = {"NOUN": NOUN, "VERB": VERB,
            "ADJECTIVE": ADJECTIVE, "ADVERB": ADVERB}
    TAG = TAGS[pos_tag] if pos_tag else ADJECTIVE

    synsets = wordnet.synsets(word, TAG)
    if len(synsets) > 0:
        polarity = synsets[0].weight
        return polarity
    else:
        return None


def get_unigram_polarity(unigram, lexicon=SWN_PRIOR_POLARITY,
                         use_position=True,
                         use_frequency=True,
                         compensate_bias=True,
                         bias_compensation=0.5):
    """Return unigram polarity based on some arguments.
        Frequency is used only IF position is FALSE
    """

    polarity = None
    if lexicon == SWN_PRIOR_POLARITY:
        polarity = word_prior_polarity(
            unigram.word, pos_tag=unigram.pos_tag)[0]
    else:
        polarity = word_swn_polarity(unigram.word, pos_tag=unigram.pos_tag)[0]

    if use_position:
        polarity = (polarity * unigram.position) / \
            float(unigram.doc_word_count)

    if use_frequency and not use_position:
        polarity = polarity / float(unigram.frequency)

    if polarity < 0 and compensate_bias:
        polarity = polarity / bias_compensation

    return polarity


def get_bigram_polarity(bigram, lexicon=SWN_PRIOR_POLARITY,
                        use_position=True,
                        use_frequency=True,
                        compensate_bias=True,
                        bias_compensation=0.5):

    unigram_polarity = get_unigram_polarity(bigram.word_2, lexicon=lexicon,
                                            use_position=use_position,
                                            use_frequency=use_frequency,
                                            compensate_bias=compensate_bias,
                                            bias_compensation=bias_compensation)

    # print '\nbefore - unigram_polarity:', unigram_polarity
    if bigram.word_1.word in [ints.intensifiers.low.seed] + ints.intensifiers.low.words:
        unigram_polarity = unigram_polarity + \
            (unigram_polarity * ints.intensifiers.low.modifier)
    elif bigram.word_1.word in [ints.intensifiers.very_low.seed] + ints.intensifiers.very_low.words:
        unigram_polarity = unigram_polarity + \
            (unigram_polarity * ints.intensifiers.very_low.modifier)
    elif bigram.word_1.word in [ints.intensifiers.lowest.seed] + ints.intensifiers.lowest.words:
        unigram_polarity = unigram_polarity + \
            (unigram_polarity * ints.intensifiers.lowest.modifier)
    elif bigram.word_1.word in [ints.intensifiers.high.seed] + ints.intensifiers.high.words:
        unigram_polarity = unigram_polarity + \
            (unigram_polarity * ints.intensifiers.high.modifier)
    elif bigram.word_1.word in [ints.intensifiers.very_high.seed] + ints.intensifiers.very_high.words:
        unigram_polarity = unigram_polarity + \
            (unigram_polarity * ints.intensifiers.very_high.modifier)
    elif bigram.word_1.word in [ints.intensifiers.highest.seed] + ints.intensifiers.highest.words:
        # print 'highest', bigram.word_1.word
        unigram_polarity = unigram_polarity + \
            (unigram_polarity * ints.intensifiers.highest.modifier)
    elif bigram.word_1.word in [ints.intensifiers.most_highest.seed] + ints.intensifiers.most_highest.words:
        unigram_polarity = unigram_polarity + \
            (unigram_polarity * ints.intensifiers.most_highest.modifier)

    # print 'after - unigram_polarity:', unigram_polarity
    return unigram_polarity


def get_trigram_polarity(trigram, lexicon=SWN_PRIOR_POLARITY,
                         use_position=True,
                         use_frequency=True,
                         compensate_bias=True,
                         bias_compensation=0.5):

    bigram = pre.Bigram()
    bigram.word_1 = trigram.word_2
    bigram.word_2 = trigram.word_3
    bigram_polarity = get_bigram_polarity(bigram, lexicon=lexicon,
                                          use_position=use_position,
                                          use_frequency=use_frequency,
                                          compensate_bias=compensate_bias,
                                          bias_compensation=bias_compensation)

    if trigram.word_1.word in [ints.intensifiers.low.seed] + ints.intensifiers.low.words:
        bigram_polarity = bigram_polarity + \
            (bigram_polarity * ints.intensifiers.low.modifier)
    elif trigram.word_1.word in [ints.intensifiers.very_low.seed] + ints.intensifiers.very_low.words:
        bigram_polarity = bigram_polarity + \
            (bigram_polarity * ints.intensifiers.very_low.modifier)
    elif trigram.word_1.word in [ints.intensifiers.lowest.seed] + ints.intensifiers.lowest.words:
        bigram_polarity = bigram_polarity + \
            (bigram_polarity * ints.intensifiers.lowest.modifier)
    elif trigram.word_1.word in [ints.intensifiers.high.seed] + ints.intensifiers.high.words:
        bigram_polarity = bigram_polarity + \
            (bigram_polarity * ints.intensifiers.high.modifier)
    elif trigram.word_1.word in [ints.intensifiers.very_high.seed] + ints.intensifiers.very_high.words:
        bigram_polarity = bigram_polarity + \
            (bigram_polarity * ints.intensifiers.very_high.modifier)
    elif trigram.word_1.word in [ints.intensifiers.highest.seed] + ints.intensifiers.highest.words:
        bigram_polarity = bigram_polarity + \
            (bigram_polarity * ints.intensifiers.highest.modifier)
    elif trigram.word_1.word in [ints.intensifiers.most_highest.seed] + ints.intensifiers.most_highest.words:
        bigram_polarity = bigram_polarity + \
            (bigram_polarity * ints.intensifiers.most_highest.modifier)

    return bigram_polarity
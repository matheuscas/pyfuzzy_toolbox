# -*- coding: utf-8 -*-

from addict import Dict
from textblob import TextBlob

# Classes and constants

POS_TAGS = Dict()
POS_TAGS.JJ = 7
POS_TAGS.JJR = 8
POS_TAGS.JJS = 9
POS_TAGS.ADJS = [POS_TAGS.JJ, POS_TAGS.JJR, POS_TAGS.JJS]
POS_TAGS.MD = 11
POS_TAGS.NN = 12
POS_TAGS.NNS = 13
POS_TAGS.NNP = 14
POS_TAGS.NNPS = 15
POS_TAGS.NOUNS = [POS_TAGS.NN, POS_TAGS.NNS, POS_TAGS.NNP, POS_TAGS.NNPS]
POS_TAGS.RB = 20
POS_TAGS.RBR = 21
POS_TAGS.RBS = 22
POS_TAGS.WRB = 36
POS_TAGS.ADVS = [POS_TAGS.RB, POS_TAGS.RBR, POS_TAGS.RBS, POS_TAGS.WRB]
POS_TAGS.VB = 27
POS_TAGS.VBD = 28
POS_TAGS.VBG = 29
POS_TAGS.VBN = 30
POS_TAGS.VBP = 31
POS_TAGS.VBZ = 32
POS_TAGS.VERBS = [POS_TAGS.VB, POS_TAGS.VBD, POS_TAGS.VBG,
                  POS_TAGS.VBN, POS_TAGS.VBP, POS_TAGS.VBZ]
POS_TAGS.USED = POS_TAGS.ADJS + POS_TAGS.ADVS + POS_TAGS.VERBS
NEGATION_WORDS = ['nobody', 'none', 'nothing', 'not',
                  "don't", 'no', "doesn't", "isn't", "aren't"]


class Word(object):

    """docstring for Word"""

    def __init__(self, pos_tag=POS_TAGS.JJ):
        self.word = None
        self.pos_tag = pos_tag
        self.position = None
        self.frequency = None
        self.doc_word_count = None

    def __str__(self):
        return "(%s , %d, %d, %d, %d)" % (self.word, self.pos_tag, self.position, self.frequency, self.doc_word_count)


class Unigram(Word):

    """docstring for Unigram"""

    def __init__(self, pos_tag=POS_TAGS.JJ):
        Word.__init__(self, pos_tag)


class Bigram(object):

    """docstring for Bigram"""

    def __init__(self, word_1=Unigram(), word_2=Unigram()):
        self.word_1 = word_1
        self.word_2 = word_2

    def __str__(self):
        return "(%s , %d, %d, %d, %d) / (%s , %d, %d, %d, %d)" % \
            (self.word_1.word, self.word_1.pos_tag, self.word_1.position, self.word_1.frequency, self.word_1.doc_word_count,
             self.word_2.word, self.word_2.pos_tag, self.word_2.position, self.word_2.frequency, self.word_2.doc_word_count)


class Trigram(object):

    """docstring for Trigram"""

    def __init__(self, word_1=Unigram(), word_2=Unigram(), word_3=Unigram()):
        self.word_1 = word_1
        self.word_2 = word_2
        self.word_3 = word_3

    def __str__(self):
        return "(%s , %d, %d, %d, %d) / (%s , %d, %d, %d, %d) / (%s , %d, %d, %d, %d)" % \
            (self.word_1.word, self.word_1.pos_tag, self.word_1.position, self.word_1.frequency, self.word_1.doc_word_count,
             self.word_2.word, self.word_2.pos_tag, self.word_2.position, self.word_2.frequency, self.word_2.doc_word_count,
             self.word_3.word, self.word_3.pos_tag, self.word_3.position, self.word_3.frequency, self.word_3.doc_word_count)

# Methods


def start(text, adj=True, verbs=True, adv=True, bi_adv_adj=True, bi_adv_verb=True, bi_adv_adv=True, tri_adv_adv_adj=True, far_negation=True):
    splitted_sentences = split_into_sentences(text)
    splitted_sentences = filter_irrealis_block(splitted_sentences)
    return turn_into_bag_of_words(splitted_sentences, adj=adj, verbs=verbs, adv=adv, bi_adv_adj=bi_adv_adj, bi_adv_verb=bi_adv_verb,
                                  bi_adv_adv=bi_adv_adv, tri_adv_adv_adj=tri_adv_adv_adj, far_negation=far_negation)


def split_into_sentences(text):
    """Split a text into sequences. It uses NLTK sentence tokenizer"""

    blob = TextBlob(text)
    return blob.sentences


def filter_irrealis_block(list_of_sentences):
    """Remove sentences with Block Irrealis stated by (Taboada,2011) in Lexicon-Based Methods for Sentiment Analysis. Section 2.5.
    It doesn't filter, though, NPI's, intensional verbs and words inclosed by quotes"""

    modals = ['can', 'could', 'may', 'might',
              'shall', 'should', 'will', 'would', 'must']

    for sentence in list_of_sentences:
        rm_sentence = False
        for modal in modals:
            if modal in sentence:
                rm_sentence = True
                break

        raw_splitted_sentence = sentence.dict['raw'].split()
        if 'if' == raw_splitted_sentence[0] or '?' == raw_splitted_sentence[len(raw_splitted_sentence) - 1]:
            rm_sentence = rm_sentence or True

        if rm_sentence:
            list_of_sentences.remove(sentence)
    return list_of_sentences


def is_unigram(obj):
    return obj.__class__.__name__ == 'Unigram'


def is_bigram(obj):
    return obj.__class__.__name__ == 'Bigram'


def is_trigram(obj):
    return obj.__class__.__name__ == 'Trigram'


def print_formatted_sentences(tokenized_sentences):
    for idx, ts in enumerate(tokenized_sentences):
        print ' ----- SENTENCE %d ----- ' % (idx + 1)
        for ngram in ts:
            print ngram


def filter_bigrams(tokenized_sentences, pos_tags_1, pos_tags_2):

    for sentence in tokenized_sentences:
        for idx, ngram in enumerate(sentence):
            if idx + 1 > len(sentence) - 1:
                break
            if is_unigram(sentence[idx]) and is_unigram(sentence[idx + 1]) and \
                    sentence[idx].pos_tag in pos_tags_1 and \
                    sentence[idx + 1].pos_tag in pos_tags_2:
                bigram = Bigram()
                bigram.word_1 = sentence[idx]
                bigram.word_2 = sentence[idx + 1]
                sentence[idx] = bigram
                sentence.remove(sentence[idx + 1])

    # for sentence in tokenized_sentences:
    #     for ts in sentence:
    #         print ts


def filter_unigrams(tokenized_sentences, pos_tags):

    for sentence in tokenized_sentences:
        for ngram in sentence[:]:
            if is_unigram(ngram) and ngram.pos_tag in pos_tags:
                sentence.remove(ngram)


def tag_negation(tokenized_sentences, adj, verbs, adv, bi_adv_adj, bi_adv_verb, bi_adv_adv, tri_adv_adv_adj):

    for ts in tokenized_sentences:
        for ngram in ts[:]:
            if is_bigram(ngram) and ngram.word_1.word.lower() in NEGATION_WORDS:
                for x in range(ts.index(ngram) + 1, len(ts)):
                    if is_unigram(ts[x]) and ts[x].word.lower() not in NEGATION_WORDS:
                        bigram = Bigram()
                        bigram.word_1 = ngram.word_1
                        bigram.word_2 = ts[x]
                        ts[x] = bigram

    for ts in tokenized_sentences:
        for ngram in ts[:]:
            if is_unigram(ngram) and ngram.word.lower() in NEGATION_WORDS:
                for x in range(ts.index(ngram) + 1, len(ts)):
                    if is_unigram(ts[x]) and ts[x].word.lower() not in NEGATION_WORDS:
                        bigram = Bigram()
                        bigram.word_1 = ngram
                        bigram.word_2 = ts[x]
                        ts[x] = bigram


def turn_into_bag_of_words(list_of_sentences, adj=True, verbs=True, adv=True, bi_adv_adj=True,
                           bi_adv_verb=True, bi_adv_adv=True, tri_adv_adv_adj=True,
                           far_negation=True):
    """Return a list of bag of Words related to each sentences based on params"""

    # count tokens
    tokens_qtd = 0
    filtered_text = ''
    for sentence in list_of_sentences:
        tokens_qtd = tokens_qtd + len(sentence.words)
        filtered_text = filtered_text + sentence.dict['raw']

    # create unigrams
    filtered_text_blob = TextBlob(filtered_text)
    tokenized_sentences = []
    for sentence in list_of_sentences:
        tokenized_sen = []
        position = 0
        for (word, tag) in sentence.tags:  # TODO configure the proper tagger
            word_counts = filtered_text_blob.word_counts[word]
            if word_counts > 0:
                position = position + 1
                unigram = Unigram()
                unigram.word = word
                unigram.pos_tag = POS_TAGS[tag] if POS_TAGS[tag] else 0
                unigram.position = position
                unigram.frequency = word_counts
                unigram.doc_word_count = tokens_qtd
                tokenized_sen.append(unigram)
        tokenized_sentences.append(tokenized_sen)

    # if set search for trigrams
    if tri_adv_adv_adj:
        for sentence in tokenized_sentences:
            for idx, ngram in enumerate(sentence):
                if idx + 2 > len(sentence) - 1:
                    break
                if sentence[idx].pos_tag in POS_TAGS.ADVS and sentence[idx + 1].pos_tag in POS_TAGS.ADVS and sentence[idx + 2].pos_tag in POS_TAGS.ADVS:
                    trigram = Trigram()
                    trigram.word_1 = sentence[idx]
                    trigram.word_2 = sentence[idx + 1]
                    trigram.word_3 = sentence[idx + 2]
                    sentence[idx] = trigram
                    sentence.remove(sentence[idx + 2])
                    sentence.remove(sentence[idx + 1])

    if bi_adv_adj:
        filter_bigrams(tokenized_sentences, POS_TAGS.ADVS, POS_TAGS.ADJS)

    if bi_adv_adv:
        filter_bigrams(tokenized_sentences, POS_TAGS.ADVS, POS_TAGS.ADVS)

    if bi_adv_verb:
        filter_bigrams(tokenized_sentences, POS_TAGS.ADVS, POS_TAGS.VERBS)

    if not adv:
        filter_unigrams(tokenized_sentences, POS_TAGS.ADVS)

    if not verbs:
        filter_unigrams(tokenized_sentences, POS_TAGS.VERBS)

    if not adj:
        filter_unigrams(tokenized_sentences, POS_TAGS.ADJS)

    for sentence in tokenized_sentences:
        for ngram in sentence[:]:
            if is_unigram(ngram) and ngram.pos_tag not in POS_TAGS.USED:
                sentence.remove(ngram)

    if far_negation:
        tag_negation(tokenized_sentences, adj, verbs, adv,
                     bi_adv_adj, bi_adv_verb, bi_adv_adv, tri_adv_adv_adj)

    # print_formatted_sentences(tokenized_sentences)

    return tokenized_sentences

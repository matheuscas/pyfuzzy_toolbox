import preprocessing as pre

ADJS = 0
ADVS = 1
VERBS = 2
ALL = 3


def sum_of_unigrams_scores(bow_sentences, unigram=ADJS, positive=True, ratio=False):

    pos_tags_codes = pre.POS_TAGS.ADJS

    if unigram == ADVS:
        pos_tags_codes = pre.POS_TAGS.ADVS
    elif unigram == VERBS:
        pos_tags_codes = pre.POS_TAGS.VERBS
    elif unigram == ALL:
        pos_tags_codes = pre.POS_TAGS.ADJS + \
            pre.POS_TAGS.ADVS + pre.POS_TAGS.VERBS

    polarity_eval_stm = 'ngram.polarity > 0'
    if not positive:
        polarity_eval_stm = 'ngram.polarity < 0'

    _sum = 0
    doc_word_count = 1
    for bs in bow_sentences:
        for ngram in bs:
            if pre.is_unigram(ngram) and ngram.pos_tag in pos_tags_codes and eval(polarity_eval_stm):
                _sum = _sum + ngram.polarity
                doc_word_count = ngram.doc_word_count

    return _sum if not ratio else (_sum / float(doc_word_count))


def positive_to_negative_ratio_sum_unigrams_scores(bow_sentences, unigram=ADJS):
    positive_sum = sum_of_unigrams_scores(bow_sentences, unigram=unigram)
    negative_sum = sum_of_unigrams_scores(bow_sentences, unigram=unigram, positive=False)
    return positive_sum + negative_sum

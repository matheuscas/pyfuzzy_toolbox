import preprocessing as pre

ADJS = 0
ADVS = 1
VERBS = 2
ALL = 3


def set_pos_tags_codes(unigram_type=ADJS):

    pos_tags_codes = pre.POS_TAGS.ADJS

    if unigram_type == ADVS:
        pos_tags_codes = pre.POS_TAGS.ADVS
    elif unigram_type == VERBS:
        pos_tags_codes = pre.POS_TAGS.VERBS
    elif unigram_type == ALL:
        pos_tags_codes = pre.POS_TAGS.ADJS + \
            pre.POS_TAGS.ADVS + pre.POS_TAGS.VERBS

    return pos_tags_codes


def set_ngram_polarity_statement(positive=True):

    polarity_eval_stm = 'ngram.polarity > 0'
    if not positive:
        polarity_eval_stm = 'ngram.polarity < 0'

    return polarity_eval_stm


def sum_of_unigrams_scores(bow_sentences, unigram=ADJS, positive=True, ratio=False):

    pos_tags_codes = set_pos_tags_codes(unigram)

    polarity_eval_stm = set_ngram_polarity_statement(positive=positive)

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
    negative_sum = sum_of_unigrams_scores(
        bow_sentences, unigram=unigram, positive=False)
    return positive_sum + negative_sum


def sum_of_bigrams_scores(bow_sentences, bigram_word_1=ADVS, bigram_word_2=ADJS, positive=True, ratio=False):

    pos_tags_codes_word_1 = set_pos_tags_codes(bigram_word_1)
    pos_tags_codes_word_2 = set_pos_tags_codes(bigram_word_2)

    polarity_eval_stm = set_ngram_polarity_statement(positive=positive)

    _sum = 0
    doc_word_count = 1
    for bs in bow_sentences:
        for ngram in bs:
            if pre.is_bigram(ngram) and \
                    (ngram.word_1.pos_tag in pos_tags_codes_word_1) and \
                    (ngram.word_2.pos_tag in pos_tags_codes_word_2) and \
                    eval(polarity_eval_stm):
                    _sum = _sum + ngram.polarity
                    doc_word_count = ngram.word_2.doc_word_count

    return _sum if not ratio else (_sum / float(doc_word_count))


def sum_of_unigrams_and_bigrams_scores(bow_sentences, unigram=ADJS, bigram_word_1=ADVS, bigram_word_2=ADJS, positive=True, ratio=False):
    unigrams_sum = sum_of_unigrams_scores(bow_sentences, unigram=unigram, positive=positive, ratio=ratio)
    bigrams_sum = sum_of_bigrams_scores(bow_sentences, bigram_word_1=bigram_word_1, bigram_word_2=bigram_word_2, positive=positive, ratio=ratio)
    return unigrams_sum + bigrams_sum


def positive_to_negative_ratio_sum_unigrams_and_bigrams_scores(bow_sentences, unigram=ADJS, bigram_word_1=ADVS, bigram_word_2=ADJS):
    positive_unigrams_and_bigrams_sum = sum_of_unigrams_and_bigrams_scores(bow_sentences, unigram=unigram, bigram_word_1=bigram_word_1, bigram_word_2=bigram_word_2)
    negative_unigrams_and_bigrams_sum = sum_of_unigrams_and_bigrams_scores(bow_sentences, unigram=unigram, bigram_word_1=bigram_word_1, bigram_word_2=bigram_word_2, positive=False)
    return positive_unigrams_and_bigrams_sum + negative_unigrams_and_bigrams_sum


# UNTESTED
def sum_of_trigrams_scores(bow_sentences, bigram_word_1=ADVS, bigram_word_2=ADVS, bigram_word_3=ADJS, positive=True, ratio=False):

    pos_tags_codes_word_1 = set_pos_tags_codes(bigram_word_1)
    pos_tags_codes_word_2 = set_pos_tags_codes(bigram_word_2)
    pos_tags_codes_word_3 = set_pos_tags_codes(bigram_word_3)

    polarity_eval_stm = set_ngram_polarity_statement(positive=positive)

    _sum = 0
    doc_word_count = 1
    for bs in bow_sentences:
        for ngram in bs:
            if pre.is_trigram(ngram) and \
                    (ngram.word_1.pos_tag in pos_tags_codes_word_1) and \
                    (ngram.word_2.pos_tag in pos_tags_codes_word_2) and \
                    (ngram.word_3.pos_tag in pos_tags_codes_word_3) and \
                    eval(polarity_eval_stm):
                    _sum = _sum + ngram.polarity
                    doc_word_count = ngram.word_3.doc_word_count

    return _sum if not ratio else (_sum / float(doc_word_count))


def count_of_unigrams_scores(bow_sentences, unigram=ADJS, positive=True):

    pos_tags_codes = set_pos_tags_codes(unigram)

    polarity_eval_stm = set_ngram_polarity_statement(positive=positive)

    _count = 0
    for bs in bow_sentences:
        for ngram in bs:
            if pre.is_unigram(ngram) and ngram.pos_tag in pos_tags_codes and eval(polarity_eval_stm):
                _count += 1

    return _count


def count_of_bigrams_scores(bow_sentences, bigram_word_1=ADVS, bigram_word_2=ADJS, positive=True):

    pos_tags_codes_word_1 = set_pos_tags_codes(bigram_word_1)
    pos_tags_codes_word_2 = set_pos_tags_codes(bigram_word_2)

    polarity_eval_stm = set_ngram_polarity_statement(positive=positive)

    _count = 0
    for bs in bow_sentences:
        for ngram in bs:
            if pre.is_bigram(ngram) and \
                    (ngram.word_1.pos_tag in pos_tags_codes_word_1) and \
                    (ngram.word_2.pos_tag in pos_tags_codes_word_2) and \
                    eval(polarity_eval_stm):
                    _count += 1

    return _count


def positive_to_negative_ratio_count_unigrams_scores(bow_sentences, unigram=ADJS):
    positive_sum = count_of_unigrams_scores(bow_sentences, unigram=unigram)
    negative_sum = count_of_unigrams_scores(
        bow_sentences, unigram=unigram, positive=False)
    return positive_sum - negative_sum


def count_of_unigrams_and_bigrams_scores(bow_sentences, unigram=ADJS, bigram_word_1=ADVS, bigram_word_2=ADJS, positive=True):
    unigrams_count = count_of_unigrams_scores(bow_sentences, unigram=unigram, positive=positive)
    bigrams_count = count_of_bigrams_scores(bow_sentences, bigram_word_1=bigram_word_1, bigram_word_2=bigram_word_2, positive=positive)
    return unigrams_count + bigrams_count


def positive_to_negative_ratio_count_unigrams_and_bigrams_scores(bow_sentences, unigram=ADJS, bigram_word_1=ADVS, bigram_word_2=ADJS):
    positive_unigrams_and_bigrams_count = count_of_unigrams_and_bigrams_scores(bow_sentences, unigram=unigram, bigram_word_1=bigram_word_1, bigram_word_2=bigram_word_2)
    negative_unigrams_and_bigrams_count = count_of_unigrams_and_bigrams_scores(bow_sentences, unigram=unigram, bigram_word_1=bigram_word_1, bigram_word_2=bigram_word_2, positive=False)
    return positive_unigrams_and_bigrams_count - negative_unigrams_and_bigrams_count

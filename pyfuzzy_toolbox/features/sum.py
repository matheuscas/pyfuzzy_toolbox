from . import pre
from . import set_pos_tags_codes
from . import set_ngram_polarity_statement
from . import ADJS, ADVS, VERBS, ALL, ADJS_AND_ADVS, ADJS_AND_VERBS, ADVS_AND_VERBS,\
    ADJS_AND_BI_ADV_ADJ, ADVS_AND_BI_ADV_ADV, VERBS_AND_BI_ADV_VERB, ALL_NON_GENERAL_BIGRAMS


""" ------------------------------ Base functions ------------------------------ """


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
    unigrams_sum = sum_of_unigrams_scores(
        bow_sentences, unigram=unigram, positive=positive, ratio=ratio)
    bigrams_sum = sum_of_bigrams_scores(
        bow_sentences, bigram_word_1=bigram_word_1, bigram_word_2=bigram_word_2, positive=positive, ratio=ratio)
    return unigrams_sum + bigrams_sum


def positive_to_negative_ratio_sum_unigrams_and_bigrams_scores(bow_sentences, unigram=ADJS, bigram_word_1=ADVS, bigram_word_2=ADJS):
    positive_unigrams_and_bigrams_sum = sum_of_unigrams_and_bigrams_scores(
        bow_sentences, unigram=unigram, bigram_word_1=bigram_word_1, bigram_word_2=bigram_word_2)
    negative_unigrams_and_bigrams_sum = sum_of_unigrams_and_bigrams_scores(
        bow_sentences, unigram=unigram, bigram_word_1=bigram_word_1, bigram_word_2=bigram_word_2, positive=False)
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


""" ------------------------------ Features functions ------------------------------ """


def positive_adjectives_sum(bow_sentences):
    return {'value': sum_of_unigrams_scores(bow_sentences), 'name': 'positive_adjectives_sum'}


def negative_adjectives_sum(bow_sentences):
    return {'value': sum_of_unigrams_scores(
            bow_sentences, unigram=ADJS, positive=False), 'name': 'negative_adjectives_sum'}


def positive_adverbs_sum(bow_sentences):
    return {'value': sum_of_unigrams_scores(
            bow_sentences, unigram=ADVS, positive=True), 'name': 'positive_adverbs_sum'}


def negative_adverbs_sum(bow_sentences):
    return {'value': sum_of_unigrams_scores(
            bow_sentences, unigram=ADVS, positive=False), 'name': 'negative_adverbs_sum'}


def positive_verbs_sum(bow_sentences):
    return {'value': sum_of_unigrams_scores(
            bow_sentences, unigram=VERBS, positive=True), 'name': 'positive_verbs_sum'}


def negative_verbs_sum(bow_sentences):
    return {'value': sum_of_unigrams_scores(
            bow_sentences, unigram=VERBS, positive=False), 'name': 'positive_verbs_sum'}


def sum_ratio_of_positive_adjectives(bow_sentences):
    return {'value': sum_of_unigrams_scores(
        bow_sentences, ratio=True), 'name': 'sum_ratio_of_positive_adjectives'}


def sum_ratio_of_positive_adverbs(bow_sentences):
    return {'value': sum_of_unigrams_scores(
        bow_sentences, unigram=ADVS, ratio=True), 'name': 'sum_ratio_of_positive_adverbs'}


def sum_ratio_of_positive_verbs(bow_sentences):
    return {'value': sum_of_unigrams_scores(
        bow_sentences, unigram=VERBS, ratio=True), 'name': 'sum_ratio_of_positive_verbs'}


def sum_ratio_of_negative_adjectives(bow_sentences):
    return {'value': sum_of_unigrams_scores(
        bow_sentences, ratio=True, positive=False), 'name': 'sum_ratio_of_negative_adjectives'}


def sum_ratio_of_negative_adverbs(bow_sentences):
    return {'value': sum_of_unigrams_scores(
        bow_sentences, unigram=ADVS, ratio=True, positive=False), 'name': 'sum_ratio_of_negative_adverbs'}


def sum_ratio_of_negative_verbs(bow_sentences):
    return {'value': sum_of_unigrams_scores(
        bow_sentences, unigram=VERBS, ratio=True, positive=False), 'name': 'sum_ratio_of_negative_verbs'}


def positive_to_negative_ratio_of_adjectives_sum(bow_sentences):
    return {'value': positive_to_negative_ratio_sum_unigrams_scores(
            bow_sentences, unigram=ADJS), 'name': 'positive_to_negative_ratio_of_adjectives_sum'}


def positive_to_negative_ratio_of_adverbs_sum(bow_sentences):
    return {'value': positive_to_negative_ratio_sum_unigrams_scores(
            bow_sentences, unigram=ADVS), 'name': 'positive_to_negative_ratio_of_adverbs_sum'}


def positive_to_negative_ratio_of_verbs_sum(bow_sentences):
    return {'value': positive_to_negative_ratio_sum_unigrams_scores(
            bow_sentences, unigram=VERBS), 'name': 'positive_to_negative_ratio_of_verbs_sum'}


def positive_adjectives_sum_and_bigrams_with_adjectives(bow_sentences):
    return {'value': sum_of_unigrams_and_bigrams_scores(
            bow_sentences, unigram=ADJS, bigram_word_1=ADVS, bigram_word_2=ADJS, positive=True), 'name': 'positive_adjectives_sum_and_bigrams_with_adjectives'}


def negative_adjectives_sum_and_bigrams_with_adjectives(bow_sentences):
    return {'value': sum_of_unigrams_and_bigrams_scores(
            bow_sentences, unigram=ADJS, bigram_word_1=ADVS, bigram_word_2=ADJS, positive=False), 'name': 'negative_adjectives_sum_and_bigrams_with_adjectives'}


def positive_adverbs_sum_and_bigrams_with_adverbs(bow_sentences):
    return {'value': sum_of_unigrams_and_bigrams_scores(
            bow_sentences, unigram=ADVS, bigram_word_1=ADVS, bigram_word_2=ADVS, positive=True), 'name': 'positive_adverbs_sum_and_bigrams_with_adverbs'}


def negative_adverbs_sum_and_bigrams_with_adverbs(bow_sentences):
    return {'value': sum_of_unigrams_and_bigrams_scores(
            bow_sentences, unigram=ADVS, bigram_word_1=ADVS, bigram_word_2=ADVS, positive=False), 'name': 'negative_adverbs_sum_and_bigrams_with_adverbs'}


def positive_verbs_sum_and_bigrams_with_verbs(bow_sentences):
    return {'value': sum_of_unigrams_and_bigrams_scores(
            bow_sentences, unigram=VERBS, bigram_word_1=ADVS, bigram_word_2=VERBS, positive=True), 'name': 'positive_verbs_sum_and_bigrams_with_verbs'}


def negative_verbs_sum_and_bigrams_with_verbs(bow_sentences):
    return {'value': sum_of_unigrams_and_bigrams_scores(
            bow_sentences, unigram=VERBS, bigram_word_1=ADVS, bigram_word_2=VERBS, positive=False), 'name': 'negative_verbs_sum_and_bigrams_with_verbs'}


def positive_unigrams_and_bigrams_sum(bow_sentences):
    return {'value': sum_of_unigrams_and_bigrams_scores(
            bow_sentences, unigram=ALL, bigram_word_1=ALL, bigram_word_2=ALL, positive=True), 'name': 'positive_unigrams_and_bigrams_sum'}


def negative_unigrams_and_bigrams_sum(bow_sentences):
    return {'value': sum_of_unigrams_and_bigrams_scores(
            bow_sentences, unigram=ALL, bigram_word_1=ALL, bigram_word_2=ALL, positive=False), 'name': 'negative_unigrams_and_bigrams_sum'}


def positive_unigrams_bigrams_and_trigrams_sum(bow_sentences, ratio=False):
    unigrams_and_bigrams_scores = sum_of_unigrams_and_bigrams_scores(bow_sentences,
                                                                     unigram=ALL,
                                                                     bigram_word_1=ALL,
                                                                     bigram_word_2=ALL,
                                                                     positive=True,
                                                                     ratio=ratio)
    trigram_scores = sum_of_trigrams_scores(bow_sentences,
                                            bigram_word_1=ALL,
                                            bigram_word_2=ALL,
                                            bigram_word_3=ALL,
                                            positive=True,
                                            ratio=ratio)

    return {'value': unigrams_and_bigrams_scores + trigram_scores, 'name': 'positive_unigrams_bigrams_and_trigrams_sum'}


def negative_unigrams_bigrams_and_trigrams_sum(bow_sentences, ratio=False):
    unigrams_and_bigrams_scores = sum_of_unigrams_and_bigrams_scores(bow_sentences,
                                                                     unigram=ALL,
                                                                     bigram_word_1=ALL,
                                                                     bigram_word_2=ALL,
                                                                     positive=False,
                                                                     ratio=ratio)
    trigram_scores = sum_of_trigrams_scores(bow_sentences,
                                            bigram_word_1=ALL,
                                            bigram_word_2=ALL,
                                            bigram_word_3=ALL,
                                            positive=False,
                                            ratio=ratio)
    return {'value': unigrams_and_bigrams_scores + trigram_scores, 'name': 'negative_unigrams_bigrams_and_trigrams_sum'}


def sum_ratio_of_positive_adjectives_and_bigrams_with_adjectives(bow_sentences):
    return {'value': sum_of_unigrams_and_bigrams_scores(bow_sentences, ratio=True), 'name': 'sum_ratio_of_positive_adjectives_and_bigrams_with_adjectives'}


def sum_ratio_of_negative_adjectives_and_bigrams_with_adjectives(bow_sentences):
    return {'value': sum_of_unigrams_and_bigrams_scores(bow_sentences, positive=False, ratio=True), 'name': 'sum_ratio_of_negative_adjectives_and_bigrams_with_adjectives'}


def sum_ratio_of_positive_adverbs_and_bigrams_with_adverbs(bow_sentences):
    return {'value': sum_of_unigrams_and_bigrams_scores(bow_sentences, unigram=ADVS, bigram_word_1=ADVS, bigram_word_2=ADVS, ratio=True), 'name': 'sum_ratio_of_positive_adverbs_and_bigrams_with_adverbs'}


def sum_ratio_of_negative_adverbs_and_bigrams_with_adverbs(bow_sentences):
    return {'value': sum_of_unigrams_and_bigrams_scores(bow_sentences, unigram=ADVS, bigram_word_1=ADVS, bigram_word_2=ADVS, positive=False, ratio=True), 'name': 'sum_ratio_of_negative_adverbs_and_bigrams_with_adverbs'}


def sum_ratio_of_positive_verbs_and_bigrams_with_verbs(bow_sentences):
    return {'value': sum_of_unigrams_and_bigrams_scores(bow_sentences, unigram=VERBS, bigram_word_1=ADVS, bigram_word_2=VERBS, ratio=True), 'name': 'sum_ratio_of_positive_verbs_and_bigrams_with_verbs'}


def sum_ratio_of_negative_verbs_and_bigrams_with_verbs(bow_sentences):
    return {'value': sum_of_unigrams_and_bigrams_scores(bow_sentences, unigram=VERBS, bigram_word_1=ADVS, bigram_word_2=VERBS, positive=False, ratio=True), 'name': 'sum_ratio_of_negative_verbs_and_bigrams_with_verbs'}


def sum_ratio_of_positive_unigrams_and_bigrams(bow_sentences):
    return {'value': sum_of_unigrams_and_bigrams_scores(bow_sentences, unigram=ALL, bigram_word_1=ALL, bigram_word_2=ALL, ratio=True), 'name': 'sum_ratio_of_positive_unigrams_and_bigrams'}


def sum_ratio_of_negative_unigrams_and_bigrams(bow_sentences):
    return {'value': sum_of_unigrams_and_bigrams_scores(bow_sentences, unigram=ALL, bigram_word_1=ALL, bigram_word_2=ALL, positive=False, ratio=True), 'name': 'sum_ratio_of_negative_unigrams_and_bigrams'}


def sum_ratio_of_positive_unigrams_bigrams_and_trigrams(bow_sentences):
	return {'value': positive_unigrams_bigrams_and_trigrams_sum(bow_sentences, ratio=True)['value'], 'name': 'sum_ratio_of_positive_unigrams_bigrams_and_trigrams'}


def sum_ratio_of_negative_unigrams_bigrams_and_trigrams(bow_sentences):
	return {'value': negative_unigrams_bigrams_and_trigrams_sum(bow_sentences, ratio=True)['value'], 'name': 'sum_ratio_of_negative_unigrams_bigrams_and_trigrams'}


def positive_to_negative_ratio_of_adjectives_sum_and_bigrams_with_adjectives(bow_sentences):
    return {'value': positive_to_negative_ratio_sum_unigrams_and_bigrams_scores(
            bow_sentences, unigram=ADJS, bigram_word_1=ADVS, bigram_word_2=ADJS), 'name': 'positive_to_negative_ratio_of_adjectives_sum_and_bigrams_with_adjectives'}


def positive_to_negative_ratio_of_adverbs_sum_and_bigrams_with_adverbs(bow_sentences):
    return {'value': positive_to_negative_ratio_sum_unigrams_and_bigrams_scores(
            bow_sentences, unigram=ADVS, bigram_word_1=ADVS, bigram_word_2=ADVS), 'name': 'positive_to_negative_ratio_of_adverbs_sum_and_bigrams_with_adverbs'}


def positive_to_negative_ratio_of_verbs_sum_and_bigrams_with_verbs(bow_sentences):
    return {'value': positive_to_negative_ratio_sum_unigrams_and_bigrams_scores(
            bow_sentences, unigram=VERBS, bigram_word_1=ADVS, bigram_word_2=VERBS), 'name': 'positive_to_negative_ratio_of_verbs_sum_and_bigrams_with_verbs'}


def positive_to_negative_ratio_of_unigrams_and_bigrams_sum(bow_sentences):
    return {'value': positive_to_negative_ratio_sum_unigrams_and_bigrams_scores(
            bow_sentences, unigram=ALL, bigram_word_1=ALL, bigram_word_2=ALL), 'name': 'positive_to_negative_ratio_of_unigrams_and_bigrams_sum'}


def positive_to_negative_ratio_of_unigrams_bigrams_and_trigrams_sum(bow_sentences):
    positive_to_negative_ratio = (positive_unigrams_bigrams_and_trigrams_sum(bow_sentences)['value'] -
                                  negative_unigrams_bigrams_and_trigrams_sum(bow_sentences)['value'])
    return {'value': positive_to_negative_ratio, 'name': 'positive_to_negative_ratio_of_unigrams_bigrams_and_trigrams_sum'}


def all(bow_sentences,
        unigrams=True,
        unigrams_ratio=True,
        unigram_type=ALL,
        non_general_unigrams_and_bigrams=True,
        non_general_unigrams_and_bigrams_ratio=True,
        non_general_bigram_type=ALL_NON_GENERAL_BIGRAMS,
        general_unigrams_and_bigrams=True,
        general_unigrams_and_bigrams_ratio=True,
        unigrams_and_bigrams_trigram=True,
        unigrams_and_bigrams_trigram_ratio=True):

    features_list = []
    if unigrams:
        if unigram_type == ADJS:
            features_list.append(positive_adjectives_sum(bow_sentences))
            features_list.append(negative_adjectives_sum(bow_sentences))
        elif unigram_type == ADJS_AND_ADVS:
            features_list.append(positive_adjectives_sum(bow_sentences))
            features_list.append(negative_adjectives_sum(bow_sentences))
            features_list.append(positive_adverbs_sum(bow_sentences))
            features_list.append(negative_adverbs_sum(bow_sentences))
        elif unigram_type == ADJS_AND_VERBS:
            features_list.append(positive_adjectives_sum(bow_sentences))
            features_list.append(negative_adjectives_sum(bow_sentences))
            features_list.append(positive_verbs_sum(bow_sentences))
            features_list.append(negative_verbs_sum(bow_sentences))
        elif unigram_type == ADVS_AND_VERBS:
            features_list.append(positive_adverbs_sum(bow_sentences))
            features_list.append(negative_adverbs_sum(bow_sentences))
            features_list.append(positive_verbs_sum(bow_sentences))
            features_list.append(negative_verbs_sum(bow_sentences))
        elif unigram_type == ADVS:
            features_list.append(positive_adverbs_sum(bow_sentences))
            features_list.append(negative_adverbs_sum(bow_sentences))
        elif unigram_type == VERBS:
            features_list.append(positive_verbs_sum(bow_sentences))
            features_list.append(negative_verbs_sum(bow_sentences))
        else:
            features_list.append(positive_adjectives_sum(bow_sentences))
            features_list.append(negative_adjectives_sum(bow_sentences))
            features_list.append(positive_adverbs_sum(bow_sentences))
            features_list.append(negative_adverbs_sum(bow_sentences))
            features_list.append(positive_verbs_sum(bow_sentences))
            features_list.append(negative_verbs_sum(bow_sentences))

    if unigrams_ratio:
        features_list.append(
            positive_to_negative_ratio_of_adjectives_sum(bow_sentences))
        features_list.append(
            positive_to_negative_ratio_of_adverbs_sum(bow_sentences))
        features_list.append(
            positive_to_negative_ratio_of_verbs_sum(bow_sentences))
        features_list.append(sum_ratio_of_positive_adjectives(bow_sentences))
        features_list.append(sum_ratio_of_positive_adverbs(bow_sentences))
        features_list.append(sum_ratio_of_positive_verbs(bow_sentences))
        features_list.append(sum_ratio_of_negative_adjectives(bow_sentences))
        features_list.append(sum_ratio_of_negative_adverbs(bow_sentences))
        features_list.append(sum_ratio_of_negative_verbs(bow_sentences))

    if non_general_unigrams_and_bigrams:
        if non_general_bigram_type == ADVS_AND_BI_ADV_ADV:
            features_list.append(
                positive_adverbs_sum_and_bigrams_with_adverbs(bow_sentences))
            features_list.append(
                negative_adverbs_sum_and_bigrams_with_adverbs(bow_sentences))
        elif non_general_bigram_type == VERBS_AND_BI_ADV_VERB:
            features_list.append(
                positive_verbs_sum_and_bigrams_with_verbs(bow_sentences))
            features_list.append(
                negative_verbs_sum_and_bigrams_with_verbs(bow_sentences))
        elif non_general_bigram_type == ADJS_AND_BI_ADV_ADJ:
            features_list.append(
                positive_adjectives_sum_and_bigrams_with_adjectives(bow_sentences))
            features_list.append(
                negative_adjectives_sum_and_bigrams_with_adjectives(bow_sentences))
        else:
            features_list.append(
                positive_adverbs_sum_and_bigrams_with_adverbs(bow_sentences))
            features_list.append(
                negative_adverbs_sum_and_bigrams_with_adverbs(bow_sentences))
            features_list.append(
                positive_verbs_sum_and_bigrams_with_verbs(bow_sentences))
            features_list.append(
                negative_verbs_sum_and_bigrams_with_verbs(bow_sentences))
            features_list.append(
                positive_adjectives_sum_and_bigrams_with_adjectives(bow_sentences))
            features_list.append(
                negative_adjectives_sum_and_bigrams_with_adjectives(bow_sentences))

    if non_general_unigrams_and_bigrams_ratio:
        features_list.append(
            positive_to_negative_ratio_of_adjectives_sum_and_bigrams_with_adjectives(bow_sentences))
        features_list.append(
            positive_to_negative_ratio_of_adverbs_sum_and_bigrams_with_adverbs(bow_sentences))
        features_list.append(
            positive_to_negative_ratio_of_verbs_sum_and_bigrams_with_verbs(bow_sentences))
        features_list.append(
            sum_ratio_of_positive_adjectives_and_bigrams_with_adjectives(bow_sentences))
        features_list.append(
            sum_ratio_of_negative_adjectives_and_bigrams_with_adjectives(bow_sentences))
        features_list.append(
            sum_ratio_of_positive_adverbs_and_bigrams_with_adverbs(bow_sentences))
        features_list.append(
            sum_ratio_of_negative_adverbs_and_bigrams_with_adverbs(bow_sentences))
        features_list.append(
            sum_ratio_of_positive_verbs_and_bigrams_with_verbs(bow_sentences))
        features_list.append(
            sum_ratio_of_negative_verbs_and_bigrams_with_verbs(bow_sentences))

    if general_unigrams_and_bigrams:
        features_list.append(
            positive_unigrams_and_bigrams_sum(bow_sentences))
        features_list.append(
            negative_unigrams_and_bigrams_sum(bow_sentences))

    if general_unigrams_and_bigrams_ratio:
    	features_list.append(
            sum_ratio_of_positive_unigrams_and_bigrams(bow_sentences))
    	features_list.append(
            sum_ratio_of_negative_unigrams_and_bigrams(bow_sentences))
        features_list.append(
            positive_to_negative_ratio_of_unigrams_and_bigrams_sum(bow_sentences))

    if unigrams_and_bigrams_trigram:
        features_list.append(
            positive_unigrams_bigrams_and_trigrams_sum(bow_sentences))
        features_list.append(
            negative_unigrams_bigrams_and_trigrams_sum(bow_sentences))

    if unigrams_and_bigrams_trigram_ratio:
        features_list.append(
            sum_ratio_of_positive_unigrams_bigrams_and_trigrams(bow_sentences))
        features_list.append(
            sum_ratio_of_negative_unigrams_bigrams_and_trigrams(bow_sentences))
        features_list.append(
            positive_to_negative_ratio_of_unigrams_bigrams_and_trigrams_sum(bow_sentences))

    return features_list

from . import pre
from . import set_pos_tags_codes
from . import set_ngram_polarity_statement
from . import ADJS, ADVS, VERBS, ALL, ADJS_AND_ADVS, ADJS_AND_VERBS, ADVS_AND_VERBS,\
    ADJS_AND_BI_ADV_ADJ, ADVS_AND_BI_ADV_ADV, VERBS_AND_BI_ADV_VERB, ALL_NON_GENERAL_BIGRAMS


""" ------------------------------ Base functions ------------------------------ """


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
    unigrams_count = count_of_unigrams_scores(
        bow_sentences, unigram=unigram, positive=positive)
    bigrams_count = count_of_bigrams_scores(
        bow_sentences, bigram_word_1=bigram_word_1, bigram_word_2=bigram_word_2, positive=positive)
    return unigrams_count + bigrams_count


def positive_to_negative_ratio_count_unigrams_and_bigrams_scores(bow_sentences, unigram=ADJS, bigram_word_1=ADVS, bigram_word_2=ADJS):
    positive_unigrams_and_bigrams_count = count_of_unigrams_and_bigrams_scores(
        bow_sentences, unigram=unigram, bigram_word_1=bigram_word_1, bigram_word_2=bigram_word_2)
    negative_unigrams_and_bigrams_count = count_of_unigrams_and_bigrams_scores(
        bow_sentences, unigram=unigram, bigram_word_1=bigram_word_1, bigram_word_2=bigram_word_2, positive=False)
    return positive_unigrams_and_bigrams_count - negative_unigrams_and_bigrams_count


# UNTESTED
def count_of_trigrams_scores(bow_sentences, trigram_word_1=ADVS, trigram_word_2=ADVS, trigram_word_3=ADJS, positive=True):

    pos_tags_codes_word_1 = set_pos_tags_codes(trigram_word_1)
    pos_tags_codes_word_2 = set_pos_tags_codes(trigram_word_2)
    pos_tags_codes_word_3 = set_pos_tags_codes(trigram_word_3)

    polarity_eval_stm = set_ngram_polarity_statement(positive=positive)

    _count = 0
    for bs in bow_sentences:
        for ngram in bs:
            if pre.is_trigram(ngram) and \
                (ngram.word_1.pos_tag in pos_tags_codes_word_1) and \
                (ngram.word_2.pos_tag in pos_tags_codes_word_2) and \
                (ngram.word_3.pos_tag in pos_tags_codes_word_3) and \
                    eval(polarity_eval_stm):
                _count += 1

    return _count

# UNTESTED


def count_of_unigrams_bigrams_and_trigrams_scores(bow_sentences,
                                                  unigram=ADJS,
                                                  bigram_word_1=ADVS, bigram_word_2=ADJS,
                                                  trigram_word_1=ADVS, trigram_word_2=ADVS, trigram_word_3=ADJS,
                                                  positive=True):

    unigrams_count_and_bigrams_count = count_of_unigrams_and_bigrams_scores(bow_sentences,
                                                                            unigram=unigram,
                                                                            bigram_word_1=bigram_word_1, bigram_word_2=bigram_word_2,
                                                                            positive=positive)
    return unigrams_count_and_bigrams_count + count_of_trigrams_scores(bow_sentences,
                                                                       trigram_word_1=trigram_word_1,
                                                                       trigram_word_2=trigram_word_2,
                                                                       trigram_word_3=trigram_word_3,
                                                                       positive=positive)

# UNTESTED


def positive_to_negative_ratio_count_unigrams_bigrams_and_trigrams_scores(bow_sentences,
                                                                          unigram=ADJS,
                                                                          bigram_word_1=ADVS, bigram_word_2=ADJS,
                                                                          trigram_word_1=ADVS, trigram_word_2=ADVS, trigram_word_3=ADJS):

    all_ratio_positives = count_of_unigrams_bigrams_and_trigrams_scores(bow_sentences,
                                                                        unigram=unigram,
                                                                        bigram_word_1=bigram_word_1, bigram_word_2=bigram_word_2,
                                                                        trigram_word_1=trigram_word_1, trigram_word_2=trigram_word_2, trigram_word_3=trigram_word_3,
                                                                        positive=True)
    return all_ratio_positives - count_of_unigrams_bigrams_and_trigrams_scores(bow_sentences,
                                                                               unigram=unigram,
                                                                               bigram_word_1=bigram_word_1, bigram_word_2=bigram_word_2,
                                                                               trigram_word_1=trigram_word_1, trigram_word_2=trigram_word_2, trigram_word_3=trigram_word_3,
                                                                               positive=False)


def count_selected_ngrams(bow_sentences):

    ngrams_selected = 0
    for bs in bow_sentences:
        ngrams_selected = ngrams_selected + len(bs)

    return ngrams_selected


def percentage_of_negated_ngrams_by_document_size(bow_sentences):

    _count = 0
    _doc_words_count = 0
    for bs in bow_sentences:
        for ngram in bs:
            if pre.is_bigram(ngram) and ngram.word_1.word in pre.NEGATION_WORDS or \
                    pre.is_trigram(ngram) and ngram.word_1.word in pre.NEGATION_WORDS:
                _doc_words_count = ngram.word_1.doc_word_count
                _count += 1

    return _count / float(_doc_words_count)


""" ------------------------------ Features functions ------------------------------ """


def positive_adjectives_count(bow_sentences):
    return {'value': count_of_unigrams_scores(
            bow_sentences, unigram=ADJS, positive=True), 'name': 'positive_adjectives_count'}


def negative_adjectives_count(bow_sentences):
    return {'value': count_of_unigrams_scores(
            bow_sentences, unigram=ADJS, positive=False), 'name': 'negative_adjectives_count'}


def positive_adverbs_count(bow_sentences):
    return {'value': count_of_unigrams_scores(
            bow_sentences, unigram=ADVS, positive=True), 'name': 'positive_adverbs_count'}


def negative_adverbs_count(bow_sentences):
    return {'value': count_of_unigrams_scores(
            bow_sentences, unigram=ADVS, positive=False), 'name': 'negative_adverbs_count'}


def positive_verbs_count(bow_sentences):
    return {'value': count_of_unigrams_scores(
            bow_sentences, unigram=VERBS, positive=True), 'name': 'positive_verbs_count'}


def negative_verbs_count(bow_sentences):
    return {'value': count_of_unigrams_scores(
            bow_sentences, unigram=VERBS, positive=False), 'name': 'positive_verbs_count'}


def positive_to_negative_ratio_of_adjectives_count(bow_sentences):
    return {'value': positive_to_negative_ratio_count_unigrams_scores(
            bow_sentences, unigram=ADJS), 'name': 'positive_to_negative_ratio_of_adjectives_count'}


def positive_to_negative_ratio_of_adverbs_count(bow_sentences):
    return {'value': positive_to_negative_ratio_count_unigrams_scores(
            bow_sentences, unigram=ADVS), 'name': 'positive_to_negative_ratio_of_adverbs_count'}


def positive_to_negative_ratio_of_verbs_count(bow_sentences):
    return {'value': positive_to_negative_ratio_count_unigrams_scores(
            bow_sentences, unigram=VERBS), 'name': 'positive_to_negative_ratio_of_verbs_count'}


def positive_adjectives_count_and_bigrams_with_adjectives(bow_sentences):
    return {'value': count_of_unigrams_and_bigrams_scores(
            bow_sentences, unigram=ADJS, bigram_word_1=ADVS, bigram_word_2=ADJS, positive=True), 'name': 'positive_adjectives_count_and_bigrams_with_adjectives'}


def negative_adjectives_count_and_bigrams_with_adjectives(bow_sentences):
    return {'value': count_of_unigrams_and_bigrams_scores(
            bow_sentences, unigram=ADJS, bigram_word_1=ADVS, bigram_word_2=ADJS, positive=False), 'name': 'negative_adjectives_count_and_bigrams_with_adjectives'}


def positive_adverbs_count_and_bigrams_with_adverbs(bow_sentences):
    return {'value': count_of_unigrams_and_bigrams_scores(
            bow_sentences, unigram=ADVS, bigram_word_1=ADVS, bigram_word_2=ADVS, positive=True), 'name': 'positive_adverbs_count_and_bigrams_with_adverbs'}


def negative_adverbs_count_and_bigrams_with_adverbs(bow_sentences):
    return {'value': count_of_unigrams_and_bigrams_scores(
            bow_sentences, unigram=ADVS, bigram_word_1=ADVS, bigram_word_2=ADVS, positive=False), 'name': 'negative_adverbs_count_and_bigrams_with_adverbs'}


def positive_verbs_count_and_bigrams_with_verbs(bow_sentences):
    return {'value': count_of_unigrams_and_bigrams_scores(
            bow_sentences, unigram=VERBS, bigram_word_1=ADVS, bigram_word_2=VERBS, positive=True), 'name': 'positive_verbs_count_and_bigrams_with_verbs'}


def negative_verbs_count_and_bigrams_with_verbs(bow_sentences):
    return {'value': count_of_unigrams_and_bigrams_scores(
            bow_sentences, unigram=VERBS, bigram_word_1=ADVS, bigram_word_2=VERBS, positive=False), 'name': 'negative_verbs_count_and_bigrams_with_verbs'}


def positive_unigrams_and_bigrams_count(bow_sentences):
    return {'value': count_of_unigrams_and_bigrams_scores(
            bow_sentences, unigram=ALL, bigram_word_1=ALL, bigram_word_2=ALL, positive=True), 'name': 'positive_unigrams_and_bigrams_count'}


def negative_unigrams_and_bigrams_count(bow_sentences):
    return {'value': count_of_unigrams_and_bigrams_scores(
            bow_sentences, unigram=ALL, bigram_word_1=ALL, bigram_word_2=ALL, positive=False), 'name': 'negative_unigrams_and_bigrams_count'}


def positive_unigrams_bigrams_and_trigrams_count(bow_sentences):
    return {'value': count_of_unigrams_bigrams_and_trigrams_scores(
            bow_sentences, unigram=ALL, bigram_word_1=ALL, bigram_word_2=ALL, positive=True,
            trigram_word_1=ALL, trigram_word_2=ALL, trigram_word_3=ALL), 'name': 'positive_unigrams_bigrams_and_trigrams_count'}


def negative_unigrams_bigrams_and_trigrams_count(bow_sentences):
    return {'value': count_of_unigrams_bigrams_and_trigrams_scores(
            bow_sentences, unigram=ALL, bigram_word_1=ALL, bigram_word_2=ALL, positive=False,
            trigram_word_1=ALL, trigram_word_2=ALL, trigram_word_3=ALL), 'name': 'negative_unigrams_bigrams_and_trigrams_count'}


def positive_to_negative_ratio_of_adjectives_count_and_bigrams_with_adjectives(bow_sentences):
    return {'value': positive_to_negative_ratio_count_unigrams_and_bigrams_scores(
            bow_sentences, unigram=ADJS, bigram_word_1=ADVS, bigram_word_2=ADJS), 'name': 'positive_to_negative_ratio_of_adjectives_count_and_bigrams_with_adjectives'}


def positive_to_negative_ratio_of_adverbs_count_and_bigrams_with_adverbs(bow_sentences):
    return {'value': positive_to_negative_ratio_count_unigrams_and_bigrams_scores(
            bow_sentences, unigram=ADVS, bigram_word_1=ADVS, bigram_word_2=ADVS), 'name': 'positive_to_negative_ratio_of_adverbs_count_and_bigrams_with_adverbs'}


def positive_to_negative_ratio_of_verbs_count_and_bigrams_with_verbs(bow_sentences):
    return {'value': positive_to_negative_ratio_count_unigrams_and_bigrams_scores(
            bow_sentences, unigram=VERBS, bigram_word_1=ADVS, bigram_word_2=VERBS), 'name': 'positive_to_negative_ratio_of_verbs_count_and_bigrams_with_verbs'}


def positive_to_negative_ratio_of_unigrams_and_bigrams_count(bow_sentences):
    return {'value': positive_to_negative_ratio_count_unigrams_and_bigrams_scores(
            bow_sentences, unigram=ALL, bigram_word_1=ALL, bigram_word_2=ALL), 'name': 'positive_to_negative_ratio_of_unigrams_and_bigrams_count'}


def positive_to_negative_ratio_of_unigrams_bigrams_and_trigrams_count(bow_sentences):
    return {'value': positive_to_negative_ratio_count_unigrams_bigrams_and_trigrams_scores(bow_sentences,
                                                                                           unigram=ALL,
                                                                                           bigram_word_1=ALL, bigram_word_2=ALL,
                                                                                           trigram_word_1=ALL, trigram_word_2=ALL, trigram_word_3=ALL),
            'name': 'positive_to_negative_ratio_of_unigrams_bigrams_and_trigrams_count'}


def selected_ngrams_count(bow_sentences):
    return {'value': count_selected_ngrams(bow_sentences), 'name': 'selected_ngrams_count'}


def all(bow_sentences,
        unigrams_only=True,
        unigrams_only_ratio=True,
        unigram_type=ALL,
        non_general_unigrams_and_bigrams=True,
        non_general_unigrams_and_bigrams_ratio=True,
        non_general_bigram_type=ALL_NON_GENERAL_BIGRAMS,
        ngrams_count=True,
        general_unigrams_and_bigrams=True,
        general_unigrams_and_bigrams_ratio=True,
        unigrams_and_bigrams_trigram=True,
        unigrams_and_bigrams_trigram_ratio=True):

    features_list = []
    if unigrams_only:
        if unigram_type == ADJS:
            features_list.append(positive_adjectives_count(bow_sentences))
            features_list.append(negative_adjectives_count(bow_sentences))
        elif unigram_type == ADJS_AND_ADVS:
            features_list.append(positive_adjectives_count(bow_sentences))
            features_list.append(negative_adjectives_count(bow_sentences))
            features_list.append(positive_adverbs_count(bow_sentences))
            features_list.append(negative_adverbs_count(bow_sentences))
        elif unigram_type == ADJS_AND_VERBS:
            features_list.append(positive_adjectives_count(bow_sentences))
            features_list.append(negative_adjectives_count(bow_sentences))
            features_list.append(positive_verbs_count(bow_sentences))
            features_list.append(negative_verbs_count(bow_sentences))
        elif unigram_type == ADVS_AND_VERBS:
            features_list.append(positive_adverbs_count(bow_sentences))
            features_list.append(negative_adverbs_count(bow_sentences))
            features_list.append(positive_verbs_count(bow_sentences))
            features_list.append(negative_verbs_count(bow_sentences))
        elif unigram_type == ADVS:
            features_list.append(positive_adverbs_count(bow_sentences))
            features_list.append(negative_adverbs_count(bow_sentences))
        elif unigram_type == VERBS:
            features_list.append(positive_verbs_count(bow_sentences))
            features_list.append(negative_verbs_count(bow_sentences))
        else:
            features_list.append(positive_adjectives_count(bow_sentences))
            features_list.append(negative_adjectives_count(bow_sentences))
            features_list.append(positive_adverbs_count(bow_sentences))
            features_list.append(negative_adverbs_count(bow_sentences))
            features_list.append(positive_verbs_count(bow_sentences))
            features_list.append(negative_verbs_count(bow_sentences))

    if unigrams_only_ratio:
        features_list.append(
            positive_to_negative_ratio_of_adjectives_count(bow_sentences))
        features_list.append(
            positive_to_negative_ratio_of_adverbs_count(bow_sentences))
        features_list.append(
            positive_to_negative_ratio_of_verbs_count(bow_sentences))

    if non_general_unigrams_and_bigrams:
        if non_general_bigram_type == ADVS_AND_BI_ADV_ADV:
            features_list.append(
                positive_adverbs_count_and_bigrams_with_adverbs(bow_sentences))
            features_list.append(
                negative_adverbs_count_and_bigrams_with_adverbs(bow_sentences))
        elif non_general_bigram_type == VERBS_AND_BI_ADV_VERB:
            features_list.append(
                positive_verbs_count_and_bigrams_with_verbs(bow_sentences))
            features_list.append(
                negative_verbs_count_and_bigrams_with_verbs(bow_sentences))
        elif non_general_bigram_type == ADJS_AND_BI_ADV_ADJ:
            features_list.append(
                positive_adjectives_count_and_bigrams_with_adjectives(bow_sentences))
            features_list.append(
                negative_adjectives_count_and_bigrams_with_adjectives(bow_sentences))
        else:
            features_list.append(
                positive_adverbs_count_and_bigrams_with_adverbs(bow_sentences))
            features_list.append(
                negative_adverbs_count_and_bigrams_with_adverbs(bow_sentences))
            features_list.append(
                positive_verbs_count_and_bigrams_with_verbs(bow_sentences))
            features_list.append(
                negative_verbs_count_and_bigrams_with_verbs(bow_sentences))
            features_list.append(
                positive_adjectives_count_and_bigrams_with_adjectives(bow_sentences))
            features_list.append(
                negative_adjectives_count_and_bigrams_with_adjectives(bow_sentences))

    if non_general_unigrams_and_bigrams_ratio:
        features_list.append(
            positive_to_negative_ratio_of_adjectives_count_and_bigrams_with_adjectives(bow_sentences))
        features_list.append(
            positive_to_negative_ratio_of_adverbs_count_and_bigrams_with_adverbs(bow_sentences))
        features_list.append(
            positive_to_negative_ratio_of_verbs_count_and_bigrams_with_verbs(bow_sentences))

    if ngrams_count:
        features_list.append(selected_ngrams_count(bow_sentences))

    if general_unigrams_and_bigrams:
        features_list.append(
            positive_unigrams_and_bigrams_count(bow_sentences))
        features_list.append(
            negative_unigrams_and_bigrams_count(bow_sentences))

    if general_unigrams_and_bigrams_ratio:
        features_list.append(
            positive_to_negative_ratio_of_unigrams_and_bigrams_count(bow_sentences))

    if unigrams_and_bigrams_trigram:
        features_list.append(
            positive_unigrams_bigrams_and_trigrams_count(bow_sentences))
        features_list.append(
            negative_unigrams_bigrams_and_trigrams_count(bow_sentences))

    if unigrams_and_bigrams_trigram_ratio:
        features_list.append(
            positive_to_negative_ratio_of_unigrams_bigrams_and_trigrams_count(bow_sentences))

    return features_list

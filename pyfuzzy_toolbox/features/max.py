from . import pre
from . import set_pos_tags_codes
from . import ADJS, ADVS, VERBS, ALL, ADJS_AND_ADVS, ADJS_AND_VERBS, ADVS_AND_VERBS, ALL_NON_GENERAL_BIGRAMS, ADVS_AND_BI_ADV_ADV, VERBS_AND_BI_ADV_VERB, ADJS_AND_BI_ADV_ADJ


""" ------------------------------ Base functions ------------------------------ """


def max_rule_score_for_unigrams(bow_sentences, unigram=ADJS):

    pos_tags_codes = set_pos_tags_codes(unigram)
    there_is_a_max_unigram = -1
    max_value = 0
    for bs in bow_sentences:
        for ngram in bs:
            if pre.is_unigram(ngram) and ngram.pos_tag in pos_tags_codes:
                if abs(ngram.polarity) > abs(max_value) and ngram.polarity < 0:
                    there_is_a_max_unigram = 0
                    max_value = ngram.polarity
                elif abs(ngram.polarity) > abs(max_value) and ngram.polarity > 0:
                    there_is_a_max_unigram = 1
                    max_value = ngram.polarity
    return {'sign': there_is_a_max_unigram, 'value': max_value}


def max_rule_score_for_bigrams(bow_sentences, bigram_word_1=ADVS, bigram_word_2=ADJS):

    pos_tags_codes_word_1 = set_pos_tags_codes(bigram_word_1)
    pos_tags_codes_word_2 = set_pos_tags_codes(bigram_word_2)
    there_is_a_max_bigram = -1
    max_value = 0
    for bs in bow_sentences:
        for ngram in bs:
            if pre.is_bigram(ngram) and ngram.word_1.pos_tag in pos_tags_codes_word_1 and ngram.word_2.pos_tag in pos_tags_codes_word_2:
                if abs(ngram.polarity) > abs(max_value) and ngram.polarity < 0:
                    there_is_a_max_bigram = 0
                    max_value = ngram.polarity
                elif abs(ngram.polarity) > abs(max_value) and ngram.polarity > 0:
                    there_is_a_max_bigram = 1
                    max_value = ngram.polarity
    return {'sign': there_is_a_max_bigram, 'value': max_value}


# UNTESTED
def max_rule_score_for_trigrams(bow_sentences, bigram_word_1=ADVS, bigram_word_2=ADVS, bigram_word_3=ADJS):

    pos_tags_codes_word_1 = set_pos_tags_codes(bigram_word_1)
    pos_tags_codes_word_2 = set_pos_tags_codes(bigram_word_2)
    pos_tags_codes_word_3 = set_pos_tags_codes(bigram_word_3)

    there_is_a_max_trigram = -1
    max_value = 0
    for bs in bow_sentences:
        for ngram in bs:
            if pre.is_trigram(ngram) and \
                    ngram.word_1.pos_tag in pos_tags_codes_word_1 and \
                    ngram.word_2.pos_tag in pos_tags_codes_word_2 and \
                    ngram.word_2.pos_tag in pos_tags_codes_word_3:
                if abs(ngram.polarity) > abs(max_value) and ngram.polarity < 0:
                    there_is_a_max_trigram = 0
                    max_value = ngram.polarity
                elif abs(ngram.polarity) > abs(max_value) and ngram.polarity > 0:
                    there_is_a_max_trigram = 1
                    max_value = ngram.polarity
    return {'sign': there_is_a_max_trigram, 'value': max_value}


def max_rule_score_for_unigrams_and_bigrams(bow_sentences, unigram=ADJS, bigram_word_1=ADVS, bigram_word_2=ADJS):

    unigram_sign_and_value = max_rule_score_for_unigrams(
        bow_sentences, unigram=unigram)
    bigram_sign_and_value = max_rule_score_for_bigrams(
        bow_sentences, bigram_word_1=bigram_word_1, bigram_word_2=bigram_word_2)

    if unigram_sign_and_value['sign'] == -1 and bigram_sign_and_value['sign'] == -1:
        return -1
    elif (unigram_sign_and_value['sign'] == 0 or unigram_sign_and_value['sign'] == 1) and bigram_sign_and_value['sign'] == -1:
        return unigram_sign_and_value['sign']
    elif (bigram_sign_and_value['sign'] == 0 or bigram_sign_and_value['sign'] == 1) and unigram_sign_and_value['sign'] == -1:
        return bigram_sign_and_value['sign']
    elif (bigram_sign_and_value['sign'] == 0 or bigram_sign_and_value['sign'] == 1) and \
            (unigram_sign_and_value['sign'] == 0 or unigram_sign_and_value['sign'] == 1):
        if abs(bigram_sign_and_value['value']) > abs(unigram_sign_and_value['value']):
            return bigram_sign_and_value['sign']
        else:
            return unigram_sign_and_value['sign']


""" ------------------------------ Features functions ------------------------------ """


def max_rule_for_adjective(bow_sentences):
    return {'value': max_rule_score_for_unigrams(bow_sentences, unigram=ADJS)['sign'], 'name': 'max_rule_for_adjective'}


def max_rule_for_adverbs(bow_sentences):
    return {'value': max_rule_score_for_unigrams(
            bow_sentences, unigram=ADVS)['sign'], 'name': 'max_rule_for_adverbs'}


def max_rule_for_verbs(bow_sentences):
    return {'value': max_rule_score_for_unigrams(
            bow_sentences, unigram=VERBS)['sign'], 'name': 'max_rule_for_verbs'}


def max_rule_for_adjective_and_bigrams_with_adjectives(bow_sentences):
    return {'value': max_rule_score_for_unigrams_and_bigrams(bow_sentences, unigram=ADJS, bigram_word_1=ADVS, bigram_word_2=ADJS), 'name': 'max_rule_for_adjective_and_bigrams_with_adjectives'}


def max_rule_for_adverbs_and_bigrams_with_adverbs(bow_sentences):
    return {'value': max_rule_score_for_unigrams_and_bigrams(bow_sentences, unigram=ADVS, bigram_word_1=ADVS, bigram_word_2=ADVS), 'name': 'max_rule_for_adverbs_and_bigrams_with_adverbs'}


def max_rule_for_verbs_and_bigrams_with_verbs(bow_sentences):
    return {'value': max_rule_score_for_unigrams_and_bigrams(bow_sentences, unigram=VERBS, bigram_word_1=ADVS, bigram_word_2=VERBS), 'name': 'max_rule_for_verbs_and_bigrams_with_verbs'}


def max_rule_for_unigrams_and_bigrams(bow_sentences):
    return {'value': max_rule_score_for_unigrams_and_bigrams(bow_sentences, unigram=ALL, bigram_word_1=ALL, bigram_word_2=ALL), 'name': 'max_rule_for_unigrams_and_bigrams'}


def max_rule_for_unigrams_bigrams_and_trigrams(bow_sentences):

    unigram_sign_and_value = max_rule_score_for_unigrams(
        bow_sentences, unigram=ALL)
    bigram_sign_and_value = max_rule_score_for_bigrams(
        bow_sentences, bigram_word_1=ALL, bigram_word_2=ALL)
    max_tri = max_rule_score_for_trigrams(
        bow_sentences, bigram_word_1=ALL, bigram_word_2=ALL, bigram_word_3=ALL)
    result = {
        'value': None, 'name': 'max_rule_for_unigrams_bigrams_and_trigrams'}

    print unigram_sign_and_value['sign'], bigram_sign_and_value['sign'], max_tri['sign']
    if unigram_sign_and_value['sign'] == -1 and bigram_sign_and_value['sign'] == -1 and max_tri['sign'] == -1:
        result['value'] = -1
    elif unigram_sign_and_value['sign'] != -1 and bigram_sign_and_value['sign'] == -1 and max_tri['sign'] == -1:
        result['value'] = unigram_sign_and_value['sign']
    elif unigram_sign_and_value['sign'] == -1 and bigram_sign_and_value['sign'] != -1 and max_tri['sign'] == -1:
        result['value'] = bigram_sign_and_value['sign']
    elif unigram_sign_and_value['sign'] == -1 and bigram_sign_and_value['sign'] == -1 and max_tri['sign'] != -1:
        result['value'] = max_tri['sign']
    elif unigram_sign_and_value['sign'] != -1 and bigram_sign_and_value['sign'] != -1 and max_tri['sign'] == -1:
    	if abs(unigram_sign_and_value['value']) > abs(bigram_sign_and_value['value']):
    		result['value'] = unigram_sign_and_value['sign']
    	else:
    		result['value'] = bigram_sign_and_value['sign']
    elif unigram_sign_and_value['sign'] != -1 and bigram_sign_and_value['sign'] == -1 and max_tri['sign'] != -1:
    	if abs(unigram_sign_and_value['value']) > abs(max_tri['value']):
    		result['value'] = unigram_sign_and_value['sign']
    	else:
    		result['value'] = max_tri['sign']
    elif unigram_sign_and_value['sign'] == -1 and bigram_sign_and_value['sign'] != -1 and max_tri['sign'] != -1:
    	if abs(bigram_sign_and_value['value']) > abs(max_tri['value']):
    		result['value'] = bigram_sign_and_value['sign']
    	else:
    		result['value'] = max_tri['sign']

    return result


def all(bow_sentences,
        unigrams=True,
        unigram_type=ALL,
        non_general_unigrams_and_bigrams=True,
        non_general_bigram_type=ALL_NON_GENERAL_BIGRAMS,
        general_unigrams_and_bigrams=True,
        unigrams_and_bigrams_trigram=True):

    features_list = []
    if unigrams:
        if unigram_type == ADJS:
            features_list.append(max_rule_for_adjective(bow_sentences))
        elif unigram_type == ADJS_AND_ADVS:
            features_list.append(max_rule_for_adjective(bow_sentences))
            features_list.append(max_rule_for_adverbs(bow_sentences))
        elif unigram_type == ADJS_AND_VERBS:
            features_list.append(max_rule_for_adjective(bow_sentences))
            features_list.append(max_rule_for_verbs(bow_sentences))
        elif unigram_type == ADVS_AND_VERBS:
            features_list.append(max_rule_for_adverbs(bow_sentences))
            features_list.append(max_rule_for_verbs(bow_sentences))
        elif unigram_type == ADVS:
            features_list.append(max_rule_for_adverbs(bow_sentences))
        elif unigram_type == VERBS:
            features_list.append(max_rule_for_verbs(bow_sentences))
        else:
            features_list.append(max_rule_for_verbs(bow_sentences))
            features_list.append(max_rule_for_adverbs(bow_sentences))
            features_list.append(max_rule_for_adjective(bow_sentences))

    if non_general_unigrams_and_bigrams:
        if non_general_bigram_type == ADVS_AND_BI_ADV_ADV:
            features_list.append(
                max_rule_for_adverbs_and_bigrams_with_adverbs(bow_sentences))
        elif non_general_bigram_type == VERBS_AND_BI_ADV_VERB:
            features_list.append(
                max_rule_for_verbs_and_bigrams_with_verbs(bow_sentences))
        elif non_general_bigram_type == ADJS_AND_BI_ADV_ADJ:
            features_list.append(
                max_rule_for_adjective_and_bigrams_with_adjectives(bow_sentences))
        else:
            features_list.append(
                max_rule_for_adverbs_and_bigrams_with_adverbs(bow_sentences))
            features_list.append(
                max_rule_for_verbs_and_bigrams_with_verbs(bow_sentences))
            features_list.append(
                max_rule_for_adjective_and_bigrams_with_adjectives(bow_sentences))

    if general_unigrams_and_bigrams:
        features_list.append(max_rule_for_unigrams_and_bigrams(bow_sentences))

    if unigrams_and_bigrams_trigram:
        features_list.append(
            max_rule_for_unigrams_bigrams_and_trigrams(bow_sentences))
    return features_list

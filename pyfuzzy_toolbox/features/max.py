from . import pre
from . import set_pos_tags_codes
from . import set_ngram_polarity_statement
from . import ADJS, ADVS, VERBS, ALL


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


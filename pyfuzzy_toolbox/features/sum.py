from . import pre
from . import set_pos_tags_codes
from . import set_ngram_polarity_statement
from . import ADJS, ADVS, VERBS, ALL

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
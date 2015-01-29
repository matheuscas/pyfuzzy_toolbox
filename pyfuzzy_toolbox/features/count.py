from . import pre
from . import set_pos_tags_codes
from . import set_ngram_polarity_statement
from . import ADJS, ADVS, VERBS, ALL

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
def count_of_trigrams_scores(bow_sentences, bigram_word_1=ADVS, bigram_word_2=ADVS, bigram_word_3=ADJS, positive=True):

	pos_tags_codes_word_1 = set_pos_tags_codes(bigram_word_1)
	pos_tags_codes_word_2 = set_pos_tags_codes(bigram_word_2)
	pos_tags_codes_word_3 = set_pos_tags_codes(bigram_word_3)

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

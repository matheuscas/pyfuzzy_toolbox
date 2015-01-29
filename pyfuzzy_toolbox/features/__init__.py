from .. import preprocessing as pre

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
	
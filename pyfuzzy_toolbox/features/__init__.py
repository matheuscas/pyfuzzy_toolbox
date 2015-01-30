from .. import preprocessing as pre

ADJS = 0
ADVS = 1
VERBS = 2
ALL = 3
ADJS_AND_ADVS = 4
ADJS_AND_VERBS = 5
ADVS_AND_VERBS = 6
ADJS_AND_BI_ADV_ADJ = 7
ADVS_AND_BI_ADV_ADV = 8
VERBS_AND_BI_ADV_VERB = 9
ALL_NON_GENERAL_BIGRAMS = 10


def set_pos_tags_codes(unigram_type=ADJS):

    pos_tags_codes = pre.POS_TAGS.ADJS

    if unigram_type == ADVS:
        pos_tags_codes = pre.POS_TAGS.ADVS
    elif unigram_type == VERBS:
        pos_tags_codes = pre.POS_TAGS.VERBS
    elif unigram_type == ADJS_AND_ADVS:
        pos_tags_codes = pre.POS_TAGS.ADJS + pre.POS_TAGS.ADVS
    elif unigram_type == ADJS_AND_VERBS:
        pos_tags_codes = pre.POS_TAGS.ADJS + pre.POS_TAGS.VERBS
    elif unigram_type == ADVS_AND_VERBS:
        pos_tags_codes = pre.POS_TAGS.ADVS + pre.POS_TAGS.VERBS
    elif unigram_type == ALL:
        pos_tags_codes = pre.POS_TAGS.ADJS + \
            pre.POS_TAGS.ADVS + pre.POS_TAGS.VERBS

    return pos_tags_codes


def set_ngram_polarity_statement(positive=True):

    polarity_eval_stm = 'ngram.polarity > 0'
    if not positive:
        polarity_eval_stm = 'ngram.polarity < 0'

    return polarity_eval_stm

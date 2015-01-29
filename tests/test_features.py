from pyfuzzy_toolbox import transformation as trans
from pyfuzzy_toolbox import preprocessing as pre
from pyfuzzy_toolbox import features as fts
import test_preprocessing as tpre
import nose


print 'Loading test text 1'
bow_sentences_1 = pre.start(tpre.text_1)
bow_sentences_1 = trans.start(bow_sentences_1)

print 'Loading test text 1a'
bow_sentences_1a = pre.start(tpre.text_1a)
bow_sentences_1a = trans.start(bow_sentences_1a)

print 'Loading test text 2a'
bow_sentences_2a = pre.start(tpre.text_2a)
bow_sentences_2a = trans.start(bow_sentences_2a)

max_adjective = -1
max_adjective_value = 0
max_adverb = -1
max_adverb_value = 0
max_verb = -1
max_verb_value = 0
for bs in bow_sentences_1a:
	for ngram in bs:
		if pre.is_unigram(ngram) and ngram.pos_tag in pre.POS_TAGS.ADJS:
			if abs(ngram.polarity) > abs(max_adjective_value):
				max_adjective_value = ngram.polarity
		elif pre.is_unigram(ngram) and ngram.pos_tag in pre.POS_TAGS.ADVS:
			if abs(ngram.polarity) > abs(max_adverb_value):
				max_adverb_value = ngram.polarity
		elif pre.is_unigram(ngram) and ngram.pos_tag in pre.POS_TAGS.VERBS:
			if abs(ngram.polarity) > abs(max_verb_value):
				max_verb_value = ngram.polarity

if max_adjective_value != 0:
	if max_adjective_value < 0:
		max_adjective = 0
	else:
		max_adjective = 1

if max_adverb_value != 0:
	if max_adverb_value < 0:
		max_adverb = 0
	else:
		max_adverb = 1

if max_verb_value != 0:
	if max_verb_value < 0:
		max_verb = 0
	else:
		max_verb = 1

print max_adjective, max_adjective_value
print max_adverb, max_adverb_value
print max_verb, max_verb_value

""" ----------------------------- SUM FEATURES ----------------------------- """

"""UNIGRAMS"""


def test_sum_of_positive_adjectives_scores():
    expected_sum = 0.0855961827957
    sum_of_positive_adjectives = fts.sum_of_unigrams_scores(bow_sentences_1)
    nose.tools.assert_almost_equal(expected_sum, sum_of_positive_adjectives)


def test_sum_of_positive_adverbs_scores():
    expected_sum = 0.0
    sum_of_positive_adverbs = fts.sum_of_unigrams_scores(
        bow_sentences_1, unigram=fts.ADVS)
    nose.tools.assert_almost_equal(expected_sum, sum_of_positive_adverbs)


def test_sum_of_positive_verbs_scores():
    expected_sum = 0.0261040860215
    sum_of_positive_verbs = fts.sum_of_unigrams_scores(
        bow_sentences_1, unigram=fts.VERBS)
    nose.tools.assert_almost_equal(expected_sum, sum_of_positive_verbs)


def test_sum_of_negative_adjectives_scores():
    expected_sum = -0.0644678504673
    sum_of_negative_adjectives = fts.sum_of_unigrams_scores(
        bow_sentences_1a, positive=False)
    nose.tools.assert_almost_equal(expected_sum, sum_of_negative_adjectives)


def test_sum_of_negative_adverbs_scores():
    expected_sum = -0.00891862928349
    sum_of_negative_adverbs = fts.sum_of_unigrams_scores(
        bow_sentences_1a, unigram=fts.ADVS, positive=False)
    nose.tools.assert_almost_equal(expected_sum, sum_of_negative_adverbs)


def test_sum_of_negative_verbs_scores():
    expected_sum = 0.0
    sum_of_negative_verbs = fts.sum_of_unigrams_scores(
        bow_sentences_1a, unigram=fts.VERBS, positive=False)
    nose.tools.assert_almost_equal(expected_sum, sum_of_negative_verbs)


def test_sum_ratio_of_positive_adjectives_scores():
    expected_sum = 0.0004601945311596716
    sum_of_positive_adjectives = fts.sum_of_unigrams_scores(
        bow_sentences_1, ratio=True)
    nose.tools.assert_almost_equal(expected_sum, sum_of_positive_adjectives)


def test_sum_ratio_of_positive_adverbs_scores():
    expected_sum = 0.0
    sum_of_positive_adverbs = fts.sum_of_unigrams_scores(
        bow_sentences_1, unigram=fts.ADVS, ratio=True)
    nose.tools.assert_almost_equal(expected_sum, sum_of_positive_adverbs)


def test_sum_ratio_of_positive_verbs_scores():
    expected_sum = 0.000140344548503
    sum_of_positive_verbs = fts.sum_of_unigrams_scores(
        bow_sentences_1, unigram=fts.VERBS, ratio=True, positive=True)
    nose.tools.assert_almost_equal(expected_sum, sum_of_positive_verbs)


def test_sum_ratio_of_negative_adjectives_scores():
    expected_sum = -0.0008910665972944851
    sum_of_negative_adjectives = fts.sum_of_unigrams_scores(
        bow_sentences_1, ratio=True, positive=False)
    nose.tools.assert_almost_equal(expected_sum, sum_of_negative_adjectives)


def test_sum_ratio_of_negative_adverbs_scores():
    expected_sum = -2.7783891848875693e-05
    sum_of_negative_adverbs = fts.sum_of_unigrams_scores(
        bow_sentences_1a, unigram=fts.ADVS, ratio=True, positive=False)
    nose.tools.assert_almost_equal(expected_sum, sum_of_negative_adverbs)


def test_sum_ratio_of_negative_verbs_scores():
    expected_sum = -0.000179220719158
    sum_of_negative_verbs = fts.sum_of_unigrams_scores(
        bow_sentences_1, unigram=fts.VERBS, ratio=True, positive=False)
    nose.tools.assert_almost_equal(expected_sum, sum_of_negative_verbs)


def test_positive_to_negative_ratio_sum_scores_adjectives():
    expected_ratio_sum = (0.0855961827957 + (-0.165738387097))
    positive_to_negative_ratio = fts.positive_to_negative_ratio_sum_unigrams_scores(
        bow_sentences_1)
    nose.tools.assert_almost_equal(
        expected_ratio_sum, positive_to_negative_ratio)


def test_positive_to_negative_ratio_sum_scores_adverbs():
    expected_ratio_sum = (0.0105152647975 + (-0.00891862928349))
    positive_to_negative_ratio = fts.positive_to_negative_ratio_sum_unigrams_scores(
        bow_sentences_1a, unigram=fts.ADVS)
    nose.tools.assert_almost_equal(
        expected_ratio_sum, positive_to_negative_ratio)


def test_positive_to_negative_ratio_sum_scores_verbs():
    expected_ratio_sum = (0.0223977570093 + (0.0))
    positive_to_negative_ratio = fts.positive_to_negative_ratio_sum_unigrams_scores(
        bow_sentences_1a, unigram=fts.VERBS)
    nose.tools.assert_almost_equal(
        expected_ratio_sum, positive_to_negative_ratio)


"""BIGRAMS"""


def test_sum_of_positive_adjectives_scores_and_bigrams_with_adjectives():
    expected_sum = 0.0855961827957
    sum_of_positive_adjectives_and_bigrams_with_adjectives = fts.sum_of_unigrams_and_bigrams_scores(
        bow_sentences_1)
    nose.tools.assert_almost_equal(
        expected_sum, sum_of_positive_adjectives_and_bigrams_with_adjectives)


def test_sum_of_negative_adjectives_scores_and_bigrams_with_adjectives():
    expected_sum = -0.0644678504673 - 2.1756533645
    sum_of_negative_adjectives_and_bigrams_with_adjectives = fts.sum_of_unigrams_and_bigrams_scores(
        bow_sentences_1a, positive=False)
    nose.tools.assert_almost_equal(
        expected_sum, sum_of_negative_adjectives_and_bigrams_with_adjectives)


def test_sum_of_positive_adverbs_scores_and_bigrams_with_adverbs():
    expected_sum = 0.0
    sum_of_positive_adverbs_and_bigrams_with_adverbs = fts.sum_of_unigrams_and_bigrams_scores(
        bow_sentences_1, unigram=fts.ADVS, bigram_word_1=fts.ADVS, bigram_word_2=fts.ADVS)
    nose.tools.assert_almost_equal(
        expected_sum, sum_of_positive_adverbs_and_bigrams_with_adverbs)


def test_sum_of_negative_adverbs_scores_and_bigrams_with_adverbs():
    expected_sum = -0.00891862928349
    sum_of_negative_adverbs_and_bigrams_with_adverbs = fts.sum_of_unigrams_and_bigrams_scores(
        bow_sentences_1a, unigram=fts.ADVS, bigram_word_1=fts.ADVS, bigram_word_2=fts.ADVS, positive=False)
    nose.tools.assert_almost_equal(
        expected_sum, sum_of_negative_adverbs_and_bigrams_with_adverbs)


def test_sum_of_positive_verbs_scores_and_bigrams_with_verbs():
    expected_sum = 0.0261040860215 + 0.683493333333
    sum_of_positive_verbs_and_bigrams_with_verbs = fts.sum_of_unigrams_and_bigrams_scores(
        bow_sentences_1, unigram=fts.VERBS, bigram_word_1=fts.ADVS, bigram_word_2=fts.VERBS)
    nose.tools.assert_almost_equal(
        expected_sum, sum_of_positive_verbs_and_bigrams_with_verbs)


def test_sum_of_negative_verbs_scores_and_bigrams_with_verbs():
    expected_sum = -0.0333350537634
    sum_of_negative_verbs_and_bigrams_with_verbs = fts.sum_of_unigrams_and_bigrams_scores(
        bow_sentences_1, unigram=fts.VERBS, bigram_word_1=fts.ADVS, bigram_word_2=fts.VERBS, positive=False)
    nose.tools.assert_almost_equal(
        expected_sum, sum_of_negative_verbs_and_bigrams_with_verbs)


def test_sum_ratio_of_positive_adjectives_scores_and_bigrams_with_adjectives():
    expected_sum = 0.0855961827957 / 186
    sum_of_positive_adjectives_and_bigrams_with_adjectives = fts.sum_of_unigrams_and_bigrams_scores(
        bow_sentences_1, ratio=True)
    nose.tools.assert_almost_equal(
        expected_sum, sum_of_positive_adjectives_and_bigrams_with_adjectives)


def test_sum_ratio_of_negative_adjectives_scores_and_bigrams_with_adjectives():
    expected_sum = (-0.0644678504673 - 2.1756533645) / 321
    sum_of_negative_adjectives_and_bigrams_with_adjectives = fts.sum_of_unigrams_and_bigrams_scores(
        bow_sentences_1a, positive=False, ratio=True)
    nose.tools.assert_almost_equal(
        expected_sum, sum_of_negative_adjectives_and_bigrams_with_adjectives)


def test_sum_ratio_of_positive_adverbs_scores_and_bigrams_with_adverbs():
    expected_sum = 0.0
    sum_of_positive_adverbs_and_bigrams_with_adverbs = fts.sum_of_unigrams_and_bigrams_scores(
        bow_sentences_1, unigram=fts.ADVS, bigram_word_1=fts.ADVS, bigram_word_2=fts.ADVS, ratio=True)
    nose.tools.assert_almost_equal(
        expected_sum, sum_of_positive_adverbs_and_bigrams_with_adverbs)


def test_sum_ratio_of_negative_adverbs_scores_and_bigrams_with_adverbs():
    expected_sum = -0.00891862928349 / 321
    sum_of_negative_adverbs_and_bigrams_with_adverbs = fts.sum_of_unigrams_and_bigrams_scores(
        bow_sentences_1a, unigram=fts.ADVS, bigram_word_1=fts.ADVS, bigram_word_2=fts.ADVS, positive=False, ratio=True)
    nose.tools.assert_almost_equal(
        expected_sum, sum_of_negative_adverbs_and_bigrams_with_adverbs)


def test_sum_ratio_of_positive_verbs_scores_and_bigrams_with_verbs():
    expected_sum = (0.0261040860215 + 0.683493333333) / 186
    sum_of_positive_verbs_and_bigrams_with_verbs = fts.sum_of_unigrams_and_bigrams_scores(
        bow_sentences_1, unigram=fts.VERBS, bigram_word_1=fts.ADVS, bigram_word_2=fts.VERBS, ratio=True)
    nose.tools.assert_almost_equal(
        expected_sum, sum_of_positive_verbs_and_bigrams_with_verbs)


def test_sum_ratio_of_negative_verbs_scores_and_bigrams_with_verbs():
    expected_sum = -0.0333350537634 / 186
    sum_of_negative_verbs_and_bigrams_with_verbs = fts.sum_of_unigrams_and_bigrams_scores(
        bow_sentences_1, unigram=fts.VERBS, bigram_word_1=fts.ADVS, bigram_word_2=fts.VERBS, positive=False, ratio=True)
    nose.tools.assert_almost_equal(
        expected_sum, sum_of_negative_verbs_and_bigrams_with_verbs)


def test_positive_to_negative_ratio_sum_scores_adjectives_and_bigrams_with_adjectives():
    expected_ratio_sum = 0.0855961827957 - 0.165738387097
    positive_to_negative_ratio_sum = fts.positive_to_negative_ratio_sum_unigrams_and_bigrams_scores(
        bow_sentences_1)
    nose.tools.assert_almost_equal(
        expected_ratio_sum, positive_to_negative_ratio_sum)


def test_positive_to_negative_ratio_sum_scores_adverbs_and_bigrams_with_adverbs():
    expected_ratio_sum = 0.0
    positive_to_negative_ratio_sum = fts.positive_to_negative_ratio_sum_unigrams_and_bigrams_scores(
        bow_sentences_1, unigram=fts.ADVS, bigram_word_1=fts.ADVS, bigram_word_2=fts.ADVS)
    nose.tools.assert_almost_equal(
        expected_ratio_sum, positive_to_negative_ratio_sum)


def test_positive_to_negative_ratio_sum_scores_verbs_and_bigrams_with_verbs():
    expected_ratio_sum = 0.6762623655913979
    positive_to_negative_ratio_sum = fts.positive_to_negative_ratio_sum_unigrams_and_bigrams_scores(
        bow_sentences_1, unigram=fts.VERBS, bigram_word_1=fts.ADVS, bigram_word_2=fts.VERBS)
    nose.tools.assert_almost_equal(
        expected_ratio_sum, positive_to_negative_ratio_sum)


""" ----------------------------- COUNT FEATURES ----------------------------- """

"""UNIGRAMS"""


def test_positive_scores_adjectives_count():
    expected_count = fts.count_of_unigrams_scores(
        bow_sentences_1a, unigram=fts.ADJS, positive=True)
    assert expected_count == 16


def test_negative_scores_adjectives_count():
    expected_count = fts.count_of_unigrams_scores(
        bow_sentences_1a, unigram=fts.ADJS, positive=False)
    assert expected_count == 4


def test_positive_scores_adverbs_count():
    expected_count = fts.count_of_unigrams_scores(
        bow_sentences_1a, unigram=fts.ADVS, positive=True)
    assert expected_count == 1


def test_negative_scores_adverbs_count():
    expected_count = fts.count_of_unigrams_scores(
        bow_sentences_1a, unigram=fts.ADVS, positive=False)
    assert expected_count == 2


def test_positive_scores_verbs_count():
    expected_count = fts.count_of_unigrams_scores(
        bow_sentences_1a, unigram=fts.VERBS, positive=True)
    assert expected_count == 5


def test_negative_scores_verbs_count():
    expected_count = fts.count_of_unigrams_scores(
        bow_sentences_1a, unigram=fts.VERBS, positive=False)
    assert expected_count == 0


def test_positive_to_negative_scores_ratio_of_adjectives_count():
    expected_count = fts.positive_to_negative_ratio_count_unigrams_scores(
        bow_sentences_1a, unigram=fts.ADJS)
    assert expected_count == (16 - 4)


def test_positive_to_negative_scores_ratio_of_adverbs_count():
    expected_count = fts.positive_to_negative_ratio_count_unigrams_scores(
        bow_sentences_1a, unigram=fts.ADVS)
    assert expected_count == (1 - 2)


def test_positive_to_negative_scores_ratio_of_verbs_count():
    expected_count = fts.positive_to_negative_ratio_count_unigrams_scores(
        bow_sentences_1a, unigram=fts.VERBS)
    assert expected_count == (5 - 0)


"""BIGRAMS"""


def test_positive_scores_adjectives_count_and_bigrams_with_adjectives():
    expected_count = fts.count_of_unigrams_and_bigrams_scores(
        bow_sentences_1a, unigram=fts.ADJS, bigram_word_1=fts.ADVS, bigram_word_2=fts.ADJS, positive=True)
    assert expected_count == (16 + 1)


def test_negative_scores_adjectives_count_and_bigrams_with_adjectives():
    expected_count = fts.count_of_unigrams_and_bigrams_scores(
        bow_sentences_1a, unigram=fts.ADJS, bigram_word_1=fts.ADVS, bigram_word_2=fts.ADJS, positive=False)
    assert expected_count == (4 + 3)


def test_positive_scores_adverbs_count_and_bigrams_with_adverbs():
    expected_count = fts.count_of_unigrams_and_bigrams_scores(
        bow_sentences_1a, unigram=fts.ADVS, bigram_word_1=fts.ADVS, bigram_word_2=fts.ADVS, positive=True)
    assert expected_count == (1 + 0)


def test_negative_scores_adverbs_count_and_bigrams_with_adverbs():
    expected_count = fts.count_of_unigrams_and_bigrams_scores(
        bow_sentences_1a, unigram=fts.ADVS, bigram_word_1=fts.ADVS, bigram_word_2=fts.ADVS, positive=False)
    assert expected_count == (2 + 0)


def test_positive_scores_verbs_count_and_bigrams_with_verbs():
    expected_count = fts.count_of_unigrams_and_bigrams_scores(
        bow_sentences_1a, unigram=fts.VERBS, bigram_word_1=fts.ADVS, bigram_word_2=fts.VERBS, positive=True)
    assert expected_count == (5 + 1)


def test_negative_scores_verbs_count_and_bigrams_with_verbs():
    expected_count = fts.count_of_unigrams_and_bigrams_scores(
        bow_sentences_1a, unigram=fts.VERBS, bigram_word_1=fts.ADVS, bigram_word_2=fts.VERBS, positive=False)
    assert expected_count == (0 + 0)


def test_positive_to_negative_scores_ratio_of_adjectives_count_and_bigrams_with_adjectives():
    expected_count = fts.positive_to_negative_ratio_count_unigrams_and_bigrams_scores(bow_sentences_1a, unigram=fts.ADJS, bigram_word_1=fts.ADVS, bigram_word_2=fts.ADJS)
    assert expected_count == (16 + 1) - (4 + 3)


def test_positive_to_negative_scores_ratio_of_adverbs_count_and_bigrams_with_adverbs():
    expected_count = fts.positive_to_negative_ratio_count_unigrams_and_bigrams_scores(bow_sentences_1a, unigram=fts.ADVS, bigram_word_1=fts.ADVS, bigram_word_2=fts.ADVS)
    assert expected_count == (1 + 0) - (2 + 0)


def test_positive_to_negative_scores_ratio_of_verbs_count_and_bigrams_with_verbs():
    expected_count = fts.positive_to_negative_ratio_count_unigrams_and_bigrams_scores(bow_sentences_1a, unigram=fts.VERBS, bigram_word_1=fts.ADVS, bigram_word_2=fts.VERBS)
    assert expected_count == (5 + 1) - (0 + 0)


def test_count_selected_ngrams():
	assert fts.count_selected_ngrams(bow_sentences_1) == 17
	assert fts.count_selected_ngrams(bow_sentences_1a) == 33
	assert fts.count_selected_ngrams(bow_sentences_2a) == 13

""" ----------------------------- MAX FEATURES ----------------------------- """

"""UNIGRAMS"""


def test_max_rule_score_for_adjective():
	assert fts.max_rule_score_for_adjective(bow_sentences_1a, unigram=fts.ADJS) == 0


def test_max_rule_score_for_adverbs():
	assert fts.max_rule_score_for_adjective(bow_sentences_1a, unigram=fts.ADVS) == 1


def test_max_rule_score_for_verbs():
	assert fts.max_rule_score_for_adjective(bow_sentences_1a, unigram=fts.VERBS) == 1

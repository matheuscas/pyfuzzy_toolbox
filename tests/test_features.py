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

print 'Loading test text 2b'
bow_sentences_2b = pre.start(tpre.text_2b)
bow_sentences_2b = trans.start(bow_sentences_2b)


_sum = 0
size = 0
for bs in bow_sentences_2b:
	for ngram in bs:
		if pre.is_trigram(ngram):
			print ngram, ngram.polarity

"""UNIGRAMS"""


def test_sum_of_positive_adjectives_scores():
	expected_sum = 0.0855961827957
	sum_of_positive_adjectives = fts.sum_of_unigrams_scores(bow_sentences_1)
	nose.tools.assert_almost_equal(expected_sum, sum_of_positive_adjectives)


def test_sum_of_positive_adverbs_scores():
	expected_sum = 0.0
	sum_of_positive_adverbs = fts.sum_of_unigrams_scores(bow_sentences_1, unigram=fts.ADVS)
	nose.tools.assert_almost_equal(expected_sum, sum_of_positive_adverbs)


def test_sum_of_positive_verbs_scores():
	expected_sum = 0.0261040860215
	sum_of_positive_verbs = fts.sum_of_unigrams_scores(bow_sentences_1, unigram=fts.VERBS)
	nose.tools.assert_almost_equal(expected_sum, sum_of_positive_verbs)


def test_sum_of_negative_adjectives_scores():
	expected_sum = -0.0644678504673
	sum_of_negative_adjectives = fts.sum_of_unigrams_scores(bow_sentences_1a, positive=False)
	nose.tools.assert_almost_equal(expected_sum, sum_of_negative_adjectives)


def test_sum_of_negative_adverbs_scores():
	expected_sum = -0.00891862928349
	sum_of_negative_adverbs = fts.sum_of_unigrams_scores(bow_sentences_1a, unigram=fts.ADVS, positive=False)
	nose.tools.assert_almost_equal(expected_sum, sum_of_negative_adverbs)


def test_sum_of_negative_verbs_scores():
	expected_sum = 0.0
	sum_of_negative_verbs = fts.sum_of_unigrams_scores(bow_sentences_1a, unigram=fts.VERBS, positive=False)
	nose.tools.assert_almost_equal(expected_sum, sum_of_negative_verbs)


def test_sum_ratio_of_positive_adjectives_scores():
	expected_sum = 0.0004601945311596716
	sum_of_positive_adjectives = fts.sum_of_unigrams_scores(bow_sentences_1, ratio=True)
	nose.tools.assert_almost_equal(expected_sum, sum_of_positive_adjectives)


def test_sum_ratio_of_positive_adverbs_scores():
	expected_sum = 0.0
	sum_of_positive_adverbs = fts.sum_of_unigrams_scores(bow_sentences_1, unigram=fts.ADVS, ratio=True)
	nose.tools.assert_almost_equal(expected_sum, sum_of_positive_adverbs)


def test_sum_ratio_of_positive_verbs_scores():
	expected_sum = 0.000140344548503
	sum_of_positive_verbs = fts.sum_of_unigrams_scores(bow_sentences_1, unigram=fts.VERBS, ratio=True, positive=True)
	nose.tools.assert_almost_equal(expected_sum, sum_of_positive_verbs)


def test_sum_ratio_of_negative_adjectives_scores():
	expected_sum = -0.0008910665972944851
	sum_of_negative_adjectives = fts.sum_of_unigrams_scores(bow_sentences_1, ratio=True, positive=False)
	nose.tools.assert_almost_equal(expected_sum, sum_of_negative_adjectives)


def test_sum_ratio_of_negative_adverbs_scores():
	expected_sum = -2.7783891848875693e-05
	sum_of_negative_adverbs = fts.sum_of_unigrams_scores(bow_sentences_1a, unigram=fts.ADVS, ratio=True, positive=False)
	nose.tools.assert_almost_equal(expected_sum, sum_of_negative_adverbs)


def test_sum_ratio_of_negative_verbs_scores():
	expected_sum = -0.000179220719158
	sum_of_negative_verbs = fts.sum_of_unigrams_scores(bow_sentences_1, unigram=fts.VERBS, ratio=True, positive=False)
	nose.tools.assert_almost_equal(expected_sum, sum_of_negative_verbs)


def test_positive_to_negative_ratio_sum_scores_adjectives():
	expected_ratio_sum = (0.0855961827957 + (-0.165738387097))
	positive_to_negative_ratio = fts.positive_to_negative_ratio_sum_unigrams_scores(bow_sentences_1)
	nose.tools.assert_almost_equal(expected_ratio_sum, positive_to_negative_ratio)


def test_positive_to_negative_ratio_sum_scores_adverbs():
	expected_ratio_sum = (0.0105152647975 + (-0.00891862928349))
	positive_to_negative_ratio = fts.positive_to_negative_ratio_sum_unigrams_scores(bow_sentences_1a, unigram=fts.ADVS)
	nose.tools.assert_almost_equal(expected_ratio_sum, positive_to_negative_ratio)


def test_positive_to_negative_ratio_sum_scores_verbs():
	expected_ratio_sum = (0.0223977570093 + (0.0))
	positive_to_negative_ratio = fts.positive_to_negative_ratio_sum_unigrams_scores(bow_sentences_1a, unigram=fts.VERBS)
	nose.tools.assert_almost_equal(expected_ratio_sum, positive_to_negative_ratio)


"""BIGRAMS"""


def test_sum_of_positive_adjectives_scores_and_bigrams_with_adjectives():
	expected_sum = 0.0855961827957
	sum_of_positive_adjectives_and_bigrams_with_adjectives = fts.sum_of_unigrams_and_bigrams_scores(bow_sentences_1)
	nose.tools.assert_almost_equal(expected_sum, sum_of_positive_adjectives_and_bigrams_with_adjectives)


def test_sum_of_negative_adjectives_scores_and_bigrams_with_adjectives():
	expected_sum = -0.0644678504673 - 2.1756533645
	sum_of_negative_adjectives_and_bigrams_with_adjectives = fts.sum_of_unigrams_and_bigrams_scores(bow_sentences_1a, positive=False)
	nose.tools.assert_almost_equal(expected_sum, sum_of_negative_adjectives_and_bigrams_with_adjectives)


def test_sum_of_positive_adverbs_scores_and_bigrams_with_adverbs():
	expected_sum = 0.0
	sum_of_positive_adverbs_and_bigrams_with_adverbs = fts.sum_of_unigrams_and_bigrams_scores(bow_sentences_1, unigram=fts.ADVS, bigram_word_1=fts.ADVS, bigram_word_2=fts.ADVS)
	nose.tools.assert_almost_equal(expected_sum, sum_of_positive_adverbs_and_bigrams_with_adverbs)


def test_sum_of_negative_adverbs_scores_and_bigrams_with_adverbs():
	expected_sum = -0.00891862928349
	sum_of_negative_adverbs_and_bigrams_with_adverbs = fts.sum_of_unigrams_and_bigrams_scores(bow_sentences_1a, unigram=fts.ADVS, bigram_word_1=fts.ADVS, bigram_word_2=fts.ADVS, positive=False)
	nose.tools.assert_almost_equal(expected_sum, sum_of_negative_adverbs_and_bigrams_with_adverbs)


def test_sum_of_positive_verbs_scores_and_bigrams_with_verbs():
	expected_sum = 0.0261040860215 + 0.683493333333
	sum_of_positive_verbs_and_bigrams_with_verbs = fts.sum_of_unigrams_and_bigrams_scores(bow_sentences_1, unigram=fts.VERBS, bigram_word_1=fts.ADVS, bigram_word_2=fts.VERBS)
	nose.tools.assert_almost_equal(expected_sum, sum_of_positive_verbs_and_bigrams_with_verbs)


def test_sum_of_negative_verbs_scores_and_bigrams_with_verbs():
	expected_sum = -0.0333350537634
	sum_of_negative_verbs_and_bigrams_with_verbs = fts.sum_of_unigrams_and_bigrams_scores(bow_sentences_1, unigram=fts.VERBS, bigram_word_1=fts.ADVS, bigram_word_2=fts.VERBS, positive=False)
	nose.tools.assert_almost_equal(expected_sum, sum_of_negative_verbs_and_bigrams_with_verbs)


def test_sum_ratio_of_positive_adjectives_scores_and_bigrams_with_adjectives():
	expected_sum = 0.0855961827957 / 186
	sum_of_positive_adjectives_and_bigrams_with_adjectives = fts.sum_of_unigrams_and_bigrams_scores(bow_sentences_1, ratio=True)
	nose.tools.assert_almost_equal(expected_sum, sum_of_positive_adjectives_and_bigrams_with_adjectives)


def test_sum_ratio_of_negative_adjectives_scores_and_bigrams_with_adjectives():
	expected_sum = (-0.0644678504673 - 2.1756533645) / 321
	sum_of_negative_adjectives_and_bigrams_with_adjectives = fts.sum_of_unigrams_and_bigrams_scores(bow_sentences_1a, positive=False, ratio=True)
	nose.tools.assert_almost_equal(expected_sum, sum_of_negative_adjectives_and_bigrams_with_adjectives)


def test_sum_ratio_of_positive_adverbs_scores_and_bigrams_with_adverbs():
	expected_sum = 0.0
	sum_of_positive_adverbs_and_bigrams_with_adverbs = fts.sum_of_unigrams_and_bigrams_scores(bow_sentences_1, unigram=fts.ADVS, bigram_word_1=fts.ADVS, bigram_word_2=fts.ADVS, ratio=True)
	nose.tools.assert_almost_equal(expected_sum, sum_of_positive_adverbs_and_bigrams_with_adverbs)


def test_sum_ratio_of_negative_adverbs_scores_and_bigrams_with_adverbs():
	expected_sum = -0.00891862928349 / 321
	sum_of_negative_adverbs_and_bigrams_with_adverbs = fts.sum_of_unigrams_and_bigrams_scores(bow_sentences_1a, unigram=fts.ADVS, bigram_word_1=fts.ADVS, bigram_word_2=fts.ADVS, positive=False, ratio=True)
	nose.tools.assert_almost_equal(expected_sum, sum_of_negative_adverbs_and_bigrams_with_adverbs)


def test_sum_ratio_of_positive_verbs_scores_and_bigrams_with_verbs():
	expected_sum = (0.0261040860215 + 0.683493333333) / 186
	sum_of_positive_verbs_and_bigrams_with_verbs = fts.sum_of_unigrams_and_bigrams_scores(bow_sentences_1, unigram=fts.VERBS, bigram_word_1=fts.ADVS, bigram_word_2=fts.VERBS, ratio=True)
	nose.tools.assert_almost_equal(expected_sum, sum_of_positive_verbs_and_bigrams_with_verbs)


def test_sum_ratio_of_negative_verbs_scores_and_bigrams_with_verbs():
	expected_sum = -0.0333350537634 / 186
	sum_of_negative_verbs_and_bigrams_with_verbs = fts.sum_of_unigrams_and_bigrams_scores(bow_sentences_1, unigram=fts.VERBS, bigram_word_1=fts.ADVS, bigram_word_2=fts.VERBS, positive=False, ratio=True)
	nose.tools.assert_almost_equal(expected_sum, sum_of_negative_verbs_and_bigrams_with_verbs)


def test_positive_to_negative_ratio_sum_scores_adjectives_and_bigrams_with_adjectives():
	expected_ratio_sum = 0.0855961827957 - 0.165738387097
	positive_to_negative_ratio_sum = fts.positive_to_negative_ratio_sum_unigrams_and_bigrams_scores(bow_sentences_1)
	nose.tools.assert_almost_equal(expected_ratio_sum, positive_to_negative_ratio_sum)


def test_positive_to_negative_ratio_sum_scores_adverbs_and_bigrams_with_adverbs():
	expected_ratio_sum = 0.0
	positive_to_negative_ratio_sum = fts.positive_to_negative_ratio_sum_unigrams_and_bigrams_scores(bow_sentences_1, unigram=fts.ADVS, bigram_word_1=fts.ADVS, bigram_word_2=fts.ADVS)
	nose.tools.assert_almost_equal(expected_ratio_sum, positive_to_negative_ratio_sum)


def test_positive_to_negative_ratio_sum_scores_verbs_and_bigrams_with_verbs():
	expected_ratio_sum = 0.6762623655913979
	positive_to_negative_ratio_sum = fts.positive_to_negative_ratio_sum_unigrams_and_bigrams_scores(bow_sentences_1, unigram=fts.VERBS, bigram_word_1=fts.ADVS, bigram_word_2=fts.VERBS)
	nose.tools.assert_almost_equal(expected_ratio_sum, positive_to_negative_ratio_sum)

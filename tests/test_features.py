from pyfuzzy_toolbox import transformation as trans
from pyfuzzy_toolbox import preprocessing as pre
from pyfuzzy_toolbox import intensifiers as ints
from pyfuzzy_toolbox import features as fts
import test_preprocessing as tpre
import nose


print 'Loading test text 1'
bow_sentences_1 = pre.start(tpre.text_1)
bow_sentences_1 = trans.start(bow_sentences_1)

print 'Loading test text 1a'
bow_sentences_1a = pre.start(tpre.text_1a)
bow_sentences_1a = trans.start(bow_sentences_1a)


_sum = 0
size = 0
for bs in bow_sentences_1:
	for ngram in bs:
		print ngram, ngram.polarity
		if pre.is_unigram(ngram) and ngram.pos_tag in pre.POS_TAGS.ADVS and ngram.polarity < 0:
			_sum = _sum + ngram.polarity
			size = ngram.doc_word_count

print 'text 1:', _sum

_sum = 0
for bs in bow_sentences_1a:
	for ngram in bs:
		print ngram, ngram.polarity
		if pre.is_unigram(ngram) and ngram.pos_tag in pre.POS_TAGS.VERBS and ngram.polarity < 0:
			_sum = _sum + ngram.polarity

print 'text 1a:', _sum


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

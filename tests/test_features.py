from pyfuzzy_toolbox import transformation as trans
from pyfuzzy_toolbox import preprocessing as pre
from pyfuzzy_toolbox.features.count import *
from pyfuzzy_toolbox.features.max import *
from pyfuzzy_toolbox.features.sum import *
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


""" ----------------------------- SUM FEATURES ----------------------------- """

"""UNIGRAMS"""


def test_sum_of_positive_adjectives_scores():
    expected_sum = 0.0855961827957
    sum_of_positive_adjectives = sum_of_unigrams_scores(bow_sentences_1)
    nose.tools.assert_almost_equal(expected_sum, sum_of_positive_adjectives)


def test_sum_of_positive_adverbs_scores():
    expected_sum = 0.0
    sum_of_positive_adverbs = sum_of_unigrams_scores(
        bow_sentences_1, unigram=ADVS)
    nose.tools.assert_almost_equal(expected_sum, sum_of_positive_adverbs)


def test_sum_of_positive_verbs_scores():
    expected_sum = 0.0261040860215
    sum_of_positive_verbs = sum_of_unigrams_scores(
        bow_sentences_1, unigram=VERBS)
    nose.tools.assert_almost_equal(expected_sum, sum_of_positive_verbs)


def test_sum_of_negative_adjectives_scores():
    expected_sum = -0.0644678504673
    sum_of_negative_adjectives = sum_of_unigrams_scores(
        bow_sentences_1a, positive=False)
    nose.tools.assert_almost_equal(expected_sum, sum_of_negative_adjectives)


def test_sum_of_negative_adverbs_scores():
    expected_sum = -0.00891862928349
    sum_of_negative_adverbs = sum_of_unigrams_scores(
        bow_sentences_1a, unigram=ADVS, positive=False)
    nose.tools.assert_almost_equal(expected_sum, sum_of_negative_adverbs)


def test_sum_of_negative_verbs_scores():
    expected_sum = 0.0
    sum_of_negative_verbs = sum_of_unigrams_scores(
        bow_sentences_1a, unigram=VERBS, positive=False)
    nose.tools.assert_almost_equal(expected_sum, sum_of_negative_verbs)


def test_sum_ratio_of_positive_adjectives_scores():
    expected_sum = 0.0004601945311596716
    sum_of_positive_adjectives = sum_of_unigrams_scores(
        bow_sentences_1, ratio=True)
    nose.tools.assert_almost_equal(expected_sum, sum_of_positive_adjectives)


def test_sum_ratio_of_positive_adverbs_scores():
    expected_sum = 0.0
    sum_of_positive_adverbs = sum_of_unigrams_scores(
        bow_sentences_1, unigram=ADVS, ratio=True)
    nose.tools.assert_almost_equal(expected_sum, sum_of_positive_adverbs)


def test_sum_ratio_of_positive_verbs_scores():
    expected_sum = 0.000140344548503
    sum_of_positive_verbs = sum_of_unigrams_scores(
        bow_sentences_1, unigram=VERBS, ratio=True, positive=True)
    nose.tools.assert_almost_equal(expected_sum, sum_of_positive_verbs)


def test_sum_ratio_of_negative_adjectives_scores():
    expected_sum = -0.0008910665972944851
    sum_of_negative_adjectives = sum_of_unigrams_scores(
        bow_sentences_1, ratio=True, positive=False)
    nose.tools.assert_almost_equal(expected_sum, sum_of_negative_adjectives)


def test_sum_ratio_of_negative_adverbs_scores():
    expected_sum = -2.7783891848875693e-05
    sum_of_negative_adverbs = sum_of_unigrams_scores(
        bow_sentences_1a, unigram=ADVS, ratio=True, positive=False)
    nose.tools.assert_almost_equal(expected_sum, sum_of_negative_adverbs)


def test_sum_ratio_of_negative_verbs_scores():
    expected_sum = -0.000179220719158
    sum_of_negative_verbs = sum_of_unigrams_scores(
        bow_sentences_1, unigram=VERBS, ratio=True, positive=False)
    nose.tools.assert_almost_equal(expected_sum, sum_of_negative_verbs)


def test_positive_to_negative_ratio_sum_scores_adjectives():
    expected_ratio_sum = (0.0855961827957 + (-0.165738387097))
    positive_to_negative_ratio = positive_to_negative_ratio_sum_unigrams_scores(
        bow_sentences_1)
    nose.tools.assert_almost_equal(
        expected_ratio_sum, positive_to_negative_ratio)


def test_positive_to_negative_ratio_sum_scores_adverbs():
    expected_ratio_sum = (0.0105152647975 + (-0.00891862928349))
    positive_to_negative_ratio = positive_to_negative_ratio_sum_unigrams_scores(
        bow_sentences_1a, unigram=ADVS)
    nose.tools.assert_almost_equal(
        expected_ratio_sum, positive_to_negative_ratio)


def test_positive_to_negative_ratio_sum_scores_verbs():
    expected_ratio_sum = (0.0223977570093 + (0.0))
    positive_to_negative_ratio = positive_to_negative_ratio_sum_unigrams_scores(
        bow_sentences_1a, unigram=VERBS)
    nose.tools.assert_almost_equal(
        expected_ratio_sum, positive_to_negative_ratio)


"""BIGRAMS"""


def test_sum_of_positive_adjectives_scores_and_bigrams_with_adjectives():
    expected_sum = 0.0855961827957
    sum_of_positive_adjectives_and_bigrams_with_adjectives = sum_of_unigrams_and_bigrams_scores(
        bow_sentences_1)
    nose.tools.assert_almost_equal(
        expected_sum, sum_of_positive_adjectives_and_bigrams_with_adjectives)


def test_sum_of_negative_adjectives_scores_and_bigrams_with_adjectives():
    expected_sum = -0.0644678504673 - 2.1756533645
    sum_of_negative_adjectives_and_bigrams_with_adjectives = sum_of_unigrams_and_bigrams_scores(
        bow_sentences_1a, positive=False)
    nose.tools.assert_almost_equal(
        expected_sum, sum_of_negative_adjectives_and_bigrams_with_adjectives)


def test_sum_of_positive_adverbs_scores_and_bigrams_with_adverbs():
    expected_sum = 0.0
    sum_of_positive_adverbs_and_bigrams_with_adverbs = sum_of_unigrams_and_bigrams_scores(
        bow_sentences_1, unigram=ADVS, bigram_word_1=ADVS, bigram_word_2=ADVS)
    nose.tools.assert_almost_equal(
        expected_sum, sum_of_positive_adverbs_and_bigrams_with_adverbs)


def test_sum_of_negative_adverbs_scores_and_bigrams_with_adverbs():
    expected_sum = -0.00891862928349
    sum_of_negative_adverbs_and_bigrams_with_adverbs = sum_of_unigrams_and_bigrams_scores(
        bow_sentences_1a, unigram=ADVS, bigram_word_1=ADVS, bigram_word_2=ADVS, positive=False)
    nose.tools.assert_almost_equal(
        expected_sum, sum_of_negative_adverbs_and_bigrams_with_adverbs)


def test_sum_of_positive_verbs_scores_and_bigrams_with_verbs():
    expected_sum = 0.0261040860215 + 0.683493333333
    sum_of_positive_verbs_and_bigrams_with_verbs = sum_of_unigrams_and_bigrams_scores(
        bow_sentences_1, unigram=VERBS, bigram_word_1=ADVS, bigram_word_2=VERBS)
    nose.tools.assert_almost_equal(
        expected_sum, sum_of_positive_verbs_and_bigrams_with_verbs)


def test_sum_of_negative_verbs_scores_and_bigrams_with_verbs():
    expected_sum = -0.0333350537634
    sum_of_negative_verbs_and_bigrams_with_verbs = sum_of_unigrams_and_bigrams_scores(
        bow_sentences_1, unigram=VERBS, bigram_word_1=ADVS, bigram_word_2=VERBS, positive=False)
    nose.tools.assert_almost_equal(
        expected_sum, sum_of_negative_verbs_and_bigrams_with_verbs)


def test_sum_ratio_of_positive_adjectives_scores_and_bigrams_with_adjectives():
    expected_sum = 0.0855961827957 / 186
    sum_of_positive_adjectives_and_bigrams_with_adjectives = sum_of_unigrams_and_bigrams_scores(
        bow_sentences_1, ratio=True)
    nose.tools.assert_almost_equal(
        expected_sum, sum_of_positive_adjectives_and_bigrams_with_adjectives)


def test_sum_ratio_of_negative_adjectives_scores_and_bigrams_with_adjectives():
    expected_sum = (-0.0644678504673 - 2.1756533645) / 321
    sum_of_negative_adjectives_and_bigrams_with_adjectives = sum_of_unigrams_and_bigrams_scores(
        bow_sentences_1a, positive=False, ratio=True)
    nose.tools.assert_almost_equal(
        expected_sum, sum_of_negative_adjectives_and_bigrams_with_adjectives)


def test_sum_ratio_of_positive_adverbs_scores_and_bigrams_with_adverbs():
    expected_sum = 0.0
    sum_of_positive_adverbs_and_bigrams_with_adverbs = sum_of_unigrams_and_bigrams_scores(
        bow_sentences_1, unigram=ADVS, bigram_word_1=ADVS, bigram_word_2=ADVS, ratio=True)
    nose.tools.assert_almost_equal(
        expected_sum, sum_of_positive_adverbs_and_bigrams_with_adverbs)


def test_sum_ratio_of_negative_adverbs_scores_and_bigrams_with_adverbs():
    expected_sum = -0.00891862928349 / 321
    sum_of_negative_adverbs_and_bigrams_with_adverbs = sum_of_unigrams_and_bigrams_scores(
        bow_sentences_1a, unigram=ADVS, bigram_word_1=ADVS, bigram_word_2=ADVS, positive=False, ratio=True)
    nose.tools.assert_almost_equal(
        expected_sum, sum_of_negative_adverbs_and_bigrams_with_adverbs)


def test_sum_ratio_of_positive_verbs_scores_and_bigrams_with_verbs():
    expected_sum = (0.0261040860215 + 0.683493333333) / 186
    sum_of_positive_verbs_and_bigrams_with_verbs = sum_of_unigrams_and_bigrams_scores(
        bow_sentences_1, unigram=VERBS, bigram_word_1=ADVS, bigram_word_2=VERBS, ratio=True)
    nose.tools.assert_almost_equal(
        expected_sum, sum_of_positive_verbs_and_bigrams_with_verbs)


def test_sum_ratio_of_negative_verbs_scores_and_bigrams_with_verbs():
    expected_sum = -0.0333350537634 / 186
    sum_of_negative_verbs_and_bigrams_with_verbs = sum_of_unigrams_and_bigrams_scores(
        bow_sentences_1, unigram=VERBS, bigram_word_1=ADVS, bigram_word_2=VERBS, positive=False, ratio=True)
    nose.tools.assert_almost_equal(
        expected_sum, sum_of_negative_verbs_and_bigrams_with_verbs)


def test_positive_to_negative_ratio_sum_scores_adjectives_and_bigrams_with_adjectives():
    expected_ratio_sum = 0.0855961827957 - 0.165738387097
    positive_to_negative_ratio_sum = positive_to_negative_ratio_sum_unigrams_and_bigrams_scores(
        bow_sentences_1)
    nose.tools.assert_almost_equal(
        expected_ratio_sum, positive_to_negative_ratio_sum)


def test_positive_to_negative_ratio_sum_scores_adverbs_and_bigrams_with_adverbs():
    expected_ratio_sum = 0.0
    positive_to_negative_ratio_sum = positive_to_negative_ratio_sum_unigrams_and_bigrams_scores(
        bow_sentences_1, unigram=ADVS, bigram_word_1=ADVS, bigram_word_2=ADVS)
    nose.tools.assert_almost_equal(
        expected_ratio_sum, positive_to_negative_ratio_sum)


def test_positive_to_negative_ratio_sum_scores_verbs_and_bigrams_with_verbs():
    expected_ratio_sum = 0.6762623655913979
    positive_to_negative_ratio_sum = positive_to_negative_ratio_sum_unigrams_and_bigrams_scores(
        bow_sentences_1, unigram=VERBS, bigram_word_1=ADVS, bigram_word_2=VERBS)
    nose.tools.assert_almost_equal(
        expected_ratio_sum, positive_to_negative_ratio_sum)


""" ----------------------------- COUNT FEATURES ----------------------------- """

"""UNIGRAMS"""


def test_positive_scores_adjectives_count():
    expected_count = count_of_unigrams_scores(
        bow_sentences_1a, unigram=ADJS, positive=True)
    assert expected_count == 16


def test_negative_scores_adjectives_count():
    expected_count = count_of_unigrams_scores(
        bow_sentences_1a, unigram=ADJS, positive=False)
    assert expected_count == 4


def test_positive_scores_adverbs_count():
    expected_count = count_of_unigrams_scores(
        bow_sentences_1a, unigram=ADVS, positive=True)
    assert expected_count == 1


def test_negative_scores_adverbs_count():
    expected_count = count_of_unigrams_scores(
        bow_sentences_1a, unigram=ADVS, positive=False)
    assert expected_count == 2


def test_positive_scores_verbs_count():
    expected_count = count_of_unigrams_scores(
        bow_sentences_1a, unigram=VERBS, positive=True)
    assert expected_count == 5


def test_negative_scores_verbs_count():
    expected_count = count_of_unigrams_scores(
        bow_sentences_1a, unigram=VERBS, positive=False)
    assert expected_count == 0


def test_positive_to_negative_scores_ratio_of_adjectives_count():
    expected_count = positive_to_negative_ratio_count_unigrams_scores(
        bow_sentences_1a, unigram=ADJS)
    assert expected_count == (16 - 4)


def test_positive_to_negative_scores_ratio_of_adverbs_count():
    expected_count = positive_to_negative_ratio_count_unigrams_scores(
        bow_sentences_1a, unigram=ADVS)
    assert expected_count == (1 - 2)


def test_positive_to_negative_scores_ratio_of_verbs_count():
    expected_count = positive_to_negative_ratio_count_unigrams_scores(
        bow_sentences_1a, unigram=VERBS)
    assert expected_count == (5 - 0)


"""BIGRAMS"""


def test_positive_scores_adjectives_count_and_bigrams_with_adjectives():
    expected_count = count_of_unigrams_and_bigrams_scores(
        bow_sentences_1a, unigram=ADJS, bigram_word_1=ADVS, bigram_word_2=ADJS, positive=True)
    assert expected_count == (16 + 1)


def test_negative_scores_adjectives_count_and_bigrams_with_adjectives():
    expected_count = count_of_unigrams_and_bigrams_scores(
        bow_sentences_1a, unigram=ADJS, bigram_word_1=ADVS, bigram_word_2=ADJS, positive=False)
    assert expected_count == (4 + 3)


def test_positive_scores_adverbs_count_and_bigrams_with_adverbs():
    expected_count = count_of_unigrams_and_bigrams_scores(
        bow_sentences_1a, unigram=ADVS, bigram_word_1=ADVS, bigram_word_2=ADVS, positive=True)
    assert expected_count == (1 + 0)


def test_negative_scores_adverbs_count_and_bigrams_with_adverbs():
    expected_count = count_of_unigrams_and_bigrams_scores(
        bow_sentences_1a, unigram=ADVS, bigram_word_1=ADVS, bigram_word_2=ADVS, positive=False)
    assert expected_count == (2 + 0)


def test_positive_scores_verbs_count_and_bigrams_with_verbs():
    expected_count = count_of_unigrams_and_bigrams_scores(
        bow_sentences_1a, unigram=VERBS, bigram_word_1=ADVS, bigram_word_2=VERBS, positive=True)
    assert expected_count == (5 + 1)


def test_negative_scores_verbs_count_and_bigrams_with_verbs():
    expected_count = count_of_unigrams_and_bigrams_scores(
        bow_sentences_1a, unigram=VERBS, bigram_word_1=ADVS, bigram_word_2=VERBS, positive=False)
    assert expected_count == (0 + 0)


def test_positive_to_negative_scores_ratio_of_adjectives_count_and_bigrams_with_adjectives():
    expected_count = positive_to_negative_ratio_count_unigrams_and_bigrams_scores(
        bow_sentences_1a, unigram=ADJS, bigram_word_1=ADVS, bigram_word_2=ADJS)
    assert expected_count == (16 + 1) - (4 + 3)


def test_positive_to_negative_scores_ratio_of_adverbs_count_and_bigrams_with_adverbs():
    expected_count = positive_to_negative_ratio_count_unigrams_and_bigrams_scores(
        bow_sentences_1a, unigram=ADVS, bigram_word_1=ADVS, bigram_word_2=ADVS)
    assert expected_count == (1 + 0) - (2 + 0)


def test_positive_to_negative_scores_ratio_of_verbs_count_and_bigrams_with_verbs():
    expected_count = positive_to_negative_ratio_count_unigrams_and_bigrams_scores(
        bow_sentences_1a, unigram=VERBS, bigram_word_1=ADVS, bigram_word_2=VERBS)
    assert expected_count == (5 + 1) - (0 + 0)


def test_count_selected_ngrams():
    assert count_selected_ngrams(bow_sentences_1) == 17
    assert count_selected_ngrams(bow_sentences_1a) == 33
    assert count_selected_ngrams(bow_sentences_2a) == 13

""" ----------------------------- MAX FEATURES ----------------------------- """

"""UNIGRAMS"""


def test_max_rule_score_for_adjective():
    assert max_rule_score_for_unigrams(
        bow_sentences_1a, unigram=ADJS)['sign'] == 0


def test_max_rule_score_for_adverbs():
    assert max_rule_score_for_unigrams(
        bow_sentences_1a, unigram=ADVS)['sign'] == 1


def test_max_rule_score_for_verbs():
    assert max_rule_score_for_unigrams(
        bow_sentences_1a, unigram=VERBS)['sign'] == 1


"""BIGRAMS"""


def test_max_rule_score_for_adjective_and_bigrams_with_adjectives():
    assert max_rule_score_for_unigrams_and_bigrams(bow_sentences_1a, unigram=ADJS, bigram_word_1=ADVS, bigram_word_2=ADJS) == 0


def test_max_rule_score_for_adverbs_and_bigrams_with_adverbs():
    assert max_rule_score_for_unigrams_and_bigrams(bow_sentences_1a, unigram=ADVS, bigram_word_1=ADVS, bigram_word_2=ADVS) == 1


def test_max_rule_score_for_verbs_and_bigrams_with_verbs():
    assert max_rule_score_for_unigrams_and_bigrams(bow_sentences_1a, unigram=VERBS, bigram_word_1=ADVS, bigram_word_2=VERBS) == 1


""" ----------------------------- PERCENTAGE FEATURES ----------------------------- """

def test_percentage_of_negated_ngrams_by_document_size():
	nose.tools.assert_almost_equal(0.00537634408602, percentage_of_negated_ngrams_by_document_size(bow_sentences_1))
	nose.tools.assert_almost_equal(0.0155763239875, percentage_of_negated_ngrams_by_document_size(bow_sentences_1a))
	nose.tools.assert_almost_equal(0.0127388535032, percentage_of_negated_ngrams_by_document_size(bow_sentences_2a))

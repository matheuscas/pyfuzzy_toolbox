from pyfuzzy_toolbox import transformation as trans
from pyfuzzy_toolbox import preprocessing as pre
import decimal
import nose

# expected prior polarity value for 'nice': 0.48759
positive_unigram = pre.Unigram()
positive_unigram.position = 14
positive_unigram.frequency = 2
positive_unigram.doc_word_count = 28
positive_unigram.word = 'nice'

# expected prior polarity value for 'poor': -0.3325
negative_unigram = pre.Unigram()
negative_unigram.position = 14
negative_unigram.frequency = 4
negative_unigram.doc_word_count = 28
negative_unigram.word = 'poor'

# really
really_intensifier_unigram = pre.Unigram()
really_intensifier_unigram.position = 13
really_intensifier_unigram.frequency = 1
really_intensifier_unigram.doc_word_count = 28
really_intensifier_unigram.word = 'really'

# extraordinarily
extraordinarily_intensifier_unigram = pre.Unigram()
extraordinarily_intensifier_unigram.position = 13
extraordinarily_intensifier_unigram.frequency = 1
extraordinarily_intensifier_unigram.doc_word_count = 28
extraordinarily_intensifier_unigram.word = 'extraordinarily'

# slightly
slightly_intensifier_unigram = pre.Unigram()
slightly_intensifier_unigram.position = 13
slightly_intensifier_unigram.frequency = 1
slightly_intensifier_unigram.doc_word_count = 28
slightly_intensifier_unigram.word = 'slightly'

bigram = pre.Bigram()


def test_get_unigram_polarity_position_true():
    # position calc: (polarity * position) / doc_word_count
    expected_polarity = 0.243795
    unigram_polarity = trans.get_unigram_polarity(positive_unigram,
                                                  lexicon=trans.SWN_PRIOR_POLARITY,
                                                  use_position=True,
                                                  use_frequency=False,
                                                  compensate_bias=False,
                                                  bias_compensation=0.5)
    assert expected_polarity == unigram_polarity

    expected_polarity = -0.16625
    unigram_polarity = trans.get_unigram_polarity(negative_unigram,
                                                  lexicon=trans.SWN_PRIOR_POLARITY,
                                                  use_position=True,
                                                  use_frequency=False,
                                                  compensate_bias=False,
                                                  bias_compensation=0.5)
    assert expected_polarity == unigram_polarity


def test_get_unigram_polarity_frequency_true():
    # frequency calc: polarity / frequency
    expected_polarity = 0.243795
    unigram_polarity = trans.get_unigram_polarity(positive_unigram,
                                                  lexicon=trans.SWN_PRIOR_POLARITY,
                                                  use_position=False,
                                                  use_frequency=True,
                                                  compensate_bias=False,
                                                  bias_compensation=0.5)
    assert expected_polarity == unigram_polarity

    expected_polarity = -0.083125
    unigram_polarity = trans.get_unigram_polarity(negative_unigram,
                                                  lexicon=trans.SWN_PRIOR_POLARITY,
                                                  use_position=False,
                                                  use_frequency=True,
                                                  compensate_bias=False,
                                                  bias_compensation=0.5)
    assert expected_polarity == unigram_polarity


def test_get_unigram_polarity_compensate_bias_true():
    expected_polarity = 0.48759
    unigram_polarity = trans.get_unigram_polarity(positive_unigram,
                                                  lexicon=trans.SWN_PRIOR_POLARITY,
                                                  use_position=False,
                                                  use_frequency=False,
                                                  compensate_bias=True,
                                                  bias_compensation=0.5)
    assert expected_polarity == unigram_polarity

    expected_polarity = -0.665
    unigram_polarity = trans.get_unigram_polarity(negative_unigram,
                                                  lexicon=trans.SWN_PRIOR_POLARITY,
                                                  use_position=False,
                                                  use_frequency=False,
                                                  compensate_bias=True,
                                                  bias_compensation=0.5)
    assert expected_polarity == unigram_polarity


def test_get_unigram_polarity_use_position_only_false():
    expected_polarity = 0.243795
    unigram_polarity = trans.get_unigram_polarity(positive_unigram,
                                                  lexicon=trans.SWN_PRIOR_POLARITY,
                                                  use_position=False,
                                                  use_frequency=True,
                                                  compensate_bias=True,
                                                  bias_compensation=0.5)
    assert expected_polarity == unigram_polarity

    expected_polarity = -0.16625
    unigram_polarity = trans.get_unigram_polarity(negative_unigram,
                                                  lexicon=trans.SWN_PRIOR_POLARITY,
                                                  use_position=False,
                                                  use_frequency=True,
                                                  compensate_bias=True,
                                                  bias_compensation=0.5)
    assert expected_polarity == unigram_polarity


def test_get_unigram_polarity_use_frequency_only_false():
    expected_polarity = 0.243795
    unigram_polarity = trans.get_unigram_polarity(positive_unigram,
                                                  lexicon=trans.SWN_PRIOR_POLARITY,
                                                  use_position=True,
                                                  use_frequency=False,
                                                  compensate_bias=True,
                                                  bias_compensation=0.5)
    assert expected_polarity == unigram_polarity

    expected_polarity = -0.3325
    unigram_polarity = trans.get_unigram_polarity(negative_unigram,
                                                  lexicon=trans.SWN_PRIOR_POLARITY,
                                                  use_position=True,
                                                  use_frequency=False,
                                                  compensate_bias=True,
                                                  bias_compensation=0.5)
    assert expected_polarity == unigram_polarity


def test_get_bigram_polarity_position_true():

    bigram.word_1 = really_intensifier_unigram
    bigram.word_2 = positive_unigram
    expected_polarity = 0.28036425
    unigram_polarity = trans.get_bigram_polarity(bigram,
                                                 lexicon=trans.SWN_PRIOR_POLARITY,
                                                 use_position=True,
                                                 use_frequency=False,
                                                 compensate_bias=False,
                                                 bias_compensation=0.5)
    nose.tools.assert_almost_equal(expected_polarity,unigram_polarity)

    bigram.word_1 = slightly_intensifier_unigram
    expected_polarity = 0.1218975
    unigram_polarity = trans.get_bigram_polarity(bigram,
                                                 lexicon=trans.SWN_PRIOR_POLARITY,
                                                 use_position=True,
                                                 use_frequency=False,
                                                 compensate_bias=False,
                                                 bias_compensation=0.5)

    nose.tools.assert_almost_equal(expected_polarity,unigram_polarity)

    bigram.word_1 = really_intensifier_unigram
    bigram.word_2 = negative_unigram
    expected_polarity = -0.1911875
    unigram_polarity = trans.get_bigram_polarity(bigram,
                                                 lexicon=trans.SWN_PRIOR_POLARITY,
                                                 use_position=True,
                                                 use_frequency=False,
                                                 compensate_bias=False,
                                                 bias_compensation=0.5)
    nose.tools.assert_almost_equal(expected_polarity,unigram_polarity)

    bigram.word_1 = slightly_intensifier_unigram
    expected_polarity = -0.083125
    unigram_polarity = trans.get_bigram_polarity(bigram,
                                                 lexicon=trans.SWN_PRIOR_POLARITY,
                                                 use_position=True,
                                                 use_frequency=False,
                                                 compensate_bias=False,
                                                 bias_compensation=0.5)

    nose.tools.assert_almost_equal(expected_polarity,unigram_polarity)


def test_get_bigram_polarity_frequency_true():

    bigram.word_1 = really_intensifier_unigram
    bigram.word_2 = positive_unigram
    expected_polarity = 0.28036425
    unigram_polarity = trans.get_bigram_polarity(bigram,
                                                 lexicon=trans.SWN_PRIOR_POLARITY,
                                                 use_position=False,
                                                 use_frequency=True,
                                                 compensate_bias=False,
                                                 bias_compensation=0.5)
    nose.tools.assert_almost_equal(expected_polarity,unigram_polarity)

    bigram.word_1 = slightly_intensifier_unigram
    expected_polarity = 0.1218975
    unigram_polarity = trans.get_bigram_polarity(bigram,
                                                 lexicon=trans.SWN_PRIOR_POLARITY,
                                                 use_position=False,
                                                 use_frequency=True,
                                                 compensate_bias=False,
                                                 bias_compensation=0.5)

    nose.tools.assert_almost_equal(expected_polarity,unigram_polarity)

    bigram.word_1 = really_intensifier_unigram
    bigram.word_2 = negative_unigram
    expected_polarity = -0.09559375
    unigram_polarity = trans.get_bigram_polarity(bigram,
                                                 lexicon=trans.SWN_PRIOR_POLARITY,
                                                 use_position=False,
                                                 use_frequency=True,
                                                 compensate_bias=False,
                                                 bias_compensation=0.5)
    nose.tools.assert_almost_equal(expected_polarity,unigram_polarity)

    bigram.word_1 = slightly_intensifier_unigram
    expected_polarity = -0.0415625
    unigram_polarity = trans.get_bigram_polarity(bigram,
                                                 lexicon=trans.SWN_PRIOR_POLARITY,
                                                 use_position=False,
                                                 use_frequency=True,
                                                 compensate_bias=False,
                                                 bias_compensation=0.5)

    nose.tools.assert_almost_equal(expected_polarity,unigram_polarity)


def test_get_bigram_polarity_compensate_bias_true():

    bigram.word_1 = really_intensifier_unigram
    bigram.word_2 = positive_unigram
    expected_polarity = 0.5607285
    unigram_polarity = trans.get_bigram_polarity(bigram,
                                                 lexicon=trans.SWN_PRIOR_POLARITY,
                                                 use_position=False,
                                                 use_frequency=False,
                                                 compensate_bias=True,
                                                 bias_compensation=0.5)
    nose.tools.assert_almost_equal(expected_polarity,unigram_polarity)

    bigram.word_1 = slightly_intensifier_unigram
    expected_polarity = 0.243795
    unigram_polarity = trans.get_bigram_polarity(bigram,
                                                 lexicon=trans.SWN_PRIOR_POLARITY,
                                                 use_position=False,
                                                 use_frequency=False,
                                                 compensate_bias=True,
                                                 bias_compensation=0.5)

    nose.tools.assert_almost_equal(expected_polarity,unigram_polarity)

    bigram.word_1 = really_intensifier_unigram
    bigram.word_2 = negative_unigram
    expected_polarity = -0.76475
    unigram_polarity = trans.get_bigram_polarity(bigram,
                                                 lexicon=trans.SWN_PRIOR_POLARITY,
                                                 use_position=False,
                                                 use_frequency=False,
                                                 compensate_bias=True,
                                                 bias_compensation=0.5)
    nose.tools.assert_almost_equal(expected_polarity,unigram_polarity)

    bigram.word_1 = slightly_intensifier_unigram
    expected_polarity = -0.3325
    unigram_polarity = trans.get_bigram_polarity(bigram,
                                                 lexicon=trans.SWN_PRIOR_POLARITY,
                                                 use_position=False,
                                                 use_frequency=False,
                                                 compensate_bias=True,
                                                 bias_compensation=0.5)

    nose.tools.assert_almost_equal(expected_polarity,unigram_polarity)
from pyfuzzy_toolbox import transformation as trans
from pyfuzzy_toolbox import preprocessing as pre
from pyfuzzy_toolbox import intensifiers as ints
import nose

# expected prior polarity value for 'nice': 0.48759
positive_unigram = pre.Unigram()
positive_unigram.position = 14
positive_unigram.frequency = 2
positive_unigram.doc_word_count = 28
positive_unigram.word = 'nice'
positive_unigram_polarity = 0.48759

# expected prior polarity value for 'poor': -0.3325
negative_unigram = pre.Unigram()
negative_unigram.position = 14
negative_unigram.frequency = 4
negative_unigram.doc_word_count = 28
negative_unigram.word = 'poor'
negative_unigram_polarity = -0.3325

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
    expected_polarity = (positive_unigram_polarity * positive_unigram.position) / positive_unigram.doc_word_count
    unigram_polarity = trans.get_unigram_polarity(positive_unigram,
                                                  lexicon=trans.SWN_PRIOR_POLARITY,
                                                  use_position=True,
                                                  use_frequency=False,
                                                  compensate_bias=False,
                                                  bias_compensation=0.5)
    assert expected_polarity == unigram_polarity

    expected_polarity = (negative_unigram_polarity * negative_unigram.position) / negative_unigram.doc_word_count
    unigram_polarity = trans.get_unigram_polarity(negative_unigram,
                                                  lexicon=trans.SWN_PRIOR_POLARITY,
                                                  use_position=True,
                                                  use_frequency=False,
                                                  compensate_bias=False,
                                                  bias_compensation=0.5)
    assert expected_polarity == unigram_polarity


def test_get_unigram_polarity_frequency_true():
    # frequency calc: polarity / frequency
    expected_polarity = positive_unigram_polarity / float(positive_unigram.frequency)
    unigram_polarity = trans.get_unigram_polarity(positive_unigram,
                                                  lexicon=trans.SWN_PRIOR_POLARITY,
                                                  use_position=False,
                                                  use_frequency=True,
                                                  compensate_bias=False,
                                                  bias_compensation=0.5)
    assert expected_polarity == unigram_polarity

    expected_polarity = negative_unigram_polarity / float(negative_unigram.frequency)
    unigram_polarity = trans.get_unigram_polarity(negative_unigram,
                                                  lexicon=trans.SWN_PRIOR_POLARITY,
                                                  use_position=False,
                                                  use_frequency=True,
                                                  compensate_bias=False,
                                                  bias_compensation=0.5)
    assert expected_polarity == unigram_polarity


def test_get_unigram_polarity_compensate_bias_true():
    expected_polarity = positive_unigram_polarity
    unigram_polarity = trans.get_unigram_polarity(positive_unigram,
                                                  lexicon=trans.SWN_PRIOR_POLARITY,
                                                  use_position=False,
                                                  use_frequency=False,
                                                  compensate_bias=True,
                                                  bias_compensation=0.5)
    assert expected_polarity == unigram_polarity

    expected_polarity = negative_unigram_polarity / 0.5
    unigram_polarity = trans.get_unigram_polarity(negative_unigram,
                                                  lexicon=trans.SWN_PRIOR_POLARITY,
                                                  use_position=False,
                                                  use_frequency=False,
                                                  compensate_bias=True,
                                                  bias_compensation=0.5)
    assert expected_polarity == unigram_polarity


def test_get_unigram_polarity_use_position_only_false():
    expected_polarity = positive_unigram_polarity / positive_unigram.frequency
    unigram_polarity = trans.get_unigram_polarity(positive_unigram,
                                                  lexicon=trans.SWN_PRIOR_POLARITY,
                                                  use_position=False,
                                                  use_frequency=True,
                                                  compensate_bias=True,
                                                  bias_compensation=0.5)
    assert expected_polarity == unigram_polarity

    expected_polarity = (negative_unigram_polarity / 0.5) / negative_unigram.frequency
    unigram_polarity = trans.get_unigram_polarity(negative_unigram,
                                                  lexicon=trans.SWN_PRIOR_POLARITY,
                                                  use_position=False,
                                                  use_frequency=True,
                                                  compensate_bias=True,
                                                  bias_compensation=0.5)
    assert expected_polarity == unigram_polarity


def test_get_unigram_polarity_use_frequency_only_false():
    expected_polarity = (positive_unigram_polarity * positive_unigram.position) / positive_unigram.doc_word_count
    unigram_polarity = trans.get_unigram_polarity(positive_unigram,
                                                  lexicon=trans.SWN_PRIOR_POLARITY,
                                                  use_position=True,
                                                  use_frequency=False,
                                                  compensate_bias=True,
                                                  bias_compensation=0.5)
    assert expected_polarity == unigram_polarity

    expected_polarity = ((negative_unigram_polarity * negative_unigram.position) / negative_unigram.doc_word_count) / 0.5
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
    expected_polarity = (positive_unigram_polarity * positive_unigram.position) / positive_unigram.doc_word_count
    expected_polarity = expected_polarity + (expected_polarity * ints.intensifiers.high.modifier)
    unigram_polarity = trans.get_bigram_polarity(bigram,
                                                 lexicon=trans.SWN_PRIOR_POLARITY,
                                                 use_position=True,
                                                 use_frequency=False,
                                                 compensate_bias=False,
                                                 bias_compensation=0.5)
    nose.tools.assert_almost_equal(expected_polarity,unigram_polarity)

    bigram.word_1 = slightly_intensifier_unigram
    expected_polarity = (positive_unigram_polarity * positive_unigram.position) / positive_unigram.doc_word_count
    expected_polarity = expected_polarity + (expected_polarity * ints.intensifiers.lowest.modifier)
    unigram_polarity = trans.get_bigram_polarity(bigram,
                                                 lexicon=trans.SWN_PRIOR_POLARITY,
                                                 use_position=True,
                                                 use_frequency=False,
                                                 compensate_bias=False,
                                                 bias_compensation=0.5)

    nose.tools.assert_almost_equal(expected_polarity,unigram_polarity)

    bigram.word_1 = really_intensifier_unigram
    bigram.word_2 = negative_unigram
    expected_polarity = (negative_unigram_polarity * negative_unigram.position) / negative_unigram.doc_word_count
    expected_polarity = expected_polarity + (expected_polarity * ints.intensifiers.high.modifier)
    unigram_polarity = trans.get_bigram_polarity(bigram,
                                                 lexicon=trans.SWN_PRIOR_POLARITY,
                                                 use_position=True,
                                                 use_frequency=False,
                                                 compensate_bias=False,
                                                 bias_compensation=0.5)
    nose.tools.assert_almost_equal(expected_polarity,unigram_polarity)

    bigram.word_1 = slightly_intensifier_unigram
    expected_polarity = (negative_unigram_polarity * negative_unigram.position) / negative_unigram.doc_word_count
    expected_polarity = expected_polarity + (expected_polarity * ints.intensifiers.lowest.modifier)
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
    expected_polarity = (positive_unigram_polarity / positive_unigram.frequency)
    expected_polarity = expected_polarity + (expected_polarity * ints.intensifiers.high.modifier)
    unigram_polarity = trans.get_bigram_polarity(bigram,
                                                 lexicon=trans.SWN_PRIOR_POLARITY,
                                                 use_position=False,
                                                 use_frequency=True,
                                                 compensate_bias=False,
                                                 bias_compensation=0.5)
    nose.tools.assert_almost_equal(expected_polarity,unigram_polarity)

    bigram.word_1 = slightly_intensifier_unigram
    expected_polarity = (positive_unigram_polarity / positive_unigram.frequency)
    expected_polarity = expected_polarity + (expected_polarity * ints.intensifiers.lowest.modifier)
    unigram_polarity = trans.get_bigram_polarity(bigram,
                                                 lexicon=trans.SWN_PRIOR_POLARITY,
                                                 use_position=False,
                                                 use_frequency=True,
                                                 compensate_bias=False,
                                                 bias_compensation=0.5)

    nose.tools.assert_almost_equal(expected_polarity,unigram_polarity)

    bigram.word_1 = really_intensifier_unigram
    bigram.word_2 = negative_unigram
    expected_polarity = (negative_unigram_polarity / negative_unigram.frequency)
    expected_polarity = expected_polarity + (expected_polarity * ints.intensifiers.high.modifier)
    unigram_polarity = trans.get_bigram_polarity(bigram,
                                                 lexicon=trans.SWN_PRIOR_POLARITY,
                                                 use_position=False,
                                                 use_frequency=True,
                                                 compensate_bias=False,
                                                 bias_compensation=0.5)
    nose.tools.assert_almost_equal(expected_polarity,unigram_polarity)

    bigram.word_1 = slightly_intensifier_unigram
    expected_polarity = (negative_unigram_polarity / negative_unigram.frequency)
    expected_polarity = expected_polarity + (expected_polarity * ints.intensifiers.lowest.modifier)
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
    expected_polarity = positive_unigram_polarity + (positive_unigram_polarity * ints.intensifiers.high.modifier)
    unigram_polarity = trans.get_bigram_polarity(bigram,
                                                 lexicon=trans.SWN_PRIOR_POLARITY,
                                                 use_position=False,
                                                 use_frequency=False,
                                                 compensate_bias=True,
                                                 bias_compensation=0.5)
    nose.tools.assert_almost_equal(expected_polarity,unigram_polarity)

    bigram.word_1 = slightly_intensifier_unigram
    expected_polarity = positive_unigram_polarity + (positive_unigram_polarity * ints.intensifiers.lowest.modifier)
    unigram_polarity = trans.get_bigram_polarity(bigram,
                                                 lexicon=trans.SWN_PRIOR_POLARITY,
                                                 use_position=False,
                                                 use_frequency=False,
                                                 compensate_bias=True,
                                                 bias_compensation=0.5)

    nose.tools.assert_almost_equal(expected_polarity,unigram_polarity)

    bigram.word_1 = really_intensifier_unigram
    bigram.word_2 = negative_unigram
    expected_polarity = negative_unigram_polarity + (negative_unigram_polarity * ints.intensifiers.high.modifier)
    expected_polarity = expected_polarity / 0.5
    unigram_polarity = trans.get_bigram_polarity(bigram,
                                                 lexicon=trans.SWN_PRIOR_POLARITY,
                                                 use_position=False,
                                                 use_frequency=False,
                                                 compensate_bias=True,
                                                 bias_compensation=0.5)
    nose.tools.assert_almost_equal(expected_polarity,unigram_polarity)

    bigram.word_1 = slightly_intensifier_unigram
    expected_polarity = negative_unigram_polarity + (negative_unigram_polarity * ints.intensifiers.lowest.modifier)
    expected_polarity = expected_polarity / 0.5
    unigram_polarity = trans.get_bigram_polarity(bigram,
                                                 lexicon=trans.SWN_PRIOR_POLARITY,
                                                 use_position=False,
                                                 use_frequency=False,
                                                 compensate_bias=True,
                                                 bias_compensation=0.5)

    nose.tools.assert_almost_equal(expected_polarity,unigram_polarity)

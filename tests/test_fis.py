from nose.tools import *
import numpy as np
from pyfuzzy_toolbox import fis


def test_fuzzySet_right_result_for_scalar_input():
	foo = fis.FuzzySet('foo',[2,4,6], np.array(range(11)))

	expected_result_1 = np.array([0])
	expected_result_2 = np.array([0])
	expected_result_3 = np.array([0.5])
	expected_result_4 = np.array([1])
	expected_result_5 = np.array([0.5])
	expected_result_6 = np.array([0])
	expected_result_7 = np.array([0])

	assert np.array_equal(foo.degree(1), expected_result_1) == True
	assert np.array_equal(foo.degree(2), expected_result_2) == True
	assert np.array_equal(foo.degree(3), expected_result_3) == True
	assert np.array_equal(foo.degree(4), expected_result_4) == True
	assert np.array_equal(foo.degree(5), expected_result_5) == True
	assert np.array_equal(foo.degree(6), expected_result_6) == True
	assert np.array_equal(foo.degree(7), expected_result_7) == True


def test_fuzzySet_right_result_for_array_input():
	foo = fis.FuzzySet('foo',[1,3,5], np.array(range(11)))
	expected_result_1 = np.array([0,0,0.5000,1.0000,0.5000,0,0,0,0,0,0])
	assert np.array_equal(foo.degree(np.array(range(11))), expected_result_1) == True

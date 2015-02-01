from nose.tools import *
import numpy as np
from pyfuzzy_toolbox import mf

"""Tests form trimf function"""


@raises(AssertionError)
def test_trimf_wrong_size_params():
    mf.trimf(3, [2, 2])


@raises(TypeError)
def test_trimf_wrong_x_type():
    mf.trimf('3', [2, 2, 4])


@raises(ValueError)
def test_trimf_a_cant_be_greater_than_b():
    mf.trimf(3, [2, 1, 4])


@raises(ValueError)
def test_trimf_b_cant_be_greater_than_c():
    mf.trimf(3, [2, 6, 5])


def test_trimf_right_result_for_scalar_input():
    expected_result_1 = np.array([0])
    expected_result_2 = np.array([0])
    expected_result_3 = np.array([0.5])
    expected_result_4 = np.array([1])
    expected_result_5 = np.array([0.5])
    expected_result_6 = np.array([0])
    expected_result_7 = np.array([0])

    assert np.array_equal(mf.trimf(1, [2, 4, 6]), expected_result_1) == True
    assert np.array_equal(mf.trimf(2, [2, 4, 6]), expected_result_2) == True
    assert np.array_equal(mf.trimf(3, [2, 4, 6]), expected_result_3) == True
    assert np.array_equal(mf.trimf(4, [2, 4, 6]), expected_result_4) == True
    assert np.array_equal(mf.trimf(5, [2, 4, 6]), expected_result_5) == True
    assert np.array_equal(mf.trimf(6, [2, 4, 6]), expected_result_6) == True
    assert np.array_equal(mf.trimf(7, [2, 4, 6]), expected_result_7) == True


def test_trimf_right_result_for_array_input():
    expected_result_1 = np.array(
        [0, 0, 0.5000, 1.0000, 0.5000, 0, 0, 0, 0, 0, 0])
    assert np.array_equal(
        mf.trimf(np.array(range(11)), [1, 3, 5]), expected_result_1) == True

"""Tests form centroid function"""
# @raises(TypeError)
# def test_wrong_defuzz_type():
# 	mf.defuzz([3],[],'mispelled centroid')


@raises(AssertionError)
def test_size_mismatch_between_x_and_mf():
    mf.centroid(np.zeros(3), np.zeros(2))


@raises(TypeError)
def test_wrong_mf_type():
    mf.centroid(True, [1, 2, 3, 4])


@raises(TypeError)
def test_wrong_x_type():
    mf.centroid([1, 2], np.zeros(2))


def test_centroid_right_result():
    expected_result_1 = 3
    expected_result_2 = 5.6667
    s_1 = mf.trimf(np.array(range(11)), [1, 3, 5])
    s_2 = mf.trimf(np.arange(0, 10.1, 0.1), [3, 6, 8])

    assert expected_result_1 == mf.centroid(np.array(range(11)), s_1)
    assert expected_result_2 == mf.centroid(np.arange(0, 10.1, 0.1), s_2)

from pyfuzzy_toolbox import wm
import numpy as np
from nose.tools import raises


@raises(TypeError)
def test_generate_regions_right_range_type():
    regions = wm.generate_regions(range(0, 1), 5)


@raises(TypeError)
def test_generate_regions_right_N_type():
    regions = wm.generate_regions(np.arange(0, 1.01, 0.01), 2.5)


def test_generate_regions_right_numbet_of_regions_for_N_0():
    N = 0
    _range = np.arange(0, 1.01, 0.01)
    regions = wm.generate_regions(_range, N)
    assert len(regions) == 1
    assert regions[0].params == [0, 0.5, 1]
    assert (regions[0].range == _range).all()


def test_generate_regions_right_numbet_of_regions_for_N_1():
    N = 1
    _range = np.arange(0, 1.01, 0.01)
    regions = wm.generate_regions(_range, N)
    assert len(regions) == 3
    assert regions[1].params == [0, 0.5, 1]
    assert regions[0].params == [0, 0, 0.5]
    assert regions[2].params == [0.5, 1, 1]


def test_generate_regions_right_numbet_of_regions_for_N_1_and_negative_range():
    N = 1
    _range = np.linspace(-1, 1, num=101)
    regions = wm.generate_regions(_range, N)
    assert len(regions) == 3
    assert (regions[1].params[1] - regions[1].params[0]
            ) == (regions[1].params[2] - regions[1].params[1])


def test_generate_regions_right_numbet_of_regions_for_N_2():
    N = 2
    _range = np.arange(0, 15.01, 0.01)
    regions = wm.generate_regions(_range, N)
    assert len(regions) == 5
    assert (regions[0].params[2] - regions[0].params[0]
            ) == (regions[2].params[2] - regions[2].params[1])
    assert (regions[1].params[2] - regions[1].params[0]
            ) == (regions[2].params[2] - regions[2].params[0])
    assert (regions[2].params[2] - regions[2].params[0]
            ) == (regions[3].params[2] - regions[3].params[0])
    assert (regions[4].params[2] - regions[4].params[0]
            ) == (regions[3].params[2] - regions[3].params[1])


def test_generate_regions_right_numbet_of_regions_for_N_2_and_negative_range():
    N = 2
    _range = np.linspace(-9, 0, num=101)
    regions = wm.generate_regions(_range, N)
    assert len(regions) == 5
    assert (regions[0].params[2] - regions[0].params[0]
            ) == (regions[2].params[2] - regions[2].params[1])
    assert (regions[1].params[2] - regions[1].params[0]
            ) == (regions[2].params[2] - regions[2].params[0])
    assert (regions[2].params[2] - regions[2].params[0]
            ) == (regions[3].params[2] - regions[3].params[0])
    assert (regions[4].params[2] - regions[4].params[0]
            ) == (regions[3].params[2] - regions[3].params[1])

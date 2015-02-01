import numpy as np


def trimf(x, params):
    """Triangular-shaped membership function

    Keyword arguments:
    x -- integer, float or (int or float) input numpy array
    params -- list with parameters a and c locate the "feet" of the triangle and the parameter b locates the peak.
    """

    if not (type(x) == int or type(x) == float or type(x) == np.ndarray):
        raise TypeError('x must be int, float or numpy array.')

    assert len(params) == 3

    a = float(params[0])
    b = float(params[1])
    c = float(params[2])

    if a > b or b > c or a > c:
        raise ValueError()

    if type(x) == int or type(x) == float:
        x = np.array([float(x)])

    result = np.zeros(len(x))

    index = (x <= a).nonzero()[0]
    result[index] = np.zeros(len(index))

    index = (x >= c).nonzero()[0]
    result[index] = np.zeros(len(index))

    if a != b:
        index = np.logical_and(x > a, x < b).nonzero()[0]
        result[index] = (x[index] - a) / (b - a)

    if b != c:
        index = np.logical_and(x > b, x < c).nonzero()[0]
        result[index] = (c - x[index]) / (c - b)

    index = (x == b).nonzero()[0]
    result[index] = np.ones(len(index))

    return result


def centroid(x, mf):
    """Returns a defuzzified value, of a membership function 'mf' positioned at associated variable value 'x'

    Keyword arguments:
    x -- (int or float) numpy array of a set or alpha cut
    mf -- (int or float) numpy array that represents a mf function
    """

    if not (type(mf) == np.ndarray):
        raise TypeError(
            'Undefined mf type. Assure that you are using numpy array.')
    if not (type(x) == np.ndarray):
        raise TypeError(
            'Undefined x type. Assure that you are using numpy array.')
    if not (len(x) == len(mf)):
        raise AssertionError('x and mf are not the same size.')

    return round((x * mf).sum() / mf.sum(), 4)  # rounded due to matlsb pattern

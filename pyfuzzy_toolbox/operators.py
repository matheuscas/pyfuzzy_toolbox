# -*- coding: utf-8 -*-

# UNTESTED


def t_norm(x, y, type='product'):
    """
    Binary operation T on the interval [0,1]

    TM(x,y)=min(x,y) (minimum or Godel t-norm)
    TP(x,y)=x*y (product t-norm)
    TL(x,y)=max(x+y−1,0) (Lukasiewicz t-norm)

    x and y -- numeric inputs for the triangular norm
    """

    if type == 'product':
        return x * y
    elif type == 'minimum':
        return min(x, y)
    elif type == 'Lukasiewicz':
        return max(x + y - 1, 0)
    else:
        raise TypeError("Triangular Norm type invalid")

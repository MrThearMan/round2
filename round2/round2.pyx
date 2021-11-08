cimport cython
from libc.math cimport round


@cython.cdivision(True)
cpdef round2(double n, int decimals = 0):
    """Round half up for positive and half down for negative numbers.

    :param n: Number to round.
    :type n: int or float
    :param decimals: Decimals to round to.
    :type decimals: int
    :return: Rounded number
    :rtype: int or float
    """

    cdef int m
    cdef double power = 10 ** decimals
    n = n * power
    n = round(n)

    m = <int>n

    if decimals == 0:
        return m
    
    n = m / power

    return n


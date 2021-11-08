"""Define typing for round2."""

from typing import *


def round2(n: Union[int, float], decimals: int = 0) -> Union[int, float]:
    """Round half up for positive and half down for negative numbers.

    :param n: Number to round.
    :param decimals: Decimals to round to.
    :return: Rounded number.
    """

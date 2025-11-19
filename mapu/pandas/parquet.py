import pandas as pd


def pa_mod(
    ds: int | pd.Series,
    divisor: int,
) -> int | pd.Series:
    """
    Calculates remainder after division by a positive divisor

    Args:
        ds: An integer value or a pd.Series with int64[pyarrow] dtype
        divisor: The positive divisor for the modulo operation

    Returns:
        pd.Series: An integer or pd.series containing the modulo results
    """

    if divisor <= 0:
        raise ValueError('Divisor must be a positive integer')

    # Check if divisor is a power of 2
    if divisor & (divisor - 1) == 0:
        # Efficient bitwise AND for power-of-2 divisors
        remainder = ds & (divisor - 1)
    else:
        # Slower integer division for non-power-of-2 divisors
        quotient = ds // divisor
        remainder = ds - (quotient * divisor)

    return remainder

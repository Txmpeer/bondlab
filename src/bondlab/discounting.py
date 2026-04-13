import numpy as np


def discount_factor(rate, t, frequency=2, compounding="discrete"):
    """
    Compute a discount factor for a given annual rate and time.
    """
    if t < 0:
        raise ValueError("t must be non-negative")

    if compounding not in {"discrete", "continuous"}:
        raise ValueError("compounding must be 'discrete' or 'continuous'")

    if compounding == "continuous":
        return float(np.exp(-rate * t))

    if frequency <= 0:
        raise ValueError("frequency must be a positive integer for discrete compounding")

    return float(1 / (1 + rate / frequency) ** (frequency * t))


def spot_to_discount_factor(rate, t, frequency=2, compounding="discrete"):
    """
    Convert a spot rate into a discount factor.
    """
    return discount_factor(rate, t, frequency=frequency, compounding=compounding)


def discount_factor_to_spot(df, t, frequency=2, compounding="discrete"):
    """
    Convert a discount factor into a spot rate.
    """
    if df <= 0:
        raise ValueError("discount factor must be positive")

    if t <= 0:
        raise ValueError("t must be positive")

    if compounding not in {"discrete", "continuous"}:
        raise ValueError("compounding must be 'discrete' or 'continuous'")

    if compounding == "continuous":
        return float(-np.log(df) / t)

    if frequency <= 0:
        raise ValueError("frequency must be a positive integer for discrete compounding")

    return float(frequency * ((1 / df) ** (1 / (frequency * t)) - 1))
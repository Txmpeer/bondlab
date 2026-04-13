import numpy as np


def portfolio_price(weights, prices):
    """
    Compute portfolio price/value as weighted sum.
    """
    weights = np.asarray(weights, dtype=float)
    prices = np.asarray(prices, dtype=float)

    if len(weights) != len(prices):
        raise ValueError("weights and prices must have the same length")

    return float(np.sum(weights * prices))


def portfolio_duration(weights, durations):
    """
    Compute weighted-average portfolio duration.
    """
    weights = np.asarray(weights, dtype=float)
    durations = np.asarray(durations, dtype=float)

    if len(weights) != len(durations):
        raise ValueError("weights and durations must have the same length")

    return float(np.sum(weights * durations))


def portfolio_dollar_duration(weights, dollar_durations=None, prices=None, modified_durations=None):
    """
    Compute portfolio dollar duration.

    Either provide:
    - dollar_durations directly, or
    - prices and modified_durations
    """
    weights = np.asarray(weights, dtype=float)

    if dollar_durations is not None:
        dollar_durations = np.asarray(dollar_durations, dtype=float)
        if len(weights) != len(dollar_durations):
            raise ValueError("weights and dollar_durations must have the same length")
        return float(np.sum(weights * dollar_durations))

    if prices is not None and modified_durations is not None:
        prices = np.asarray(prices, dtype=float)
        modified_durations = np.asarray(modified_durations, dtype=float)

        if not (len(weights) == len(prices) == len(modified_durations)):
            raise ValueError("weights, prices, and modified_durations must have the same length")

        return float(np.sum(weights * prices * modified_durations))

    raise ValueError("Provide either dollar_durations or both prices and modified_durations")


def portfolio_convexity(weights, convexities):
    """
    Compute weighted-average portfolio convexity.
    """
    weights = np.asarray(weights, dtype=float)
    convexities = np.asarray(convexities, dtype=float)

    if len(weights) != len(convexities):
        raise ValueError("weights and convexities must have the same length")

    return float(np.sum(weights * convexities))
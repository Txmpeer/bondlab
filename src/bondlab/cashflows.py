import numpy as np


def coupon_schedule(maturity, frequency=2):
    """
    Generate coupon payment times in years.

    Parameters
    ----------
    maturity : float
        Bond maturity in years.
    frequency : int, default=2
        Number of coupon payments per year.

    Returns
    -------
    numpy.ndarray
        Payment times in years.
    """
    if maturity <= 0:
        raise ValueError("maturity must be positive")

    if frequency <= 0:
        raise ValueError("frequency must be a positive integer")

    periods = int(round(maturity * frequency))
    return np.arange(1, periods + 1) / frequency


def bond_cashflows(face, coupon_rate, maturity, frequency=2):
    """
    Generate bond cash flow times and amounts.

    Parameters
    ----------
    face : float
        Face value of the bond.
    coupon_rate : float
        Annual coupon rate in decimal form.
    maturity : float
        Bond maturity in years.
    frequency : int, default=2
        Number of coupon payments per year.

    Returns
    -------
    tuple
        (times, cashflows)
    """
    if face <= 0:
        raise ValueError("face must be positive")

    if maturity <= 0:
        raise ValueError("maturity must be positive")

    if coupon_rate < 0:
        raise ValueError("coupon_rate cannot be negative")

    # Zero-coupon bond
    if coupon_rate == 0:
        times = np.array([maturity], dtype=float)
        cashflows = np.array([face], dtype=float)
        return times, cashflows

    times = coupon_schedule(maturity, frequency)
    coupon = face * coupon_rate / frequency
    cashflows = np.full(len(times), coupon, dtype=float)
    cashflows[-1] += face

    return times, cashflows
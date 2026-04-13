from scipy.optimize import brentq

from bondlab.discounting import spot_to_discount_factor
from bondlab.pricing import price_bond


def yield_to_maturity(price, face, coupon_rate, maturity, frequency=2, compounding="discrete"):
    """
    Solve for the yield to maturity that matches an observed bond price.
    """
    if price <= 0:
        raise ValueError("price must be positive")

    if face <= 0:
        raise ValueError("face must be positive")

    if maturity <= 0:
        raise ValueError("maturity must be positive")

    def objective(rate):
        return price_bond(
            face=face,
            coupon_rate=coupon_rate,
            maturity=maturity,
            rate=rate,
            frequency=frequency,
            compounding=compounding,
        ) - price

    return brentq(objective, -0.99, 1.0)


def forward_rate(r1, t1, r2, t2, frequency=2, compounding="discrete"):
    """
    Compute the forward rate implied between t1 and t2.
    """
    if t1 <= 0 or t2 <= 0:
        raise ValueError("t1 and t2 must be positive")

    if t2 <= t1:
        raise ValueError("t2 must be greater than t1")

    if compounding == "continuous":
        return float((r2 * t2 - r1 * t1) / (t2 - t1))

    df1 = spot_to_discount_factor(r1, t1, frequency=frequency, compounding=compounding)
    df2 = spot_to_discount_factor(r2, t2, frequency=frequency, compounding=compounding)

    return float(frequency * ((df1 / df2) ** (1 / (frequency * (t2 - t1))) - 1))
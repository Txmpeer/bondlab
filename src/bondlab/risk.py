from bondlab.cashflows import bond_cashflows
from bondlab.discounting import discount_factor
from bondlab.pricing import price_bond


def macaulay_duration(face, coupon_rate, maturity, rate, frequency=2, compounding="discrete"):
    """
    Compute Macaulay duration in years.
    """
    times, cashflows = bond_cashflows(face, coupon_rate, maturity, frequency)
    price = price_bond(
        face=face,
        coupon_rate=coupon_rate,
        maturity=maturity,
        rate=rate,
        frequency=frequency,
        compounding=compounding,
    )

    weighted_sum = 0.0
    for t, cf in zip(times, cashflows):
        pv = cf * discount_factor(rate, t, frequency=frequency, compounding=compounding)
        weighted_sum += t * pv

    return weighted_sum / price


def modified_duration(face, coupon_rate, maturity, rate, frequency=2, compounding="discrete"):
    """
    Compute modified duration.
    """
    mac_dur = macaulay_duration(
        face=face,
        coupon_rate=coupon_rate,
        maturity=maturity,
        rate=rate,
        frequency=frequency,
        compounding=compounding,
    )

    if compounding == "continuous":
        return mac_dur

    return mac_dur / (1 + rate / frequency)


def dollar_duration(face, coupon_rate, maturity, rate, frequency=2, compounding="discrete"):
    """
    Compute dollar duration.
    """
    price = price_bond(
        face=face,
        coupon_rate=coupon_rate,
        maturity=maturity,
        rate=rate,
        frequency=frequency,
        compounding=compounding,
    )

    mod_dur = modified_duration(
        face=face,
        coupon_rate=coupon_rate,
        maturity=maturity,
        rate=rate,
        frequency=frequency,
        compounding=compounding,
    )

    return mod_dur * price


def convexity(face, coupon_rate, maturity, rate, frequency=2, compounding="discrete"):
    """
    Compute bond convexity.
    """
    times, cashflows = bond_cashflows(face, coupon_rate, maturity, frequency)
    price = price_bond(
        face=face,
        coupon_rate=coupon_rate,
        maturity=maturity,
        rate=rate,
        frequency=frequency,
        compounding=compounding,
    )

    if compounding == "continuous":
        total = 0.0
        for t, cf in zip(times, cashflows):
            pv = cf * discount_factor(rate, t, frequency=frequency, compounding=compounding)
            total += (t ** 2) * pv
        return total / price

    total = 0.0
    for t, cf in zip(times, cashflows):
        pv = cf * discount_factor(rate, t, frequency=frequency, compounding=compounding)
        total += t * (t + 1 / frequency) * pv

    return total / price / (1 + rate / frequency) ** 2
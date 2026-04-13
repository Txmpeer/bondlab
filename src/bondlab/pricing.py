from bondlab.cashflows import bond_cashflows
from bondlab.curves import interpolate_rate
from bondlab.discounting import discount_factor


def price_zero_coupon_bond(face, rate, maturity, frequency=2, compounding="discrete"):
    """
    Price a zero-coupon bond.
    """
    if face <= 0:
        raise ValueError("face must be positive")

    if maturity <= 0:
        raise ValueError("maturity must be positive")

    df = discount_factor(rate, maturity, frequency=frequency, compounding=compounding)
    return face * df


def price_coupon_bond_from_ytm(face, coupon_rate, ytm, maturity, frequency=2, compounding="discrete"):
    """
    Price a coupon bond from its yield to maturity.
    """
    if coupon_rate < 0:
        raise ValueError("coupon_rate cannot be negative")

    times, cashflows = bond_cashflows(face, coupon_rate, maturity, frequency)

    price = 0.0
    for t, cf in zip(times, cashflows):
        price += cf * discount_factor(ytm, t, frequency=frequency, compounding=compounding)

    return price


def price_bond(face, coupon_rate, maturity, rate, frequency=2, compounding="discrete"):
    """
    General bond pricer.
    If coupon_rate == 0, prices as a zero-coupon bond.
    Otherwise, prices as a coupon bond using the given rate as YTM.
    """
    if coupon_rate == 0:
        return price_zero_coupon_bond(
            face=face,
            rate=rate,
            maturity=maturity,
            frequency=frequency,
            compounding=compounding,
        )

    return price_coupon_bond_from_ytm(
        face=face,
        coupon_rate=coupon_rate,
        ytm=rate,
        maturity=maturity,
        frequency=frequency,
        compounding=compounding,
    )


def price_bond_from_spot_curve(
    face,
    coupon_rate,
    maturity,
    spot_rates,
    times,
    frequency=2,
    compounding="discrete",
):
    """
    Price a bond using a spot curve.
    Spot rates are interpolated when necessary.
    """
    cf_times, cashflows = bond_cashflows(face, coupon_rate, maturity, frequency)

    price = 0.0
    for t, cf in zip(cf_times, cashflows):
        spot = interpolate_rate(times, spot_rates, t, method="linear")
        price += cf * discount_factor(spot, t, frequency=frequency, compounding=compounding)

    return price
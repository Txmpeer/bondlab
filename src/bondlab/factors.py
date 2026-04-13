import numpy as np

from bondlab.pricing import price_bond_from_spot_curve


def level_duration_from_curve(
    face,
    coupon_rate,
    maturity,
    spot_rates,
    times,
    shock=0.0001,
    frequency=2,
    compounding="discrete",
):
    """
    Compute level duration by applying a parallel shift to the curve.
    """
    base_price = price_bond_from_spot_curve(
        face=face,
        coupon_rate=coupon_rate,
        maturity=maturity,
        spot_rates=spot_rates,
        times=times,
        frequency=frequency,
        compounding=compounding,
    )

    shocked_rates = np.asarray(spot_rates, dtype=float) + shock

    shocked_price = price_bond_from_spot_curve(
        face=face,
        coupon_rate=coupon_rate,
        maturity=maturity,
        spot_rates=shocked_rates,
        times=times,
        frequency=frequency,
        compounding=compounding,
    )

    return float(-(shocked_price - base_price) / (base_price * shock))


def slope_duration_from_curve(
    face,
    coupon_rate,
    maturity,
    spot_rates,
    times,
    shock=0.0001,
    frequency=2,
    compounding="discrete",
):
    """
    Compute slope duration by applying a linear twist to the curve.
    Short-end rates are shifted down and long-end rates are shifted up.
    """
    times = np.asarray(times, dtype=float)
    spot_rates = np.asarray(spot_rates, dtype=float)

    base_price = price_bond_from_spot_curve(
        face=face,
        coupon_rate=coupon_rate,
        maturity=maturity,
        spot_rates=spot_rates,
        times=times,
        frequency=frequency,
        compounding=compounding,
    )

    twist = np.linspace(-shock, shock, len(spot_rates))
    shocked_rates = spot_rates + twist

    shocked_price = price_bond_from_spot_curve(
        face=face,
        coupon_rate=coupon_rate,
        maturity=maturity,
        spot_rates=shocked_rates,
        times=times,
        frequency=frequency,
        compounding=compounding,
    )

    return float(-(shocked_price - base_price) / (base_price * shock))
import numpy as np

from bondlab.cashflows import bond_cashflows
from bondlab.discounting import discount_factor_to_spot


def interpolate_rate(times, rates, target_time, method="linear"):
    """
    Interpolate a spot rate at a target maturity.
    """
    times = np.asarray(times, dtype=float)
    rates = np.asarray(rates, dtype=float)

    if len(times) != len(rates):
        raise ValueError("times and rates must have the same length")

    if method != "linear":
        raise ValueError("only 'linear' interpolation is supported in v1")

    return float(np.interp(target_time, times, rates))


def interpolate_discount_factor(times, discount_factors, target_time, method="linear"):
    """
    Interpolate a discount factor at a target maturity.
    """
    times = np.asarray(times, dtype=float)
    discount_factors = np.asarray(discount_factors, dtype=float)

    if len(times) != len(discount_factors):
        raise ValueError("times and discount_factors must have the same length")

    if method != "linear":
        raise ValueError("only 'linear' interpolation is supported in v1")

    return float(np.interp(target_time, times, discount_factors))


def bootstrap_spot_curve(prices, maturities, coupon_rates, face=100, frequency=2, compounding="discrete"):
    """
    Bootstrap spot rates and discount factors from bond prices.
    """
    prices = np.asarray(prices, dtype=float)
    maturities = np.asarray(maturities, dtype=float)
    coupon_rates = np.asarray(coupon_rates, dtype=float)

    if not (len(prices) == len(maturities) == len(coupon_rates)):
        raise ValueError("prices, maturities, and coupon_rates must have the same length")

    order = np.argsort(maturities)
    prices = prices[order]
    maturities = maturities[order]
    coupon_rates = coupon_rates[order]

    known_dfs = {}
    spot_rates = []

    for price, maturity, coupon_rate in zip(prices, maturities, coupon_rates):
        times, cashflows = bond_cashflows(face, coupon_rate, maturity, frequency)

        pv_known = 0.0
        last_time = times[-1]
        last_cf = cashflows[-1]

        for t, cf in zip(times[:-1], cashflows[:-1]):
            if t not in known_dfs:
                raise ValueError(
                    f"Missing discount factor for time {t}. "
                    "Provide bonds in bootstrap order compatible with coupon dates."
                )
            pv_known += cf * known_dfs[t]

        df_last = (price - pv_known) / last_cf

        if df_last <= 0:
            raise ValueError("Bootstrapped discount factor must be positive")

        known_dfs[last_time] = df_last
        spot = discount_factor_to_spot(
            df_last,
            last_time,
            frequency=frequency,
            compounding=compounding,
        )
        spot_rates.append(spot)

    boot_times = list(maturities)
    boot_dfs = [known_dfs[t] for t in boot_times]

    return {
        "maturities": np.array(boot_times, dtype=float),
        "spot_rates": np.array(spot_rates, dtype=float),
        "discount_factors": np.array(boot_dfs, dtype=float),
    }
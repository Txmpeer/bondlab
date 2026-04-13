from bondlab.curves import (
    interpolate_rate,
    interpolate_discount_factor,
    bootstrap_spot_curve,
)
from bondlab.discounting import spot_to_discount_factor


def test_interpolate_rate_linear():
    times = [1, 2]
    rates = [0.04, 0.06]
    interpolated = interpolate_rate(times, rates, 1.5)
    assert abs(interpolated - 0.05) < 1e-12


def test_interpolate_discount_factor_linear():
    times = [1, 2]
    dfs = [0.96, 0.90]
    interpolated = interpolate_discount_factor(times, dfs, 1.5)
    assert abs(interpolated - 0.93) < 1e-12


def test_bootstrap_spot_curve_with_zero_coupon_bonds():
    maturities = [1, 2]
    spot_rates = [0.05, 0.06]
    prices = [
        100 * spot_to_discount_factor(0.05, 1, frequency=1, compounding="discrete"),
        100 * spot_to_discount_factor(0.06, 2, frequency=1, compounding="discrete"),
    ]
    coupon_rates = [0.0, 0.0]

    curve = bootstrap_spot_curve(
        prices=prices,
        maturities=maturities,
        coupon_rates=coupon_rates,
        face=100,
        frequency=1,
        compounding="discrete",
    )

    assert len(curve["maturities"]) == 2
    assert len(curve["spot_rates"]) == 2
    assert abs(curve["spot_rates"][0] - 0.05) < 1e-10
    assert abs(curve["spot_rates"][1] - 0.06) < 1e-10
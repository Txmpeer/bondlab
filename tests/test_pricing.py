from bondlab.discounting import spot_to_discount_factor
from bondlab.pricing import (
    price_zero_coupon_bond,
    price_coupon_bond_from_ytm,
    price_bond,
    price_bond_from_spot_curve,
)


def test_price_zero_coupon_bond():
    price = price_zero_coupon_bond(face=100, rate=0.05, maturity=1, frequency=1)
    expected = 100 / 1.05
    assert abs(price - expected) < 1e-9


def test_price_coupon_bond_from_ytm():
    price = price_coupon_bond_from_ytm(
        face=100,
        coupon_rate=0.06,
        ytm=0.06,
        maturity=2,
        frequency=2,
    )
    assert abs(price - 100) < 1e-9


def test_price_bond_zero_coupon_path():
    price = price_bond(face=100, coupon_rate=0, maturity=1, rate=0.05, frequency=1)
    expected = 100 / 1.05
    assert abs(price - expected) < 1e-9


def test_price_bond_from_spot_curve_zero_coupon():
    times = [1, 2]
    spot_rates = [0.05, 0.06]

    price = price_bond_from_spot_curve(
        face=100,
        coupon_rate=0.0,
        maturity=2,
        spot_rates=spot_rates,
        times=times,
        frequency=1,
        compounding="discrete",
    )

    expected = 100 * spot_to_discount_factor(0.06, 2, frequency=1, compounding="discrete")
    assert abs(price - expected) < 1e-9
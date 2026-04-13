from bondlab.pricing import price_bond
from bondlab.risk import (
    macaulay_duration,
    modified_duration,
    dollar_duration,
    convexity,
)


def test_macaulay_duration_zero_coupon_equals_maturity():
    dur = macaulay_duration(face=100, coupon_rate=0, maturity=3, rate=0.05, frequency=2)
    assert abs(dur - 3.0) < 1e-9


def test_modified_duration_is_less_than_macaulay_for_discrete_compounding():
    mac = macaulay_duration(face=100, coupon_rate=0.06, maturity=4, rate=0.05, frequency=2)
    mod = modified_duration(face=100, coupon_rate=0.06, maturity=4, rate=0.05, frequency=2)
    assert mod < mac


def test_dollar_duration_equals_modified_duration_times_price():
    price = price_bond(face=100, coupon_rate=0.06, maturity=4, rate=0.05, frequency=2)
    mod = modified_duration(face=100, coupon_rate=0.06, maturity=4, rate=0.05, frequency=2)
    dd = dollar_duration(face=100, coupon_rate=0.06, maturity=4, rate=0.05, frequency=2)
    assert abs(dd - mod * price) < 1e-9


def test_convexity_is_positive():
    cx = convexity(face=100, coupon_rate=0.06, maturity=4, rate=0.05, frequency=2)
    assert cx > 0
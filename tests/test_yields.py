from bondlab.pricing import price_bond
from bondlab.yields import yield_to_maturity, forward_rate


def test_yield_to_maturity_recovers_original_rate():
    true_ytm = 0.05
    price = price_bond(
        face=100,
        coupon_rate=0.06,
        maturity=2,
        rate=true_ytm,
        frequency=2,
    )

    estimated_ytm = yield_to_maturity(
        price=price,
        face=100,
        coupon_rate=0.06,
        maturity=2,
        frequency=2,
    )

    assert abs(estimated_ytm - true_ytm) < 1e-9


def test_forward_rate_continuous():
    r1 = 0.04
    t1 = 1
    r2 = 0.05
    t2 = 2

    fwd = forward_rate(r1, t1, r2, t2, compounding="continuous")
    expected = (r2 * t2 - r1 * t1) / (t2 - t1)

    assert abs(fwd - expected) < 1e-12
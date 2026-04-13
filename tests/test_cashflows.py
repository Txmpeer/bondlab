from bondlab.cashflows import bond_cashflows


def test_zero_coupon_cashflows():
    times, cashflows = bond_cashflows(face=100, coupon_rate=0, maturity=2)
    assert len(times) == 1
    assert len(cashflows) == 1
    assert times[0] == 2
    assert cashflows[0] == 100


def test_coupon_bond_cashflows():
    times, cashflows = bond_cashflows(face=100, coupon_rate=0.06, maturity=2, frequency=2)
    assert len(times) == 4
    assert abs(cashflows[0] - 3.0) < 1e-9
    assert abs(cashflows[-1] - 103.0) < 1e-9
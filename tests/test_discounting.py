from bondlab.discounting import (
    discount_factor,
    spot_to_discount_factor,
    discount_factor_to_spot,
)


def test_spot_to_discount_factor_matches_discount_factor():
    df1 = spot_to_discount_factor(0.05, 2, frequency=2, compounding="discrete")
    df2 = discount_factor(0.05, 2, frequency=2, compounding="discrete")
    assert abs(df1 - df2) < 1e-12


def test_discount_factor_to_spot_round_trip_discrete():
    rate = 0.05
    t = 2
    df = spot_to_discount_factor(rate, t, frequency=2, compounding="discrete")
    recovered = discount_factor_to_spot(df, t, frequency=2, compounding="discrete")
    assert abs(recovered - rate) < 1e-12


def test_discount_factor_to_spot_round_trip_continuous():
    rate = 0.05
    t = 2
    df = spot_to_discount_factor(rate, t, compounding="continuous")
    recovered = discount_factor_to_spot(df, t, compounding="continuous")
    assert abs(recovered - rate) < 1e-12
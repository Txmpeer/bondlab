from bondlab.factors import level_duration_from_curve, slope_duration_from_curve


def test_level_duration_from_curve_is_positive():
    ld = level_duration_from_curve(
        face=100,
        coupon_rate=0.05,
        maturity=3,
        spot_rates=[0.04, 0.045, 0.05],
        times=[1, 2, 3],
        shock=0.0001,
        frequency=1,
    )
    assert ld > 0


def test_slope_duration_from_curve_returns_float():
    sd = slope_duration_from_curve(
        face=100,
        coupon_rate=0.05,
        maturity=3,
        spot_rates=[0.04, 0.045, 0.05],
        times=[1, 2, 3],
        shock=0.0001,
        frequency=1,
    )
    assert isinstance(sd, float)
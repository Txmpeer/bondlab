from bondlab.portfolio import (
    portfolio_price,
    portfolio_duration,
    portfolio_dollar_duration,
    portfolio_convexity,
)


def test_portfolio_price():
    value = portfolio_price([0.4, 0.6], [100, 120])
    assert abs(value - 112.0) < 1e-12


def test_portfolio_duration():
    dur = portfolio_duration([0.4, 0.6], [4.0, 6.0])
    assert abs(dur - 5.2) < 1e-12


def test_portfolio_dollar_duration_direct():
    dd = portfolio_dollar_duration([0.4, 0.6], dollar_durations=[3.0, 5.0])
    assert abs(dd - 4.2) < 1e-12


def test_portfolio_dollar_duration_from_prices_and_modified_durations():
    dd = portfolio_dollar_duration(
        [0.4, 0.6],
        prices=[100, 120],
        modified_durations=[4.0, 5.0],
    )
    expected = 0.4 * 100 * 4.0 + 0.6 * 120 * 5.0
    assert abs(dd - expected) < 1e-12


def test_portfolio_convexity():
    cx = portfolio_convexity([0.4, 0.6], [10.0, 14.0])
    assert abs(cx - 12.4) < 1e-12
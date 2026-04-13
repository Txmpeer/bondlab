# bondlab

A Python library for fixed-income analytics.

`bondlab` provides reusable tools for pricing zero-coupon and coupon bonds, computing discount factors, estimating yield to maturity, constructing spot curves through bootstrapping, interpolating term structures, measuring interest-rate risk through duration and convexity, and performing portfolio and factor-based curve sensitivity analysis.

---

## Features

- Zero-coupon bond pricing  
- Coupon bond pricing from yield to maturity  
- General bond pricing interface  
- Discount factors and spot-rate conversions  
- Yield to maturity solver  
- Forward rates  
- Macaulay, modified, and dollar duration  
- Convexity  
- Spot-curve interpolation  
- Bootstrapping from bond prices  
- Portfolio analytics  
- Level and slope duration from curve shocks  

---

## Installation

```bash
pip install bondlab-txmpeer
```

## Quick Example

```python
import bondlab as bl

price = bl.price_bond(
    face=100,
    coupon_rate=0.05,
    maturity=5,
    rate=0.06,
    frequency=2,
)

duration = bl.macaulay_duration(
    face=100,
    coupon_rate=0.05,
    maturity=5,
    rate=0.06,
    frequency=2,
)

print(price)
print(duration)

```

## Tutorial Notebook:

[Open in Colab](https://colab.research.google.com/github/Txmpeer/bondlab/blob/main/notebooks/tutorial.ipynb)

## Running Tests:

pytest

## Project Structure:

bondlab/
├── src/bondlab/
├── tests/
├── notebooks/
├── docker/
├── .github/workflows/
├── README.md
└── pyproject.toml

## License

MIT
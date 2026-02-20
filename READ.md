# Aggressive Monthly Options Sniper

This is a Streamlit app to scan options, simulate a small aggressive portfolio, and backtest historical trades using Yahoo Finance.

## Features

- Builds a universe of ~200 high-volume tickers
- Scores options based on volume, OI, delta, IV, and breakout potential
- Displays top 5 calls and puts
- Simulates a $500 aggressive allocation
- 90-day rolling backtest
- Save snapshots of scored options

## Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py

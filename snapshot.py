import streamlit as st
import yfinance as yf
import datetime
import pandas as pd

st.set_page_config(layout="wide")
st.title("Portfolio Snapshot / Backtest")

st.write("This page can run your historical 90-day backtest or save portfolio snapshots.")

if st.button("Run 90-Day Backtest"):
    capital = 500
    trades = 0
    wins = 0
    losses = 0

    end_date = datetime.datetime.today()
    start_date = end_date - datetime.timedelta(days=120)
    tickers = ["AAPL","MSFT","NVDA","AMZN","GOOGL"]

    for ticker in tickers:
        hist = yf.download(ticker, start=start_date, end=end_date, progress=False)
        if len(hist) < 30:
            continue
        for i in range(10, len(hist)-5):
            entry = hist["Close"].iloc[i]
            exit = hist["Close"].iloc[i+5]
            pct_move = (exit-entry)/entry
            position_size = capital*0.2
            pnl = position_size*pct_move
            capital += pnl
            trades += 1
            if pnl>0:
                wins +=1
            else:
                losses+=1
    if trades>0:
        st.write(f"Trades: {trades}, Wins: {wins}, Losses: {losses}")
        st.write(f"Ending Capital: ${round(capital,2)}")
    else:
        st.write("No trades simulated.")

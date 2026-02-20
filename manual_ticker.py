import streamlit as st
import yfinance as yf
import pandas as pd

st.set_page_config(layout="wide")
st.title("Manual Ticker Scoring")

ticker_input = st.text_input("Enter a ticker (e.g., AAPL)")

if st.button("Score Ticker") and ticker_input:
    try:
        stock = yf.Ticker(ticker_input.upper())
        hist = stock.history(period="6mo")
        last_price = hist["Close"].iloc[-1]

        score = 0
        if hist["Close"].iloc[-1] > hist["Close"].rolling(50).mean().iloc[-1]:
            score += 3
        if hist["Close"].iloc[-1] > hist["Close"].rolling(200).mean().iloc[-1]:
            score += 2

        st.write(f"{ticker_input.upper()} Current Price: ${last_price:.2f}")
        st.write(f"{ticker_input.upper()} Score: {score}")

        # Show best options this month
        expirations = stock.options
        if expirations:
            exp = expirations[0]
            chain = stock.option_chain(exp)
            calls, puts = chain.calls, chain.puts
            st.subheader("Top Calls")
            st.dataframe(calls.head(5))
            st.subheader("Top Puts")
            st.dataframe(puts.head(5))
        else:
            st.write("No options found for this ticker.")
    except:
        st.write("Ticker not valid or no data available.")

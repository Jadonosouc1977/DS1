import yfinance as yf
import streamlit as st
import pandas as pd

st.write('Simple Stock Price App')

tickerSymbol = 'GOOGL'

tickerData = yf.ficker(tickerSymbol)

tickerDf = tickerData.history(period='id',start ='2010-5-31', end = '2020-5-31')

st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)


import yfinance as yf
import streamlit as st
import pandas as pd

st.write('Simple Stock Price App')

tickerSymbol = 'GOOGL'

tickerData = yf.Ticker(tickerSymbol)

tickerDf = tickerData.history(period='id',start ='2022-5-31', end = '2023-5-31')

st.line_chart(tickerDf.Close)

st.write('Prueba')

st.line_chart(tickerDf.Volume)

st.write('END')

import streamlit as st
import model as m
import pandas as pd

st.title("Security Analysis")  # title for the page

ticker_list = m.get_ticker_list_nse()
updated_ticker_list = [t + ".NS" for t in ticker_list]

st.subheader("Select Multiple Stocks")
tickers = st.multiselect("Select multiple stocks",
                         updated_ticker_list, label_visibility="collapsed")

i = 1
for t in tickers:
    st.write(str(i) + ".) " + t)
    i += 1

key_financial_data = m.get_key_financials_data(tickers)
key_statistic_data = m.get_key_statistics_data(tickers)

st.write(key_financial_data)
st.write(key_statistic_data)
# st.dataframe(pd.json_normalize(key_financial_data, ))

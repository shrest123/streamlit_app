import pandas as pd
import streamlit as st
import yfinance as yf
import datetime

# Heading which i have given
st.write(
    """
    # Stock Price Analyser

    Shown are the stock price of Apple.
    """
)
# for apple stock pice data we will use y_finance package

ticker_symbol=st.text_input("Enter Stock Symbol","AAPL",key="placeholder")
# ticker_symbol="AAPL"    # ticker symboll store the share name (like vaiabe)and apple is denoted as appl

col1,col2=st.columns(2) # it will create the 2 columns layout


# stating date selection from user
with col1:
    start_date=st.date_input("Input Starting Date",
                datetime.date(2019,1,1))    # if user doesnot input anything it will be default value
# ending date capturing from user
with col2:
    end_date=st.date_input("Input End Date",
                datetime.date(2022,1,1))
st.write(f"""
## {ticker_symbol}'s End Of Day Price
""")
ticker_data=yf.Ticker(ticker_symbol)  # capturing stock data making object
# ticker_df=ticker_data.history(period="1d",start="2019-01-01",end="2022-12-31") # mention date in code
ticker_df=ticker_data.history(period="1d",start=f"{start_date}",end=f"{end_date}")
# here the 1d refer end of day the stock price here the start date and end date we will store the stock price"
# ticker_df store the data frame
st.dataframe(ticker_df)  # it display the dataframe in the screen by this command

st.write("""
## Daily Closing Price Chart
""")
# Showing the charts of Volume feature in dataframe
st.line_chart(ticker_df.Close) # Close is feature name of data frame
st.write("""
## Daily Volume Chart
""")
# Showing the charts
st.line_chart(ticker_df.Volume) # Close is feature name of data frame
 
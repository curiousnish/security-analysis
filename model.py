import pandas as pd
import datetime as dt
from yahoofinancials import YahooFinancials


def get_ticker_list_nse(save=False):
    # link for all the active NSE trading equities
    url = "https://archives.nseindia.com/content/equities/EQUITY_L.csv"
    ticker_list = pd.read_csv(url)  # reading in dataframe

    if save:
        ticker_list.to_csv("nifty_sec.csv")

    # output of this function is used in the webapp
    return ticker_list["SYMBOL"].to_list()


def get_key_financials_data(quote):
    key_financial_data = YahooFinancials(quote)
    # print(key_financial_data.get_financial_data())
    # print(pd.json_normalize(key_financial_data.get_financial_data()))
    return key_financial_data.get_financial_data()


def get_key_statistics_data(quote):
    key_statistic_data = YahooFinancials(quote)
    # print(key_financial_data.get_financial_data())
    # print(pd.json_normalize(key_financial_data.get_financial_data()))
    return key_statistic_data.get_key_statistics_data()


if __name__ == "__main__":
    # get_ticker_list_nse()
    get_key_financials_data(["TCS.NS"])

import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta

class StockDataModule:
    def __init__(self):
        self.stock_symbols = ['RELIANCE.NS', 'TCS.NS', 'INFY.NS', 'HDFCBANK.NS', 
                              'ICICIBANK.NS', 'KOTAKBANK.NS', 'LT.NS', 'SBIN.NS', 
                              'AXISBANK.NS', 'BAJFINANCE.NS']
        self.one_month_ago = datetime.now() - timedelta(days=30)
        self.end_date = datetime.now().strftime('%Y-%m-%d')
        self.start_date = self.one_month_ago.strftime('%Y-%m-%d')

    def check_52_week_high(self, symbol):
        stock = yf.Ticker(symbol)
        hist = stock.history(start=self.start_date, end=self.end_date)

        try:
            high_52_weeks = stock.info['fiftyTwoWeekHigh']
        except KeyError:
            print(f"Skipping {symbol}: Missing 'fiftyTwoWeekHigh' in data.")
            return False
        
        max_high_last_month = hist['High'].max() if not hist.empty else None

        # Debugging: Print stock data
        print(f"\nStock: {symbol}")
        print(f"52-Week High: {high_52_weeks}")
        print(f"Max High in Last Month: {max_high_last_month}")

        if max_high_last_month and max_high_last_month >= high_52_weeks:
            return True
        return False

    def get_stocks_52_week_high(self):
        stocks_52_week_high = [symbol for symbol in self.stock_symbols if self.check_52_week_high(symbol)]
        return stocks_52_week_high

if __name__ == "__main__":
    stock_module = StockDataModule()
    high_stocks = stock_module.get_stocks_52_week_high()

    print("\nStocks that hit 52-week high in the last month:")
    for symbol in high_stocks:
        print(symbol)

import yfinance as yf
import datetime

class Dividend:
    def __init__(self, symbol, date, amount):
        self.symbol = symbol
        self.date = date
        self.amount = amount

    def to_dict(self):
        return {
            'symbol': self.symbol,
            'date': self.date.strftime('%Y-%m-%d'),
            'amount': self.amount
        }

class YahooFinanceService:
    @staticmethod
    def get_dividends(symbol):
        try:
            # Use the yfinance module to get dividend data
            stock = yf.Ticker(symbol)
            dividends = stock.dividends

            # Process the data and create Dividend objects
            dividend_objects = []
            for date, amount in dividends.items():
                date = date.replace(hour=0, minute=0, second=0, microsecond=0)  # Remove time information
                dividend = Dividend(symbol, date, amount)
                dividend_objects.append(dividend)

            # Return the list of dividend objects
            return [dividend.to_dict() for dividend in dividend_objects]

        # Handle any exceptions that may occur during the request
        except Exception as e:
            # Return an error message or handle the exception as needed
            return {"error": f"Failed to retrieve dividends: {str(e)}"}


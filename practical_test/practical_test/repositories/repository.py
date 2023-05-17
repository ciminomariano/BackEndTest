from practical_test.models.dividend import Dividend


class DividendRepository:
    def save_dividend(self, symbol, date, amount):
        dividend = Dividend(symbol=symbol, date=date, amount=amount)
        dividend.save()

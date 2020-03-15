from stock.models import Stock


def get_all_distinct_symbols():
    stocks = Stock.objects.all().values_list('symbol', flat=True).distinct()
    return stocks

def get_stocks_from_symbols(symbol):
    stocks = Stock.objects.filter(symbol = symbol)
    return stocks
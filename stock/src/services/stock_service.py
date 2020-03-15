import csv
from datetime import datetime

from stock.models import Stock


class StockService:

    @staticmethod
    def parse_and_persist_stocks_files(files):
        for file in files:
            try:
                with open(file, 'r',  encoding="utf8") as file:
                    reader = csv.reader(file)
                    next(reader)
                    for row in reader:
                        stock = StockService.get_stock_model(row)
                        stock.save()
                print("Parsed and saved file-", file)
            except Exception as e:
                print("Parsing csv file - {} failed".format(file) + ", exception: " + str(e))

    @staticmethod
    def get_stock_model(row):
        stock = Stock()
        stock.symbol = row[0]
        stock.series = row[1]
        stock.open_stock = row[2]
        stock.high_value = row[3]
        stock.low_value = row[4]
        stock.close_value = row[5]
        stock.last_value = row[6]
        stock.prev_close_value = row[7]
        stock.ttr_dqty_value = row[8]
        stock.ttr_dval_value = row[9]
        stock.time_stamp = datetime.strptime(row[10], '%d-%b-%Y').date()
        stock.total_trades = row[11]
        stock.isin = row[12]

        return stock
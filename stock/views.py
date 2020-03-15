from django.http import HttpResponse
from django.shortcuts import render

import django_tables2 as tables

from stock.forms import SymbolDataForm, DownloadStockDataForm
from stock.models import Stock
from stock.src.common.common import BASE_URL, FILE_NAME_FORMAT, DOWNLOAD_FILE_PATH
from stock.src.dao.StockModelDao import get_stocks_from_symbols
from stock.src.services.download_stock_service import DownloadStocksService
from stock.src.services.stock_service import StockService

class SimpleTable(tables.Table):
    class Meta:
        model = Stock

def index(request):
    return render(request, '../templates/index.html')

def download_data(request):
    if request.method == 'POST':
        form = DownloadStockDataForm(request.POST)
        if form.is_valid():
            month = form.cleaned_data['month']
            month = month.upper()
            year = form.cleaned_data['year']
            files = DownloadStocksService.download_and_parse_files(BASE_URL, FILE_NAME_FORMAT, year, month,
                                                                   DOWNLOAD_FILE_PATH)
            StockService.parse_and_persist_stocks_files(files)
            return HttpResponse("Donwloaded and saved Stocks data for {} {}".format(month, year))
    else:
        form = DownloadStockDataForm()

    context = {
        'form': form,
    }
    return render(request, '../templates/download_stock_data.html', context)

def get_symbol_data(request):
    if request.method == 'POST':
        form = SymbolDataForm(request.POST)
        if form.is_valid():
            symbol = form.cleaned_data['symbol']
            stocks = get_stocks_from_symbols(symbol)
            if stocks:
                table = SimpleTable(stocks)
                return render(request, '../templates/show_symbol_data.html', {"table": table})
            else:
                return HttpResponse("No results found")
    else:
        form = SymbolDataForm()

    context = {
        'form': form,
    }
    return render(request, '../templates/symbol_data.html', context)
from django import forms

from datalore import settings
from stock.src.dao.StockModelDao import get_all_distinct_symbols

class DownloadStockDataForm(forms.Form):
    month = forms.CharField(label="Month", widget=forms.TextInput(attrs={'placeholder':'Enter month in short word format, Ex: Jan, Feb, Mar, etc;'}))
    year = forms.IntegerField(label="Year")

class SymbolDataForm(forms.Form):
    symbol_list = get_all_distinct_symbols()
    symbol_choices = [tuple([choice, choice]) for choice in symbol_list]
    symbol = forms.ChoiceField(choices=symbol_choices, label="Get Data of Symbol")
from django.db import models

# Create your models here.
class Stock(models.Model):
    symbol = models.CharField(max_length=255, null=False)
    series = models.CharField(max_length=255)
    open_stock = models.FloatField(blank=True, null=True)
    high_value = models.FloatField(blank=True, null=True)
    low_value = models.FloatField(blank=True, null=True)
    close_value = models.FloatField(blank=True, null=True)
    last_value = models.FloatField(blank=True, null=True)
    prev_close_value = models.FloatField(blank=True, null=True)
    ttr_dqty_value = models.FloatField(blank=True, null=True)
    ttr_dval_value = models.FloatField(blank=True, null=True)
    time_stamp = models.DateField(blank=True, null=True)
    total_trades = models.PositiveIntegerField(blank=True, null=True)
    isin = models.CharField(max_length=255, null=True)
from django.db import models

# Create your models here.
from django.db import models

class Stock(models.Model):
    date = models.CharField(max_length=100)
    trade_code = models.CharField(max_length=100)
    high = models.IntegerField()
    low = models.IntegerField()
    open = models.IntegerField()
    close = models.IntegerField()
    volume = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    @staticmethod
    def create_stock(date, trade_code, high, low, open, close, volume):
        stock = Stock(date=date, trade_code=trade_code, high=high, low=low, open=open, close=close, volume=volume)
        stock.save()

    def update_stock(self, date, trade_code, high, low, open, close, volume):
        self.date = date
        self.trade_code = trade_code
        self.high = high
        self.low = low
        self.open = open
        self.close = close
        self.volume = volume
        self.save()

    def delete_stock(self):
        self.delete()


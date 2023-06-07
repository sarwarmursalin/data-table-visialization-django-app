from django.shortcuts import render,redirect
from django.http import HttpResponse
import json
# Create your views here.

# from myapp.models import Stock

# def load_data():
#     with open('stock_market_data.json') as file:
#         data = json.load(file)

#     for item in data:
#         stock = Stock(date=item['date'], trade_code=item['trade_code'], high=item['high'], low=item['low'], open=item['open'], close=item['close'], volume=item['volume'])
#         stock.save()

# if __name__ == '__main__':
#     load_data()


# def data(request):
#     stock = Stock.objects.all()
#     return render(request, 'data.html', {'stock':stock})
   


def data(request):
    with open('stock_market_data.json') as file:
        json_data = json.load(file)
    
    context = {
        'json_data': json_data
    }
    return render(request, 'data.html', context)


def create(request):
    if request.method == 'POST':
        date = request.POST['date']
        trade_code = request.POST['trade_code']
        high = request.POST['high']
        low = request.POST['low']
        open = request.POST['open']
        close = request.POST['close']
        volume = request.POST['volume']
        Stock.create_stock(date, trade_code, high, low, open, close, volume)
        return redirect('data')

def update(request, stock_id):
    stock = Stock.objects.get(id=stock_id)
    if request.method == 'POST':
        date = request.POST['date']
        trade_code = request.POST['trade_code']
        high = request.POST['high']
        low = request.POST['low']
        open = request.POST['open']
        close = request.POST['close']
        volume = request.POST['volume']
        stock.update_person(date, trade_code, high, low, open, close, volume)
        return redirect('data')
    return render(request, 'update.html', {'stock': stock})

def delete(request, stock_id):
    stock = Stock.objects.get(id=stock_id)
    stock.delete_stock()
    return redirect('data')



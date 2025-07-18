from services import price_token
from services import chat_gpt

from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string

def forecast_data(request):

    btc_price = price_token.get_btc_price()
    eth_price = price_token.get_eth_price()
    price_prediction = chat_gpt.main()
    print(price_prediction)

    context = {
        'btc_price': btc_price,
        'eth_price': eth_price,
        'week_btc': price_prediction['week']['btc'],
        'week_eth': price_prediction['week']['eth'],
        'month_btc': price_prediction['month']['btc'],
        'month_eth': price_prediction['month']['eth'],
        'six_months_btc': price_prediction['six_months']['btc'],
        'six_months_eth': price_prediction['six_months']['eth'],
    }

    html = render_to_string('forecast/forecast.html', context)
    return HttpResponse(html)

def forecast_view(request):
    return render(request, 'forecast/forecast_loading.html')
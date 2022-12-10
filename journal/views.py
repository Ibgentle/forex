from django.shortcuts import render, get_object_or_404
from .models import Trade
# Create your views here.

def trade_list(request):
    trades = Trade.objects.all()

    return render(request,
            'journal/trade/list.html',
            {'trades': trades})

def trade_detail(request, id):
    trade = get_object_or_404(Trade,
            id=id)

    return render(request,
            'journal/trade/detail.html',
            {'trade': trade})


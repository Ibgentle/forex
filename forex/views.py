from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import ProfitabilityForm


@csrf_exempt
def calculator(request):
    if request.method == 'POST':
        form = ProfitabilityForm(request.GET)
        if form.is_valid():
            form.save()

    else:
        form = ProfitabilityForm()

    return render(request, 'calculator.html', {'form': form})


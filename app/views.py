from django.shortcuts import render
from . import forms
from django.http import HttpResponse

def calc(request):
    if request.method == 'POST':
        form = forms.CalcForm(request.POST)

        if form.is_valid():
            price_per_kg = form.cleaned_data['price_per_kg']
            weight_in_grams = form.cleaned_data['weight_in_grams']
            total = (price_per_kg * weight_in_grams) / 1000
            
            return HttpResponse(f'TOTAL = {total:.2f}')
        
    else:
        form = forms.CalcForm()

    return render(
        request,
        'main.html',
        {'form': form}
    )
from django import forms

class CalcForm(forms.Form):
    price_per_kg = forms.DecimalField(decimal_places=2)
    weight_in_grams = forms.IntegerField()
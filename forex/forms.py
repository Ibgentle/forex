from django import forms

class ProfitabilityForm(forms.Form):
    capital = forms.IntegerField(label="Enter your capital")
    percentage = forms.IntegerField(label="Percentage of capital")
    days = forms.IntegerField(label="Number of days")
    trades = forms.IntegerField(label="Number of trades a day")
    broker_payout = forms.IntegerField(label="Broker Payout Percentage")

from django import forms
import datetime
from .models import Ticket, Category, Item

class TicketForm(forms.ModelForm):
    place = forms.CharField(label='Miejsce', max_length=100)
    date = forms.DateField(label='Data', initial=datetime.date.today().strftime('%Y-%m-%d'))
    serial = forms.CharField(label='Numer paragonu', max_length=100)
    total = forms.FloatField(label='Suma')
    class Meta:
        model = Ticket
        fields = ("place", "date", "serial", "total")

class ItemForm(forms.ModelForm):
    name = forms.CharField(label='Nazwa', max_length=100)
    category = forms.ModelChoiceField(label="Kategoria", queryset=Category.objects.all())
    number = forms.IntegerField(label='Ilosc',  widget=forms.TextInput(attrs={
        'class': 'itemsNumber',
        'type': 'number',
        'step': '0.001'
    }))
    singleCost = forms.FloatField(label='Cena jednostkowa', widget=forms.TextInput(attrs={
        'readonly':'readonly',
        'class': 'singleCost',
        'type': 'number'
    }))
    cost = forms.FloatField(label='Cena', widget=forms.TextInput(attrs={
        'class':'cost',
        'type': 'number',
        'step': '0.001'
    }))
    class Meta:
        model = Item
        fields = ("name", "category", "number", "singleCost", "cost")
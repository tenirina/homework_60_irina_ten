from django import forms
from django.forms import widgets


class SearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False, label="Search", initial="")


class ProductForm(forms.Form):
    title = forms.CharField(max_length=100, required=True, label="Title")
    description = forms.CharField(max_length=2000, required=False, label="Description",  widget=widgets.Textarea)
    photo = forms.CharField(max_length=200, required=True, label="Photo")
    category = forms.CharField(max_length=100, required=True, label="Category")
    balance = forms.IntegerField(required=True, label="Balance")
    price = forms.DecimalField(max_digits=9, decimal_places=2, required=True, label="Price")

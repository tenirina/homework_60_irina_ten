from django import forms
from django.core.exceptions import ValidationError
from django.db.models.query import QuerySet
from django.forms import widgets

from webapp.models import Product


def max_length_validator(string):
    if len(string) < 4:
        raise ValidationError("The number of characters must be more than 3!")
    return string


class SearchForm(forms.Form):
    search_value = forms.CharField(required=False, label='Search', max_length=100)


class ProductForm(forms.ModelForm):
    title = forms.CharField(max_length=100, required=True, label="Title", validators=(max_length_validator, ))
    description = forms.CharField(max_length=2000, required=False, label="Description",  widget=widgets.Textarea)
    photo = forms.CharField(max_length=200, required=False, label="Photo")
    balance = forms.IntegerField(required=True, label="Balance", min_value=0)
    price = forms.DecimalField(max_digits=9, decimal_places=2, required=True, label="Price")

    class Meta:
        model = Product
        fields = ('title', 'description', 'photo', 'category', 'balance', 'price')



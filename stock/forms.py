
from django import forms

from categories.models import Category


class StockReportForm(forms.Form):

    categories = forms.ModelMultipleChoiceField(
        required=False,
        queryset=Category.objects.all())

    ids = forms.CharField(required=False)

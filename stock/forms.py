
from django import forms
from django.utils.translation import ugettext_lazy as _

from categories.models import Category


class StockReportForm(forms.Form):

    categories = forms.ModelMultipleChoiceField(
        required=False,
        queryset=Category.objects.all())

    ids = forms.CharField(required=False)


from django import forms
from django.utils.translation import ugettext_lazy as _

from categories.models import Category


class StockReportForm(forms.Form):

    category = forms.ModelChoiceField(
        empty_label=_('Choose category'),
        required=False,
        queryset=Category.objects.all())

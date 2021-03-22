
from django.db.models import F
from django.utils.translation import ugettext_lazy as _
from django.contrib.admin.views.decorators import staff_member_required

from stock.forms import StockReportForm
from apps.products.models import Product

try:
    from apps.stock import render
except ImportError:
    from basement.admin import render


@staff_member_required
def get_stock_report(request):
    return _get_report(
        request,
        Product.objects.active(),
        _('Products in stock')
    )


@staff_member_required
def get_min_stock_report(request):
    return _get_report(
        request,
        Product.objects.active().filter(stock__lte=F('min_stock')),
        _('Min stock report')
    )


def _get_report(request, queryset, report_name):

    form = StockReportForm(request.GET or None)

    ids = None
    categories = None

    if form.is_valid():
        ids = form.cleaned_data['ids']
        categories = form.cleaned_data['categories']

    if categories:
        queryset = queryset.filter(category__in=categories)

    if ids:
        queryset = queryset.filter(id__in=ids.split(','))

    return render(request, 'stock/report.html', {
        'report_name': report_name,
        'products': queryset,
        'form': form,
        'totals': {
            'qty': sum([p.stock for p in queryset]),
            'grand_total': sum([p.subtotal for p in queryset])
        }
    })

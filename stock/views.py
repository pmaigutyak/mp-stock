
from django.db.models import F
from django.apps import apps
from django.contrib.admin import site
from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required


@staff_member_required
def get_min_stock_report(request):

    context = site.each_context(request)

    context['products'] = apps.get_model('products', 'Product').objects.filter(
        stock__lt=F('min_stock'))

    return render(request, 'stock/min-stock-report.html', context)


from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns

from stock import views


app_name = 'stock'


urlpatterns = [

    path('stock-report/', views.get_stock_report,
         name='stock-report'),

    path('min-stock-report/', views.get_min_stock_report,
         name='min-stock-report')

]


app_urls = i18n_patterns(
    path('stock/', include((urlpatterns, app_name)))
)

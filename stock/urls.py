
from django.urls import path

from stock import views


app_name = 'stock'


urlpatterns = [

    path('min-stock-report/', views.get_min_stock_report,
         name='min-stock-report')

]

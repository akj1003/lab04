from django.urls import path
from .views import index, calc_tax,tax_rate_view

urlpatterns = [
    path('', index, name='index'),
    path('<str:number>', calc_tax, name="calc_tax"),
    path('taxrate/', tax_rate_view, name="tax_rate")

]
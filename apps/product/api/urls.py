from django.urls import path
from .views.general_view import MeasureUnitList,CategoryProductList,IndicatorList

urlpatterns=[
    path('measure_unit/',MeasureUnitList.as_view(),name='measure_unit'),
    path('category-product_list/',CategoryProductList.as_view(),name='category-product_list'),
    path('indicator_list/',IndicatorList.as_view(),name='indicator_list')
]
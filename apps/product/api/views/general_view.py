from rest_framework import generics
#serializer
from apps.product.api.serializer.general_serializer import (
    MeaMeasureUnitSerializer,CategoryProductSerializer,IndicatorSerializer
)
#Models
from apps.product.models import MeasureUnit,CategoryProduct,Indicator

class MeasureUnitList(generics.ListAPIView):
    serializer_class=MeaMeasureUnitSerializer

    def get_queryset(self):
        data=MeasureUnit.objects.filter(state=True)
        return data

class CategoryProductList(generics.ListAPIView):
    serializer_class=CategoryProductSerializer
    def get_queryset(self):
        data=CategoryProduct.objects.filter(state=True)
        return data

class IndicatorList(generics.ListAPIView):
    serializer_class=IndicatorSerializer
    def get_queryset(self):
        data=Indicator.objects.filter(state=True)
        return data







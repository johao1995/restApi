from apps.product.models import(
    MeasureUnit,CategoryProduct,Indicator
)
from rest_framework import serializers

class MeaMeasureUnitSerializer(serializers.ModelSerializer):
    class Meta:
        model=MeasureUnit
        exclude=('state','created_date','update_date','delete_date')

class CategoryProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryProduct
        exclude = ('state','created_date','update_date','delete_date')

class IndicatorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Indicator
        exclude=('state','created_date','update_date','delete_date')
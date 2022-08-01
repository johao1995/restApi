from django.db import models
from apps.base.models import BaseModel

class MeasureUnit(BaseModel):
    description=models.CharField('Descripcion',max_length=50,blank=True,null=False,unique=True)


    class Meta:
        verbose_name='Unidad de Medida'
        verbose_name_plural='Unidades de Medida'
    

    def __str__(self):
        return self.description


class CategoryProduct(BaseModel):
    description=models.CharField('Descripcion',max_length=50,blank=False,null=False,unique=True)
    measure_unit=models.ForeignKey(MeasureUnit,on_delete=models.CASCADE,verbose_name='Unidad de Medida')

    class Meta:
        verbose_name='Categoria de Producto'
        verbose_name_plural='Categoria de Productos'
    
    def __str__(self):
        return self.description


class Indicator(BaseModel):
    descount_value=models.PositiveSmallIntegerField(default=0)#descuento
    category_product=models.ForeignKey(CategoryProduct,on_delete=models.CASCADE,verbose_name='Indicador de Categoria')

    class Meta:
        verbose_name='Indicador de Oferta'
        verbose_name_plural='Indicadores de Ofertas'
    
    def __str__(self):
        return f'Oferta de la categoria {self.category_product} : {self.descount_value}'


class Product(BaseModel):
    name=models.CharField('Nombre de Producto',max_length=150,blank=False,null=False,unique=True)
    description=models.TextField('Descripcion de Producto',blank=False,null=False)
    image_product=models.ImageField('Imagen del Producto',upload_to='products/',blank=True,null=True)

    class Meta:
        verbose_name='Producto'
        verbose_name_plural='Productos'
    
    def __str__(self):
        return self.name





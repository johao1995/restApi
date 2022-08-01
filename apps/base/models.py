from abc import abstractmethod
from xml.parsers.expat import model
from django.db import models

class BaseModel(models.Model):
    id=models.AutoField(primary_key=True)
    state=models.BooleanField('Estado',default=True)
    created_date=models.DateField('Fecha de Creacion',auto_now=False,auto_now_add=True)
    update_date=models.DateField('Fecha de Modificacion',auto_now=True,auto_now_add=False)
    delete_date=models.DateField('Fecha de Eliminacion',auto_now=True,auto_now_add=False)

    class Meta:
        abstract=True
        verbose_name='Modelo Base'
        verbose_name_plural='BaseModels'



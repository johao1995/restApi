# Generated by Django 4.0.6 on 2022-08-01 14:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryProduct',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
                ('created_date', models.DateField(auto_now_add=True, verbose_name='Fecha de Creacion')),
                ('update_date', models.DateField(auto_now=True, verbose_name='Fecha de Modificacion')),
                ('delete_date', models.DateField(auto_now=True, verbose_name='Fecha de Eliminacion')),
                ('description', models.CharField(max_length=50, unique=True, verbose_name='Descripcion')),
            ],
            options={
                'verbose_name': 'Categoria de Producto',
                'verbose_name_plural': 'Categoria de Productos',
            },
        ),
        migrations.CreateModel(
            name='MeasureUnit',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
                ('created_date', models.DateField(auto_now_add=True, verbose_name='Fecha de Creacion')),
                ('update_date', models.DateField(auto_now=True, verbose_name='Fecha de Modificacion')),
                ('delete_date', models.DateField(auto_now=True, verbose_name='Fecha de Eliminacion')),
                ('description', models.CharField(blank=True, max_length=50, unique=True, verbose_name='Descripcion')),
            ],
            options={
                'verbose_name': 'Unidad de Medida',
                'verbose_name_plural': 'Unidades de Medida',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
                ('created_date', models.DateField(auto_now_add=True, verbose_name='Fecha de Creacion')),
                ('update_date', models.DateField(auto_now=True, verbose_name='Fecha de Modificacion')),
                ('delete_date', models.DateField(auto_now=True, verbose_name='Fecha de Eliminacion')),
                ('name', models.CharField(max_length=150, unique=True, verbose_name='Nombre de Producto')),
                ('description', models.TextField(verbose_name='Descripcion de Producto')),
                ('image_product', models.ImageField(blank=True, null=True, upload_to='products/', verbose_name='Imagen del Producto')),
            ],
            options={
                'verbose_name': 'Producto',
                'verbose_name_plural': 'Productos',
            },
        ),
        migrations.CreateModel(
            name='Indicator',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
                ('created_date', models.DateField(auto_now_add=True, verbose_name='Fecha de Creacion')),
                ('update_date', models.DateField(auto_now=True, verbose_name='Fecha de Modificacion')),
                ('delete_date', models.DateField(auto_now=True, verbose_name='Fecha de Eliminacion')),
                ('descount_value', models.PositiveSmallIntegerField(default=0)),
                ('category_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.categoryproduct', verbose_name='Indicador de Categoria')),
            ],
            options={
                'verbose_name': 'Indicador de Oferta',
                'verbose_name_plural': 'Indicadores de Ofertas',
            },
        ),
        migrations.AddField(
            model_name='categoryproduct',
            name='measure_unit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.measureunit', verbose_name='Unidad de Medida'),
        ),
    ]

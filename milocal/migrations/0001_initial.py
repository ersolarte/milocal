# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('referencia', models.CharField(max_length=100)),
                ('precio', models.FloatField()),
                ('cantidad', models.IntegerField(default=0)),
                ('disponible', models.CharField(max_length=2, choices=[(b'SI', b'SI'), (b'NO', b'NO')])),
                ('descripcion', models.TextField()),
                ('descuento', models.IntegerField(default=0)),
                ('imagen', models.ImageField(upload_to=b'photos')),
                ('idmarca', models.ForeignKey(to='milocal.Marca')),
            ],
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('idcliente', models.IntegerField(default=0)),
                ('nombrecliente', models.CharField(max_length=100)),
                ('cantidad', models.IntegerField(default=0)),
                ('valor_a_pagar', models.FloatField()),
                ('idproducto', models.ForeignKey(to='milocal.Producto')),
            ],
        ),
    ]

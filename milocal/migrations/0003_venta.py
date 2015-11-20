# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('milocal', '0002_auto_20151112_2059'),
    ]

    operations = [
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

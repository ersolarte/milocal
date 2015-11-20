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
                ('disponible', models.CharField(max_length=1, choices=[(b'S', b'SI'), (b'N', b'NO')])),
                ('descripcion', models.TextField()),
                ('descuento', models.IntegerField(default=0)),
                ('idmarca', models.ForeignKey(to='milocal.Marca')),
            ],
        ),
    ]

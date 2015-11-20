# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('milocal', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='disponible',
            field=models.CharField(max_length=2, choices=[(b'SI', b'SI'), (b'NO', b'NO')]),
        ),
    ]

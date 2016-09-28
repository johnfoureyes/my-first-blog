# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='Oggetto',
            field=models.CharField(max_length=100, default='vuoto'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='sesso',
            field=models.CharField(max_length=1, default='vuoto'),
            preserve_default=False,
        ),
    ]

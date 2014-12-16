# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notifier', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sentnotification',
            name='success',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]

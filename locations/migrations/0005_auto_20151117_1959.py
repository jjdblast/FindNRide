# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0004_auto_20151117_0720'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menuitems',
            name='restaurant',
        ),
        migrations.DeleteModel(
            name='MenuItems',
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20151130_0341'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='rating',
            field=models.IntegerField(default=0, choices=[(0, b'None'), (1, b'*'), (2, b'**'), (3, b'***'), (4, b'****'), (5, b'*****')]),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20151130_0121'),
    ]

    operations = [
        migrations.AddField(
            model_name='vote',
            name='note',
            field=models.ForeignKey(blank=True, to='core.Note', null=True),
        ),
        migrations.AlterField(
            model_name='vote',
            name='course',
            field=models.ForeignKey(blank=True, to='core.Course', null=True),
        ),
    ]

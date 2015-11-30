# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0002_auto_20151128_1703'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.RenameModel(
            old_name='Class',
            new_name='Course',
        ),
        migrations.RenameField(
            model_name='note',
            old_name='Class',
            new_name='course',
        ),
        migrations.AddField(
            model_name='vote',
            name='course',
            field=models.ForeignKey(to='core.Course'),
        ),
        migrations.AddField(
            model_name='vote',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]

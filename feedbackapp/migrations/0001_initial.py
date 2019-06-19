# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='feedbackdata',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=100)),
                ('rating', models.IntegerField()),
                ('date', models.DateTimeField(max_length=100)),
                ('feedback', models.TextField(max_length=100)),
            ],
        ),
    ]

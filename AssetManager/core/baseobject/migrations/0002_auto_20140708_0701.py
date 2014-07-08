# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('baseobject', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='baseobject',
            name='type',
            field=models.CharField(max_length=256),
        ),
    ]

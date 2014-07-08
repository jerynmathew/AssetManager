# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('baseobject', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assets',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('baseobject.baseobject',),
        ),
    ]

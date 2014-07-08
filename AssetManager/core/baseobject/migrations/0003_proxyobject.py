# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('baseobject', '0002_auto_20140708_0701'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProxyObject',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('baseobject.baseobject',),
        ),
    ]

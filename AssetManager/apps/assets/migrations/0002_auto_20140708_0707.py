# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('baseobject', '0003_proxyobject'),
        ('assets', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Assets',
        ),
        migrations.CreateModel(
            name='Assets',
            fields=[
                ('baseobject_ptr', models.OneToOneField(primary_key=True, serialize=False, to='baseobject.BaseObject', auto_created=True)),
            ],
            options={
            },
            bases=('baseobject.proxyobject',),
        ),
    ]

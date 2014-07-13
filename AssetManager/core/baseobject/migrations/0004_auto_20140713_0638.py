# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('baseobject', '0003_proxyobject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='baseobject',
            name='attributes',
            field=jsonfield.fields.JSONField(blank=True),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_auto_20170115_1547'),
    ]

    operations = [
        migrations.DeleteModel(
            name='logentry',
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='logentry',
        ),
        migrations.RemoveField(
            model_name='monthjournal2',
            name='student',
        ),
        migrations.DeleteModel(
            name='MonthJournal2',
        ),
    ]

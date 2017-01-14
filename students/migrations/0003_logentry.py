# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_auto_20170115_0038'),
    ]

    operations = [
        migrations.CreateModel(
            name='logentry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('level', models.CharField(max_length=20)),
                ('asctime', models.DateTimeField(null=True)),
                ('module', models.CharField(max_length=100)),
                ('message', models.TextField()),
            ],
            options={
                'verbose_name': '\u041b\u043e\u0433 \u0416\u0443\u0440\u043d\u0430\u043b',
                'verbose_name_plural': '\u041b\u043e\u0433 \u0416\u0443\u0440\u043d\u0430\u043b\u0438',
            },
            bases=(models.Model,),
        ),
    ]

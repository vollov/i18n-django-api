# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PageTranslation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=150, db_index=True)),
                ('language', models.CharField(default=b'en', max_length=2, choices=[(b'en', b'English'), (b'zh', b'Chinese')])),
                ('page', models.ForeignKey(to='page.Page')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]

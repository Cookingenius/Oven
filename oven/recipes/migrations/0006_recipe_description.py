# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0005_auto_20140408_1952'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='description',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]

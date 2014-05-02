# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0006_recipe_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='step',
            name='picture',
        ),
        migrations.DeleteModel(
            name='Picture',
        ),
    ]

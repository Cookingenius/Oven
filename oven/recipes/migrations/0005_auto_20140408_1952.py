# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0004_auto_20140407_2059'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='title',
            new_name='name',
        ),
    ]

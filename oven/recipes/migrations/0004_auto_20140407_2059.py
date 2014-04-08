# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0003_auto_20140407_2054'),
    ]

    operations = [
        migrations.RenameField(
            model_name='step',
            old_name='number',
            new_name='order',
        ),
    ]

# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foods', '0004_auto_20140420_1449'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='unit_weight',
            field=models.IntegerField(null=True, help_text='Average weight of a base unit (grams)', blank=True),
        ),
    ]

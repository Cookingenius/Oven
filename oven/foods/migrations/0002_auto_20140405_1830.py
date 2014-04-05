# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foods', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='unitary',
            field=models.BooleanField(default=False, help_text='True if the macros are for a base unit'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='food',
            name='category',
            field=models.CharField(blank=True, max_length=255, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='food',
            name='unit_weight',
            field=models.FloatField(blank=True, help_text='Average weight of a base unit (grams)', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='food',
            name='name',
            field=models.CharField(unique=True, max_length=255),
        ),
    ]

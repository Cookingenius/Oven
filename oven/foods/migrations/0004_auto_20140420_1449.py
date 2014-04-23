# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foods', '0003_auto_20140419_1703'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='potassium',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='food',
            name='magnesium',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='food',
            name='vitamin_a',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='food',
            name='calcium',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='food',
            name='cholesterol',
            field=models.IntegerField(default=0),
        ),
    ]

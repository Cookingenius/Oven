# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0007_auto_20140427_1119'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='subtitle',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]

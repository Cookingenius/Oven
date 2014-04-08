# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_step'),
    ]

    operations = [
        migrations.AlterField(
            model_name='step',
            name='picture',
            field=models.ForeignKey(null=True, to_field='id', to='recipes.Picture', blank=True),
        ),
    ]

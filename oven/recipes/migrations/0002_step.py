# encoding: utf8
from django.db import models, migrations
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Step',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('created', model_utils.fields.AutoCreatedField(editable=False, verbose_name='created', default=django.utils.timezone.now)),
                ('modified', model_utils.fields.AutoLastModifiedField(editable=False, verbose_name='modified', default=django.utils.timezone.now)),
                ('recipe', models.ForeignKey(to='recipes.Recipe', to_field='id')),
                ('text', models.TextField()),
                ('number', models.IntegerField()),
                ('picture', models.ForeignKey(to_field='id', blank=True, to='recipes.Picture')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]

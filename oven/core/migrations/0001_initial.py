# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('url', models.CharField(max_length=700)),
                ('content_type', models.ForeignKey(to_field='id', to='contenttypes.ContentType')),
                ('object_id', models.PositiveIntegerField()),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]

# encoding: utf8
from django.db import models, migrations
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('foods', '0002_auto_20140405_1830'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('created', model_utils.fields.AutoCreatedField(editable=False, default=django.utils.timezone.now, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(editable=False, default=django.utils.timezone.now, verbose_name='modified')),
                ('name', models.CharField(max_length=255, unique=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='food',
            name='fiber',
            field=models.FloatField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='food',
            name='vitamin_a',
            field=models.FloatField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='food',
            name='potassium',
            field=models.FloatField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='food',
            name='calcium',
            field=models.FloatField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='food',
            name='fat_mono',
            field=models.FloatField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='food',
            name='fat_poly',
            field=models.FloatField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='food',
            name='vitamin_c',
            field=models.FloatField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='food',
            name='iron',
            field=models.FloatField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='food',
            name='sodium',
            field=models.FloatField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='food',
            name='sugar',
            field=models.FloatField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='food',
            name='fat_saturated',
            field=models.FloatField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='food',
            name='cholesterol',
            field=models.FloatField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='food',
            name='magnesium',
            field=models.FloatField(default=0),
            preserve_default=True,
        ),
        migrations.RemoveField(
            model_name='food',
            name='unitary',
        ),
        migrations.AlterField(
            model_name='food',
            name='carbs',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='food',
            name='category',
            field=models.ForeignKey(to_field='id', to='foods.Category'),
        ),
        migrations.AlterField(
            model_name='food',
            name='proteins',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='food',
            name='fat',
            field=models.FloatField(default=0),
        ),
    ]

# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Food'
        db.create_table('foods_food', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('proteins', self.gf('django.db.models.fields.FloatField')()),
            ('carbs', self.gf('django.db.models.fields.FloatField')()),
            ('fat', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal('foods', ['Food'])


    def backwards(self, orm):
        # Deleting model 'Food'
        db.delete_table('foods_food')


    models = {
        'foods.food': {
            'Meta': {'object_name': 'Food'},
            'carbs': ('django.db.models.fields.FloatField', [], {}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'fat': ('django.db.models.fields.FloatField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'proteins': ('django.db.models.fields.FloatField', [], {})
        }
    }

    complete_apps = ['foods']
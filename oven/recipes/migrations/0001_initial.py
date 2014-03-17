# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Recipe'
        db.create_table('recipes_recipe', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('approved', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('cooking_time', self.gf('django.db.models.fields.IntegerField')()),
            ('preparation_time', self.gf('django.db.models.fields.IntegerField')()),
            ('number_servings', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('recipes', ['Recipe'])

        # Adding model 'Picture'
        db.create_table('recipes_picture', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('recipe', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['recipes.Recipe'])),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=700)),
        ))
        db.send_create_signal('recipes', ['Picture'])

        # Adding model 'Ingredient'
        db.create_table('recipes_ingredient', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('recipe', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['recipes.Recipe'])),
            ('food', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['foods.Food'])),
            ('order', self.gf('django.db.models.fields.IntegerField')()),
            ('quantity', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal('recipes', ['Ingredient'])

        # Adding model 'Step'
        db.create_table('recipes_step', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('recipe', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['recipes.Recipe'])),
            ('text', self.gf('django.db.models.fields.TextField')()),
            ('number', self.gf('django.db.models.fields.IntegerField')()),
            ('picture', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, to=orm['recipes.Picture'])),
        ))
        db.send_create_signal('recipes', ['Step'])


    def backwards(self, orm):
        # Deleting model 'Recipe'
        db.delete_table('recipes_recipe')

        # Deleting model 'Picture'
        db.delete_table('recipes_picture')

        # Deleting model 'Ingredient'
        db.delete_table('recipes_ingredient')

        # Deleting model 'Step'
        db.delete_table('recipes_step')


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
        },
        'recipes.ingredient': {
            'Meta': {'object_name': 'Ingredient'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'food': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['foods.Food']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'order': ('django.db.models.fields.IntegerField', [], {}),
            'quantity': ('django.db.models.fields.FloatField', [], {}),
            'recipe': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['recipes.Recipe']"})
        },
        'recipes.picture': {
            'Meta': {'object_name': 'Picture'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'recipe': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['recipes.Recipe']"}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '700'})
        },
        'recipes.recipe': {
            'Meta': {'object_name': 'Recipe'},
            'approved': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'cooking_time': ('django.db.models.fields.IntegerField', [], {}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'number_servings': ('django.db.models.fields.IntegerField', [], {}),
            'preparation_time': ('django.db.models.fields.IntegerField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'recipes.step': {
            'Meta': {'object_name': 'Step'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'number': ('django.db.models.fields.IntegerField', [], {}),
            'picture': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'to': "orm['recipes.Picture']"}),
            'recipe': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['recipes.Recipe']"}),
            'text': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['recipes']
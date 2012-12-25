# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'TestSet'
        db.create_table('scenario_testset', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
            ('test_date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('note', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal('scenario', ['TestSet'])


    def backwards(self, orm):
        # Deleting model 'TestSet'
        db.delete_table('scenario_testset')


    models = {
        'scenario.scenario': {
            'Meta': {'ordering': "['case_order']", 'object_name': 'Scenario'},
            'actual_result': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'case_order': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'expected_result': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'note': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'pre_requisite': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'purpose': ('django.db.models.fields.TextField', [], {}),
            'test_case': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'test_data': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'test_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'test_step': ('django.db.models.fields.TextField', [], {}),
            'tester_accepted': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'scenario.testset': {
            'Meta': {'object_name': 'TestSet'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'note': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'test_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['scenario']
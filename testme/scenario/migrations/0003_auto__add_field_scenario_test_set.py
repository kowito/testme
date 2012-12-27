# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Scenario.test_set'
        db.add_column('scenario_scenario', 'test_set',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['scenario.TestSet']),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Scenario.test_set'
        db.delete_column('scenario_scenario', 'test_set_id')


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
            'test_set': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['scenario.TestSet']"}),
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
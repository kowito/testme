# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import DataMigration
from django.db import models
from scenario.models import Scenario, TestSet

class Migration(DataMigration):

    def forwards(self, orm):
        test_set = TestSet.objects.get(id=1)
        for scenario in orm.Scenario.objects.all():
            print "\n\n\%s\n\n" % scenario
            scenario.test_set = test_set
            scenario.save()
        

    def backwards(self, orm):
        "Write your backwards methods here."
        raise RuntimeError("Cannot reverse this migration.")
        

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
    symmetrical = True

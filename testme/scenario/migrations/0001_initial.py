# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Scenario'
        db.create_table('scenario_scenario', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('test_case', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('purpose', self.gf('django.db.models.fields.TextField')()),
            ('pre_requisite', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('test_data', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('test_step', self.gf('django.db.models.fields.TextField')()),
            ('expected_result', self.gf('django.db.models.fields.TextField')()),
            ('actual_result', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('test_date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('tester_accepted', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('note', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('case_order', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal('scenario', ['Scenario'])


    def backwards(self, orm):
        # Deleting model 'Scenario'
        db.delete_table('scenario_scenario')


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
        }
    }

    complete_apps = ['scenario']
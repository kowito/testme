from django.contrib import admin
from testbuilder.scenario.models import Scenario

class ScenarioAdmin(admin.ModelAdmin):
    list_display = ('test_case_id','test_case', 'purpose')
    
    class Media:
    
        js = [
              '/static/grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
              '/static/grappelli/tinymce_setup/tinymce_setup.js',
              ]

admin.site.register(Scenario,ScenarioAdmin)
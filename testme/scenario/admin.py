from django.contrib import admin
from scenario.models import Scenario, TestSet


class TestSetAdmin(admin.ModelAdmin):
    list_display = ('name','test_date','note')
    prepopulated_fields = {"slug": ("name",)}
    
    
class ScenarioAdmin(admin.ModelAdmin):
    list_display = ('test_case_id','test_case', 'test_date','tester_accepted')
    
    class Media:
    
        js = [
              '/static/grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
              '/static/grappelli/tinymce_setup/tinymce_setup.js',
              ]

admin.site.register(TestSet,TestSetAdmin)
admin.site.register(Scenario,ScenarioAdmin)
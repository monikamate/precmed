from django.contrib import admin
from . import models

# Register your models here.

@admin.register(models.Sequence)
class SequenceAdmin(admin.ModelAdmin):
    list_display = ['id','sample_id','sequence_data_file']
    search_fields = ['sample_id']

@admin.register(models.Reference)
class ReferenceAdmin(admin.ModelAdmin):
    list_display = ['id','reference_id','reference_file']
    search_fields = ['reference_id']

@admin.register(models.AnalysisStatus)
class AnalysisStatusAdmin(admin.ModelAdmin):
    list_display = ['id','sequence','reference','status','result_file','created_at','updated_at']
    search_fields = ['status']
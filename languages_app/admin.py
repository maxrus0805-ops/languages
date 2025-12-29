from django.contrib import admin
from .models import ProgrammingLanguage

@admin.register(ProgrammingLanguage)
class ProgrammingLanguageAdmin(admin.ModelAdmin):
    list_display = ('name', 'year_created', 'is_popular')
    list_filter = ('is_popular', 'year_created')
    search_fields = ('name', 'main_usage')
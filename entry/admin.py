from django.contrib import admin
from .models import  Entry ,Journal
from import_export.admin import ImportExportModelAdmin

# Register your models here.

class JournalInLineAdmin(admin.TabularInline):
    model = Journal



@admin.register(Entry)
class EntryAdmin(ImportExportModelAdmin):
    list_display  = [f.name for f in Entry._meta.fields]
    inlines = [JournalInLineAdmin]
    class Meta:
        model =Entry



# @admin.register(Journal)
# class JournalAdmin(ImportExportModelAdmin):
#     list_display  = [f.name for f in Journal._meta.fields]
#     class Meta:
#         model = Journal



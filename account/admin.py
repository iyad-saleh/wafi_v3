from django.contrib import admin
from .models import Account_type, Main_account, Sub_account
from import_export.admin import ImportExportModelAdmin
from mptt.admin import MPTTModelAdmin
from mptt.admin import DraggableMPTTAdmin

@admin.register(Account_type)
class Account_typeAdmin(ImportExportModelAdmin):
    list_display  = [f.name for f in Account_type._meta.fields]


    class Meta:
        model =Account_type

# @admin.register(Main_account)
class Main_accountAdmin(MPTTModelAdmin):
    list_display  = [f.name for f in Main_account._meta.fields]


    class Meta:
        model =Main_account

admin.site.register(Main_account, Main_accountAdmin)


# @admin.register(Sub_account)
class Sub_accountAdmin(ImportExportModelAdmin):
    list_display  = [f.name for f in Sub_account._meta.fields]


    class Meta:
        model =Sub_account

admin.site.register(Sub_account, Sub_accountAdmin)


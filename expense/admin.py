from django.contrib import admin
from .models import Expense
from import_export.admin import ImportExportModelAdmin
@admin.register(Expense)
class ExpenseAdmin(ImportExportModelAdmin):
    list_display = ('id',
                'account',

                'created_at',
                'author','is_deleted',
                )
    list_filter = (

                'author','is_deleted',
                )
    def get_queryset(self, request):
        qs = self.model._default_manager.all_with_deleted()
        ordering =self.ordering or ()
        if ordering:
            qs = qs.order_by(*ordering)
        return qs
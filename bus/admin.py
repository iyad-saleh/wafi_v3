from django.contrib import admin
from .models import Bus#, Driver

@admin.register(Bus)
class BusAdmin(admin.ModelAdmin):
    list_display = ( 'id',
                'account',

                'customer',
                'start_date',
                'busType',
                'busNumber',
                'seats',
                'memo',
                'create_at',
                'author',
                )
    list_filter = (

                'customer',
                'busType',
                'seats',
                'update_at',
                'author',
                )

# @admin.register(Driver)
# class DriverAdmin(admin.ModelAdmin):
#     list_display = (
#                 'name',
#                 'status',
#
#                 'phoneNumber',
#                 'start_date',
#                 'create_at',
#                 'author',
#                 )
#     list_filter = (
#
#                 )

from django.urls import path

from .views import *


urlpatterns = [
    path('', account_type_index,name='account_type_index'),
    path('account_type/', account_type_list, name='account_type_list'),
    path('add_account_type/add', add_account_type, name='add_account_type'),
    path('accounts/<int:pk>/edit', edit_account_type, name='edit_account_type'),
    path('accounts/<int:pk>/remove', remove_account_type, name='remove_account_type'),

    path('main_account/<int:pk>/', main_account_list, name='main_account_list'),
    path('add_main_account/<int:pk>/add', add_main_account, name='add_main_account'),
    path('main_account_details/<int:pk>/', main_account_details, name='main_account_details'),
    path('edit_main_account/<int:pk>/edit', edit_main_account, name='edit_main_account'),
    path('remove_main_account/<int:pk>/remove', remove_main_account, name='remove_main_account'),


    path('query_sub_account/', query_sub_account, name='query_sub_account'),
    path('search_sub_account/', search_sub_account, name='search_sub_account'),
    path('sub_account_list/<int:pk>/', sub_account_list, name='sub_account_list'),
    path('add_sub_account/<int:pk>/add', add_sub_account, name='add_sub_account'),
    path('edit_sub_account/<int:pk>/edit', edit_sub_account, name='edit_sub_account'),
    path('remove_sub_account/<int:pk>/remove', remove_sub_account, name='remove_sub_account'),
]

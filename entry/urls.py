from django.urls import path

from .views import *


urlpatterns = [
    path('', index,name='entry_index'),
    path('entry/', entry_list, name='entry_list'),
    path('entry/add', add_entry, name='add_entry'),
    # path('entry/<int:pk>/remove', remove_entry, name='remove_entry'),
    path('entry/<int:pk>/detail', entry_detail, name='entry_detail'),


    path('create_journal_form/', create_journal_form,name='create_journal_form'),

    path('journal', journal_index,name='journal_index'),
    path('journals/<int:pk>/', journal_list, name='journal_list'),
    # path('journals/add', add_journal, name='add_journal'),
    # path('journals/<int:pk>/remove', remove_journal, name='remove_journal'),
    # path('journals/<int:pk>/edit', edit_journal, name='edit_journal'),
]

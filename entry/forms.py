from django import forms
from international.models import Coin
from .models import Entry, Journal
from django.forms import ModelForm
from django.forms.models import (
    inlineformset_factory,
    formset_factory,
    modelform_factory,
    modelformset_factory
)
from django.forms import ModelForm, DateInput
from django.utils  import timezone
from django.contrib.admin.widgets import AdminDateWidget
from django.forms.fields import DateField
from account.models import Sub_account
from django.db.models import Q

from django.urls import reverse_lazy

class EntryForm(forms.ModelForm):

    class Meta:
        model = Entry
        fields = ['date','narration']
        widgets = {
            'date': forms.DateInput( attrs={'type': 'date'}),
        }



class JournalForm(forms.ModelForm):

    class Meta:
        model = Journal
        fields = ['account','amount','direction','coin','coin_ex','narration']
        # widgets = {
        # 'coin': forms.TextInput(attrs={
        #         'hx-get': reverse_lazy('check-username'),
        #         'hx-target': '#div_id_username',
        #         'hx-trigger': 'keyup[target.value.length > 3]'
        #     })}


JournalFormSet = inlineformset_factory(Entry,
                                       Journal,
                                        form=JournalForm,
                                        # min_num=2,  # minimum number of forms that must be filled in
                                        extra=2,  # number of empty forms to display
                                        can_delete=False )
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
from djangoformsetjs.utils import formset_media_js



class EntryForm(forms.ModelForm):

    class Meta:
        model = Entry
        fields = ['date','narration']
        widgets = {
            'date': forms.DateInput( attrs={'type': 'date'}),
        }



class JournalForm(forms.ModelForm):
    # account= forms.ModelChoiceField(queryset=Sub_account.objects.all(),to_field_name="name")
    # iquery = Sub_account.objects.all()
    # iquery_choices = {(acc, acc) for acc in iquery}
    # account= forms.ChoiceField( choices=iquery_choices)
    class Media(object):
        js = formset_media_js + (
            # Other form media here
        )
    class Meta:
        model = Journal
        fields = ['account','amount','direction','coin','narration']

            # 'direction':
            # 'coin':
    # def clean(self):
    #     _mutable = self.data._mutable
    #     self.data._mutable = True
    #     for item in self.data:
    #         if 'account'  in item:
    #             if str(self.data[item]).isnumeric():
    #                 continue
    #             data =self.data[item].split('-')
    #             code =data[0]
    #             name = data[1]
    #             acc = Sub_account.objects.filter(Q(name=name)|Q(code=code)).first()
    #             if acc:
    #                 self.data[item] = str(acc.id)
    #     # set mutable flag back
    #     self.data._mutable = _mutable
    #     cleaned_data=super(JournalForm, self).clean()
    #     print('cleaned_data', cleaned_data)
    #     print('self.data', self.data)
    #     return cleaned_data

JournalFormSet = inlineformset_factory(Entry,
                                       Journal,
                                        form=JournalForm,
                                        # min_num=2,  # minimum number of forms that must be filled in
                                        extra=2,  # number of empty forms to display
                                        can_delete=False )
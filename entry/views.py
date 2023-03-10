from django.shortcuts import render
from .forms import EntryForm, JournalForm, JournalFormSet
from entry.models import Entry, Journal
from account.models import Sub_account
from django.http import HttpResponse
import json
from django.contrib.auth.decorators import login_required
from international.models import Coin
import math
# from django_htmx.http import trigger_client_event
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from datetime import datetime
from django.forms.models import    inlineformset_factory
@login_required
def index(request):

    return render(request, 'entry/index.html')


def entry_list(request):
    search = request.GET.get('search','')
    filter_all = request.GET.get('all','')
    filter_narration = request.GET.get('narration','')
    filter_id = request.GET.get('id','')
    daterange = request.GET.get('daterange','')
    Checkboxdaterange = request.GET.get('Checkboxdaterange','')
    entry_list = Entry.objects.all()
    if  search:
        # print(request.GET)
        if filter_all:
            entry_list = entry_list.filter(Q(narration__icontains=search) | Q(id__icontains=search)).distinct()
            print('filter_all',entry_list)
        elif  filter_narration:
            entry_list = entry_list.filter(narration__icontains=search).distinct()
            print('filter_narration',entry_list)
        elif filter_id:
            entry_list = entry_list.filter(id__icontains=filter_id).distinct()
            print('filter_id',entry_list)
        if Checkboxdaterange:#12/06/2022 - 12/20/2022
            print('Checkboxdaterange')
            raw_start =daterange.split(' - ')[0].strip()
            raw_end = daterange.split(' - ')[1].strip()
            print(raw_start,raw_end)
            start = datetime.strptime(raw_start, '%m/%d/%Y').date()
            end =    datetime.strptime(raw_end, '%m/%d/%Y').date()
            print(type(start),start)
            print(type(end),end)
            entry_list = entry_list.filter(Q(date__gte=start) & Q(date__lte=end)).distinct()

    paginator = Paginator(entry_list, 10)
    page = request.GET.get('page', 1)
    try:
        entries = paginator.page(page)
    except PageNotAnInteger:
        entries = paginator.page(1)
    except EmptyPage:
        entries = paginator.page(paginator.num_pages)
    # print('entries',[e for  e in entries])
    return render(request, 'entry/entry_list.html', {
        'entries':entries,'page': page
    })






def balance_entry(j_form, balance=True,msg=''):
    # print('balance_entrybalance_entrybalance_entry')
    temp ={}#amount  direction   coin
    for j in j_form.cleaned_data:
        # print(j['account'].coin.all)
        if not  j['coin'] in j['account'].coin.all():
            msg =str( j['account'].name)+'/  curruncy is not same  / '+  str(j['coin'].short_title)
            balance=False
            return (balance, msg)
        if j['coin'].short_title in temp:
            temp[j['coin'].short_title] += float(j['amount'])*float(j['direction'])
        else:
            temp[j['coin'].short_title]=float(j['amount'])*float(j['direction'])

    for item in temp:#temp {'sss': -77.0, 'syp': -26.0, 'USD': -16.0}
        if math.isclose(temp[item],0.0):
            pass
        else:
            msg +=str(item)+':'+str(temp[item])+'  //  '
            balance=False
    return (balance, msg)


# def account_balance(journal):#moved to receiver
#     account= journal.account
#     coin = journal.coin.short_title
#     if not type(account.credit) is dict:
#         account.credit={}
#     if not type(account.debit) is dict:
#         account.debit={}
#     if not type(account.balance) is dict:
#             account.balance={}

#     print('account.balance',type(account.balance),account.balance)
#     # print('account.credit',type(account.credit),account.credit)
#     # print('account.debit',type(account.debit),account.debit)
#     if journal.direction == '-1':# credit    //{'syp': 69}
#         # temp={}
#         if coin  in account.credit.keys():

#             account.credit[coin] =float(account.credit[coin])+float(journal.amount)
#         else:
#             account.credit[coin]=float(journal.amount)

#     else:
#         if coin  in account.debit.keys():
#             account.debit[coin] =float(account.debit[coin])+float(journal.amount)
#         else:
#             account.debit[coin]=float(journal.amount)

#     if not coin  in account.credit.keys():
#         account.credit[coin] = 0.0
#     if not coin  in account.debit.keys():
#         account.debit[coin] = 0.0

#     print('float(account.credit[coin])', float(account.credit[coin]))

#     account.balance[coin] = float(account.credit[coin])-float(account.debit[coin])
#     account.save()
#     print('credit',journal.account.credit )
#     print('debit',journal.account.debit )



def add_entry(request):
    balance = True
    msg=''

    if request.method == "POST":
        TOTAL_FORMS = request.POST.get('journal_set-TOTAL_FORMS')
        # print('TOTAL_FORMS' ,TOTAL_FORMS)
        e_form = EntryForm(request.POST)
        j_form = JournalFormSet(request.POST)
        # print('j_form', j_form)
        if e_form.is_valid() and j_form.is_valid():

            # print('j_form.cleaned_data  : ',j_form.cleaned_data)
            balance, msg = balance_entry(j_form,balance,msg)

            if not balance:
                # print("if not balance")
                return render(request, 'entry/entry_form.html', {
                        'e_form': e_form,'j_form':j_form,'balance':balance,'msg':msg ,'TOTAL_FORMS':TOTAL_FORMS })

            entry = e_form.save(commit=False)
            entry.author=request.user
            entry.save()
            journals = j_form.save(commit=False)
            for journal in journals:
                journal.entry=entry
                journal.author=request.user
                if not journal.narration:
                    journal.narration = entry.narration

                # account_balance(journal)
                journal.save()
            entry.balance=True
            # entry.save()
            return HttpResponse(
                status=204,
                headers={
                    'HX-Trigger': json.dumps({
                        "entryListChanged": None,
                        "showMessage": f"{entry.narration} Added."
                    })
                }
            )
        else:
            print('not is_valid')
            print(e_form.errors)
            print(j_form.errors)
            return render(request, 'entry/entry_form.html', {
        'e_form': e_form,'j_form':j_form ,'balance':balance,'TOTAL_FORMS':TOTAL_FORMS ,'msg':msg })



    else:
        e_form = EntryForm()
        j_form = JournalFormSet()

        TOTAL_FORMS= j_form.management_form.initial['TOTAL_FORMS']


        for form in j_form:
            form.initial['coin']= Coin.objects.filter(active=True).first()



    return render(request, 'entry/entry_form.html', {
        'e_form': e_form,'j_form':j_form,'balance':balance,'TOTAL_FORMS':TOTAL_FORMS

    })


def entry_detail(request,pk):
    entry = get_object_or_404(Entry,pk=pk)
    return render(request,'entry/entry_detail.html',{'entry':entry})


def reverse_entry(request,pk):
    balance = True
    msg=''
    entry = get_object_or_404(Entry,pk=pk)
    if request.method == "POST":
        TOTAL_FORMS = request.POST.get('journal_set-TOTAL_FORMS')
        # print('TOTAL_FORMS' ,TOTAL_FORMS)
        e_form = EntryForm(request.POST)
        # if not request.POST.get('narration'):
        #     e_form.fields['narration']=entry.narration +  '--REVERSE Entry--'
        j_form = JournalFormSet(request.POST)
        # print("e_form['narration']",)
        if e_form.is_valid() and j_form.is_valid():

            # print('j_form.cleaned_data  : ',j_form.cleaned_data)
            balance, msg = balance_entry(j_form,balance,msg)

            if not balance:
                # print("if not balance")
                return render(request, 'entry/entry_form.html', {
                        'e_form': e_form,'j_form':j_form,'balance':balance,'msg':msg ,'TOTAL_FORMS':TOTAL_FORMS })

            entry = e_form.save(commit=False)
            entry.author=request.user
            entry.save()
            journals = j_form.save(commit=False)
            for journal in journals:
                journal.entry=entry
                journal.author=request.user
                if not journal.narration:
                    journal.narration = entry.narration
                # account_balance(journal)
                journal.save()
            entry.balance=True
            entry.save()
            return HttpResponse(
                status=204,
                headers={
                    'HX-Trigger': json.dumps({
                        "entryListChanged": None,
                        "showMessage": f"{entry.id} Added."
                    })
                }
            )
        else:
            print('not is_valid')
            print(e_form.errors)
            print(j_form.errors)
            return render(request, 'entry/entry_form.html', {
        'e_form': e_form,'j_form':j_form ,'balance':balance,'TOTAL_FORMS':TOTAL_FORMS ,'msg':msg })



    else:
        e_form = EntryForm(instance=entry)
        # print(entry.narration)
        temp= '--REVERSE Entry--'
        try:
            e_form.initial['narration']= entry.narration+ temp
        except Exception as e:
            e_form.initial['narration']=temp + str(entry.id)

        initial=[]
        for journal in entry.journal_set.all():
            # print('journal.coin_ex',journal.coin_ex)
            temp=''
            try:
                temp = journal.narration +'--REVERSE--'
            except Exception as e:
                temp ='--REVERSE journal--'+ str(journal.id)

            initial.append(

                {'account' :journal.account,
                'amount':journal.amount,
                'coin':journal.coin,
                'coin_ex':journal.coin_ex,
                'direction':str(int(journal.direction)*-1),
                'narration':temp


             }
            )
            j_form =inlineformset_factory(Entry,
                                       Journal,
                                        form=JournalForm,
                                        # min_num=2,  # minimum number of forms that must be filled in
                                        extra=entry.journal_set.all().count(),  # number of empty forms to display
                                        can_delete=False )
        j_form = j_form(initial=initial)

        # j_form.management_form.initial['TOTAL_FORMS']= entry.journal_set.all().count()
        TOTAL_FORMS= entry.journal_set.all().count()


        # for form in j_form:

            # print(form)
        #     form.initial['coin']= Coin.objects.filter(active=True).first()


    print('TOTAL_FORMS',TOTAL_FORMS)
    return render(request, 'entry/entry_form.html', {
        'e_form': e_form,'j_form':j_form,'balance':balance,'TOTAL_FORMS':TOTAL_FORMS

    })




def remove_entry(request):
    pass


# def create_jouranl_btn(request):


def create_journal_form(request):
    TOTAL_FORMS = request.GET.get('journal_set-TOTAL_FORMS',2)
    form = JournalForm()

    # form.fields['customer'].queryset = Customer.objects.filter(client=True).filter(company=company)
    form.initial['coin']= Coin.objects.filter(active=True).first()
    context = {
        "form": form,
        'TOTAL_FORMS':int(TOTAL_FORMS)+1,
        'id':int(TOTAL_FORMS)
    }
    return render(request, "entry/create_journal.html", context)
    # response = render(request, "entry/create_journal.html", context)
    # trigger_client_event(response, 'create_journal', {'TOTAL_FORMS':int(TOTAL_FORMS)+1})
    # return response


def journal_index(request):
    if hasattr( request.user  ,'is_MANAGER' ) :
        return render(request, 'journal/index.html')
    return HttpResponse(
        status=403,
        headers={
            'HX-Trigger': json.dumps({

               "journalListChanged": None,
            })
        })

def journal_list(request,pk):
    entry = get_object_or_404(Entry,pk=pk)
    journals = Journal.objects.filter(entry=entry ).order_by('-id')
    return render(request, 'journal/journal_list.html', {
        'journals':journals
    })


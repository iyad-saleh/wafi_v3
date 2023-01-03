import json
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_POST
from django.shortcuts import get_object_or_404
from international.models import Coin
from account.forms import Account_typeForm,Main_accountForm,Sub_accountForm
from .models import Account_type, Main_account, Sub_account
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from entry.models import Journal
# from django.contrib.auth.decorators import user_passes_test
# is_MANAGER
# is_RESERVATION
# is_ACCOUNTANT
# is_CUSTOMER

@login_required
def account_type_index(request):

    return render(request, 'account_type/index.html')


@login_required
def account_type_list(request):

    accounts = Account_type.objects.all()
    return render(request, 'account_type/account_type_list.html', {
        'accounts':accounts
    })

@login_required
def add_account_type(request):
    code=''
    try:
        code=Account_type.objects.all().last().code
        if  code :
            code =  int(code)+1
        else :
            code = '1'
        code = 'last Nmber you can use :' +str(code)
    except Exception as e:
        print('Exception code',e)
    if request.method == "POST":
        form = Account_typeForm(request.POST)
        if form.is_valid():
            account = form.save()
            return HttpResponse(
                status=204,
                headers={
                    'HX-Trigger': json.dumps({
                        "accountListChanged": None,
                        "showMessage": f"{account.name} Added."
                    })
                }
            )
        else:
            return render(request, 'account_type/account_type_form.html', {
        'form': form

    })

    else:
        form = Account_typeForm()


    return render(request, 'account_type/account_type_form.html', {
        'form': form,'code':code

    })

@login_required
def edit_account_type(request, pk):
    account = get_object_or_404(Account_type, pk=pk)

    # print(account)
    if request.method == "POST":
        form = Account_typeForm(request.POST, instance=account)
        # print(request.POST['account_type'])
        # print(request.POST)
        if form.is_valid():
            account = form.save()
            return HttpResponse(
                status=204,
                headers={
                    'HX-Trigger': json.dumps({
                        "accountListChanged": None,
                        "showMessage": f"{account.name} updated."
                    })
                }
            )
        else:
            return render(request, 'account_type/account_type_form.html', {
        'form': form,

    })

    else:
        form = Account_typeForm(instance=account)


    return render(request, 'account_type/account_type_form.html', {
        'form': form,'account':account

    })

@login_required
@ require_POST
def remove_account_type(request, pk):
    account = get_object_or_404(Account_type, pk=pk)
    account.delete()
    return HttpResponse(
        status=204,
        headers={
            'HX-Trigger': json.dumps({
                "accountListChanged": None,
                "showMessage": f"{account.name} deleted."
            })
        })



@login_required
def main_account_list(request,pk):
    account_type = get_object_or_404(Account_type,pk=pk)
    main_accounts = account_type.Main_children.all()
    return render(request, 'main_account/main_account_list.html', {
        'account_type':account_type,'main_accounts':main_accounts
    })


@login_required
def main_account_details(request, pk):
    main_account = get_object_or_404(Main_account,pk=pk)
    return render(request, 'main_account/main_account_details.html', {
        'main_account':main_account
    })

@login_required
def add_main_account(request,pk):
    account_type = get_object_or_404(Account_type,pk=pk)

    if request.method == "POST":
        form = Main_accountForm(request.POST)
        if form.is_valid():
            account = form.save(commit=False)
            account.account_type = account_type
            if account.parent:
                account.code = str(account.parent.code)+ str(form.cleaned_data['code'])
            else :
                account.code = str(account_type.code)+ str(form.cleaned_data['code'])

            account.save()
            return HttpResponse(
                status=204,
                headers={
                    'HX-Trigger': json.dumps({
                        "accountListChanged": None,
                        "showMessage": f"{account.name} Added."
                    })
                }
            )
        else:
            return render(request, 'main_account/main_account_form.html', {
        'form': form,'account_type':account_type

    })

    else:

        form = Main_accountForm()
        form.fields['parent'].queryset = Main_account.objects.filter(account_type=account_type)

    return render(request, 'main_account/main_account_form.html', {
        'form': form,'account_type':account_type

    })


@login_required
def edit_main_account(request,pk):
    main_account = get_object_or_404(Main_account,pk=pk)
    account_type = main_account.account_type
    if request.method == "POST":
        form = Main_accountForm(request.POST, instance=main_account)
        if form.is_valid():
            main_account = form.save()

            main_account.save()
            return HttpResponse(
                status=204,
                headers={
                    'HX-Trigger': json.dumps({
                        "accountListChanged": None,
                        "showMessage": f"{main_account.name} updated."
                    })
                }
            )
        else:
            return render(request, 'main_account/main_account_form.html', {
        'form': form,'account_type':account_type

    })

    else:
        form = Main_accountForm(instance=main_account)


    return render(request, 'main_account/main_account_form.html', {
        'form': form,'account_type':account_type,"main_account":main_account

    })


@login_required
@ require_POST
def remove_main_account(request, pk):
    account = get_object_or_404(Main_account, pk=pk)
    account.delete()
    return HttpResponse(
        status=204,
        headers={
            'HX-Trigger': json.dumps({
                "accountListChanged": None,
                "showMessage": f"{account.name} deleted."
            })
        })


@login_required
def sub_account_list(request,pk):
    main_account = get_object_or_404(Main_account,pk=pk)
    # total_debit ={}#amount  direction   coin
    # total_credit ={}#amount  direction   coin
    # total_balance ={}#amount  direction   coin
    # for account in main_account.sub_account_set.all():
    #     journals_list = Journal.objects.filter(account=account)
    #     # print(journals_list)
    #     for j in journals_list:
    #         if j.direction=='1': #('1','debit')  ('-1','credit')

    #             total_debit[j.coin.short_title] += float(j.amount)
    #         else :
    #             total_credit[j.coin.short_title] += float(j.amount)

            # if j.coin.short_title in total_balance:
            #     total_balance[j.coin.short_title] += float(j.amount)*float(j.direction)
            # else:
            #     total_balance[j.coin.short_title]=float(j.amount)*float(j.direction)



    return  render(request, 'sub_account/sub_account_list.html', {
        'main_account':main_account
    })

def add_coin_Main(main_account,coin):
    main_account = get_object_or_404(Main_account,pk=main_account.id)
    if not coin in main_account.debit:
        main_account.debit[coin]=float(0)
    if not coin in main_account.credit:
        main_account.credit[coin]=float(0)
    if not  coin in main_account.balance:
        main_account.balance[coin]=float(0)
    main_account.save()
    if main_account.parent:
        add_coin_Main(main_account.parent,coin)
    else:
        account_type  = get_object_or_404(Account_type,pk=main_account.account_type.id)
        if not coin in account_type.debit:
            account_type.debit[coin]=float(0)
        if not coin in account_type.credit:
            account_type.credit[coin]=float(0)
        if not  coin in account_type.balance:
            account_type.balance[coin]=float(0)
        account_type.save()




@login_required
def add_sub_account(request,pk):
    main_account = get_object_or_404(Main_account,pk=pk)
    account_type =main_account.account_type

    if request.method == "POST":
        form = Sub_accountForm(request.POST)
        if form.is_valid():
            sub_account = form.save(commit=False)
            sub_account.main_account= main_account
            sub_account.author=request.user
            sub_account.save()
            coins =form.cleaned_data['coin']
            for coin in coins:
                sub_account.coin.add(coin)
                sub_account.debit[coin.short_title]=float(0)
                sub_account.credit[coin.short_title]=float(0)
                sub_account.balance[coin.short_title]=float(0)

                add_coin_Main(main_account,coin.short_title)
                main_account.save()
                sub_account.save()

            return HttpResponse(
                status=204,
                headers={
                    'HX-Trigger': json.dumps({
                        "sub_accountListChanged": None,
                        "accountListChanged": None,
                        "showMessage": f"{sub_account.name} Added."
                    })
                }
            )
        else:
            return render(request, 'sub_account/sub_account_form.html', {
        'form': form,'account_type':account_type ,'main_account':main_account })



    else:
        form = Sub_accountForm(initial={'coin': Coin.objects.filter(active=True).first()})


    return render(request, 'sub_account/sub_account_form.html', {
        'form': form,'account_type':account_type,'main_account':main_account

    })

@login_required
def edit_sub_account(request,pk):
    sub_account = get_object_or_404(Sub_account,pk=pk)
    main_account = sub_account.main_account
    account_type =main_account.account_type

    if request.method == "POST":
        form = Sub_accountForm(request.POST, instance=sub_account)
        if form.is_valid():
            sub_account = form.save(commit=False)
            sub_account.main_account= main_account
            sub_account.author=request.user
            sub_account.save()
            sub_account.coin.clear()
            coins =form.cleaned_data['coin']
            for coin in coins:
                sub_account.coin.add(coin)
            return HttpResponse(
                status=204,
                headers={
                    'HX-Trigger': json.dumps({
                        "sub_accountListChanged": None,
                        "showMessage": f"{sub_account.name} updated."
                    })
                }
            )
        else:
            return render(request, 'sub_account/sub_account_form.html', {
        'form': form,'account_type':account_type ,'main_account':main_account })



    else:
        form = Sub_accountForm(instance=sub_account)


    return render(request, 'sub_account/sub_account_form.html', {
        'form': form,'account_type':account_type,'main_account':main_account,'sub_account':sub_account

    })

@login_required
def remove_sub_account(request,pk):
    account = get_object_or_404(Sub_account, pk=pk)
    account.delete()
    return HttpResponse(
        status=204,
        headers={
            'HX-Trigger': json.dumps({
                "sub_accountListChanged": None,
                "showMessage": f"{account.name} deleted."
            })
        })


def sub_account(request):
    accounts = Sub_account.objects.all()
    return render(request, 'sub_account/sub_accounts.html',{'accounts':accounts})


# def query_sub_account(request):
#     # print('request.GET', request.GET)
#     if request.GET.get('name') and   request.GET.get('code') :
#         name = request.GET.get('name')
#         code = request.GET.get('code')
#         hidden_id = request.GET.get('hidden_id')
#         sub_account= Sub_account.objects.filter(Q(name=name)|Q(code=code)).first()
#         print('name', name)
#         print('code', code)
#     return render(request, 'sub_account/hidden_sub_account.html',
#         {'sub_account':sub_account,'hidden_id':hidden_id}
#     )


# def search_sub_account(request):
#     search_text=None
#     hidden_id = request.GET.get('hidden_id')
#     search_text = request.GET.get('journal_set-'+str(hidden_id)+'-account--')
#     if search_text:
#         sub_accounts= Sub_account.objects.filter(Q(name__icontains=search_text)|Q(code__icontains=search_text)).distinct().order_by('id')
#     else:
#         sub_accounts = Sub_account.objects.all()
#         print('no search_text')

#     return render(request, 'sub_account/search_sub_account.html',
#         {'sub_accounts':sub_accounts,'hidden_id':hidden_id}
#     )


@login_required
def sub_account_journal(request,pk):
    rows = request.GET.get('rows','20')
    account = get_object_or_404(Sub_account, pk=pk)
    journals_list = Journal.objects.filter(account=account)
    total ={}#amount  direction   coin
    # print(journals_list)
    for j in journals_list:
        if j.coin.short_title in total:
            total[j.coin.short_title] += float(j.amount)*float(j.direction)
        else:
            total[j.coin.short_title]=float(j.amount)*float(j.direction)

    paginator = Paginator(journals_list, rows)
    page = request.GET.get('page', 1)
    try:
        journals = paginator.page(page)
    except PageNotAnInteger:
        journals = paginator.page(1)
    except EmptyPage:
        journals = paginator.page(paginator.num_pages)
    return render(request, 'sub_account/sub_account_journal.html',
        {'journals':journals,
        'account':account,
        'page': page,
        'total':total,
        'journals_list':journals_list}
    )

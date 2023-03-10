from django.db import models
# from django.contrib.contenttypes.models import ContentType
# from django.contrib.contenttypes.fields import GenericRelation, GenericForeignKey
from common.models import  SoftDeleteModel ,BaseModel
from international.models import Coin
from mptt.models import MPTTModel, TreeForeignKey
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

# Debit (the from-account)  the destination
# Assets expenses dividends
# Credit (the to-account).  the source
#owner's equity liabilities revenue
# Balance Sheet :
#               "Asset" accounts type are normally set as Debit,
#                    therefore its debit balance is shown as positive in the Balance Sheet.
#                   - Current Assets
#                   - Long term Assets
#               "Liabilities and Owner's Equity" account types are normally set as Credit,
#                     therefore its credit balance is shown as positive in the Balance Sheet.
#                     Same applies to the "Owner's Equity" account type.
#                  Liabilities:
#                   - Current Liabilities
#                   - Long term Liabilities
#                  Equity:
#
#
# Profit and Loss:
#               "Revenue" account types are set as Credit,
#                       therefore its Credit balance is shown as positive in the P&L report.
#
#                "Expense" account types are set as Credit,
#                       therefore its Debit balance is shown as negative in the P&L report.
#
#
#
#Assets + Expenses = Liabilities + Revenues + Equity
#
#Debits add to expense and asset accounts and subtract from liability, revenue and equity balances,
# while
#credits subtract from expense and asset balances and add to liability, revenue and equity accounts.

#ASSETS = LIABILITIES + EQUITY + income - EXPENSES
class Account_type(models.Model):#Assets liabilites Expenses income copyrights
    code = models.CharField(max_length=2, unique=True)
    name = models.CharField(max_length=255, unique=True)
    ar_name = models.CharField(max_length=255, null=True, blank=True)
    nature= models.CharField(max_length=3, choices=(
                                            ('-1','debit'),
                                            ('1','credit')))
    final = models.CharField(max_length=3, choices=(
                                            ('1','balance sheet'),
                                            ('2','gain and loss'),))
    debit  =models.JSONField(default=dict, null=True, blank=True)
    credit  =models.JSONField(default=dict,null=True, blank=True)
    balance =models.JSONField(default=dict,null=True, blank=True)
    def __str__(self):
        return self.code+' - '+self.name




class Main_account(MPTTModel):
    account_type = models.ForeignKey(Account_type, on_delete=models.CASCADE, related_name='Main_children')
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True,on_delete=models.SET_NULL)
    code = models.CharField(max_length=5)
    name = models.CharField(max_length=255, unique=True)
    ar_name = models.CharField(max_length=255, null=True, blank=True)
    debit  =models.JSONField(default=dict, null=True, blank=True)
    credit  =models.JSONField(default=dict,null=True, blank=True)
    balance =models.JSONField(default=dict,null=True, blank=True)
    class MPTTMeta:
        order_insertion_by = ['code']
    class Meta:
        unique_together = (('parent', 'code',))
    def __str__(self):
        return self.code+' - '+self.name



class Sub_account(BaseModel):
    main_account =TreeForeignKey('Main_account',  db_index=True,on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    ar_name = models.CharField(max_length=255, null=True, blank=True)

    code = models.CharField(max_length=8, unique=True)
    coin =  models.ManyToManyField(Coin, default=1)
    # dept  =models.DecimalField(max_digits=10, decimal_places=2 ,default=0.0)#
    debit  =models.JSONField(default=dict, null=True, blank=True)
    # credit  =models.DecimalField(max_digits=10, decimal_places=2 ,default=0.0)#
    credit  =models.JSONField(default=dict,null=True, blank=True)
    # balance =models.DecimalField(max_digits=10, decimal_places=2 ,default=0.0)#
    balance =models.JSONField(default=dict,null=True, blank=True)
    used   = models.BooleanField(default=False , blank=True , null=True)

    class Meta:
        unique_together = (('main_account', 'code',))
        verbose_name_plural = 'sub_Accounts'


    def __str__(self):
        return self.code+' - '+self.name


# @receiver(post_save, sender=Main_account)
# def account_balance(sender, instance, created, **kwargs):
#     if not created:
#         parent = Main_account.objects.filter

#         main_account = get_object_or_404(Main_account, pk=account.main_account.id)
#         coin = instance.coin.short_title

#         if instance.direction == '-1':# credit    //{'syp': 69}
#             # temp={}
#             account.credit[coin] =float(account.credit[coin]) + float(instance.amount)
#             main_account.credit[coin] += float(instance.amount)
#         else:
#             account.debit[coin] =float(account.debit[coin]) + float(instance.amount)
#             main_account.debit[coin] += float(instance.amount)
#         # print('float(account.credit[coin])', float(account.credit[coin]))

#         account.balance[coin] += float(account.credit[coin])-float(account.debit[coin])
#         main_account.balance[coin] +=float(account.credit[coin])-float(account.debit[coin])
#         account.save()
#         main_account.save()










# class Account(BaseModel, SoftDeleteModel):
#     Accountchoise=(
#         ('????????????', (
#                     ('1','??????????????????'),
#                     ('2','????????????????????'),
#                     ('3','??????????????????'),
#                     ('4','????????????????????'),
#                     ('5','??????'),#Shipping
#                     ('6','????????????????'),#hotel reservation
#                     ('7','?????????????? ??????'),#travel documents
#                     ('8','????????????'),#commissions
#                     ('9','?????????? ??????'),#health insurance
#                     ('10','??????????'),#backage

#                     ('11','?????????? ????????'),#exchange
#                     ('12','????????????'),#????????????????
#                     ('13','?????????? ????????????'),#Profit and loss
#                     ('14','???????? ????????'),#round balance
#                     ('15','????????????????'),#depreciation
#                     ('16','?????????????? ????????????????'),#Employee entitlements
#                     ('17','?????????????????? ????????????????????'),#social insurance
#                     ('18','??????????????????'),#expenses
#                     )),
#         ('?????????????? ?? ??????????????', (
#             ('20', '??????????????'),
#             ('21','?????????? ??????????????????'),
#             ('22','?????????? ?????? ??????'),
#             ('23','?????????? ?????? ??????'),
#             ('24','?????????? ?????? ????????'),
#             ('25','??????????'),
#             ('26','?????????? ??????'),
#             ('27','?????????? ?????????? ??????'),
#         )),
#       ('???????????? ????????????',(
#             ('30','????????????????'),#owners
#             ('31','????????????????'),#employees
#             ('32','????????????????'),#Boxes
#             ('33','???????????? ??????????'),#daily expenses
#             ('34','????????????????'),#buses

#       )

#       )

#     )


#     name         = models.CharField(max_length=255 )
#     account_type = models.CharField(choices=Accountchoise ,max_length=4, blank=True)

#     class Meta:
#         unique_together = [['name', ]]

#     def __str__(self):

#         return self.name

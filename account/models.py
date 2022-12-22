from django.db import models
# from django.contrib.contenttypes.models import ContentType
# from django.contrib.contenttypes.fields import GenericRelation, GenericForeignKey
from common.models import  SoftDeleteModel #,BaseModel,
from international.models import Coin
from mptt.models import MPTTModel, TreeForeignKey
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

# Debit (the from-account) and Credit (the to-account).
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
    def __str__(self):
        return self.code+' - '+self.name




class Main_account(MPTTModel):
    account_type = models.ForeignKey(Account_type, on_delete=models.CASCADE, related_name='Main_children')
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True,on_delete=models.SET_NULL)
    code = models.CharField(max_length=5)
    name = models.CharField(max_length=255, unique=True)
    ar_name = models.CharField(max_length=255, null=True, blank=True)

    # coin = models.ForeignKey(Coin,null=True,blank=True, on_delete=models.SET_NULL)
    class MPTTMeta:
        order_insertion_by = ['code']
    class Meta:
        unique_together = (('parent', 'code',))
    def __str__(self):
        return self.code+' - '+self.name



class Sub_account(models.Model):
    main_account =TreeForeignKey('Main_account',   db_index=True,on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    ar_name = models.CharField(max_length=255, null=True, blank=True)

    code = models.CharField(max_length=8, unique=True)
    coin =  models.ManyToManyField(Coin, default=Coin.objects.filter(active=True).first().id)
    dept  =models.DecimalField(max_digits=10, decimal_places=2 ,default=0.0)#
    credit  =models.DecimalField(max_digits=10, decimal_places=2 ,default=0.0)#
    balance =models.DecimalField(max_digits=10, decimal_places=2 ,default=0.0)#
    used   = models.BooleanField(default=False , blank=True , null=True)

    class Meta:
        unique_together = (('main_account', 'code',))
        verbose_name_plural = 'sub_Accounts'


    def __str__(self):
        return self.code+' - '+self.name
















# class Account(BaseModel, SoftDeleteModel):
#     Accountchoise=(
#         ('متاجرة', (
#                     ('1','التأشيرات'),
#                     ('2','تذاكرطيران'),
#                     ('3','تذاكربرية'),
#                     ('4','تذاكربحرية'),
#                     ('5','شحن'),#Shipping
#                     ('6','حجزفندقي'),#hotel reservation
#                     ('7','مستندات سفر'),#travel documents
#                     ('8','عمولات'),#commissions
#                     ('9','تأمين صحي'),#health insurance
#                     ('10','رحلات'),#backage

#                     ('11','تحويل عملة'),#exchange
#                     ('12','الاصول'),#رصيدمدور
#                     ('13','أرباح وخسائر'),#Profit and loss
#                     ('14','رصيد مدور'),#round balance
#                     ('15','الاهتلاك'),#depreciation
#                     ('16','مستحقات الموظفين'),#Employee entitlements
#                     ('17','التأمينات الاجتماعية'),#social insurance
#                     ('18','المصروفات'),#expenses
#                     )),
#         ('الشركات و الزبائن', (
#             ('20', 'الزبائن'),
#             ('21','شركات التأشيرات'),
#             ('22','شركات نقل جوي'),
#             ('23','شركات نقل بري'),
#             ('24','شركات نقل بحري'),
#             ('25','فنادق'),
#             ('26','شركات شحن'),
#             ('27','شركات تأمين صحي'),
#         )),
#       ('حسابات الشركة',(
#             ('30','المالكين'),#owners
#             ('31','الموظفين'),#employees
#             ('32','الصناديق'),#Boxes
#             ('33','مصاريف يومية'),#daily expenses
#             ('34','الحافلات'),#buses

#       )

#       )

#     )


#     name         = models.CharField(max_length=255 )
#     account_type = models.CharField(choices=Accountchoise ,max_length=4, blank=True)

#     class Meta:
#         unique_together = [['name', ]]

#     def __str__(self):

#         return self.name

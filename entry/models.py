from django.db import models
from django.conf import settings
from company.models import Company
from account.models import Sub_account
from international.models import Coin
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from common.models import BaseModel, SoftDeleteModel
from django.conf import settings
from django.utils.timezone import now

class Entry( BaseModel,SoftDeleteModel):

    # name     = models.CharField(max_length=500)
    balance = models.BooleanField(default=False)
    narration = models.CharField(max_length=500, null=True, blank=True)
    date = models.DateField(default=now)
    def __str__(self):
        return str(self.id)




class Journal(BaseModel, SoftDeleteModel):

    # journal_2    = models.OneToOneField('self', on_delete=models.SET_NULL, blank=True, null=True)
    entry   = models.ForeignKey(Entry, on_delete=models.CASCADE )
    account = models.ForeignKey(Sub_account, on_delete=models.CASCADE )
    # account_dept =  models.ForeignKey(Sub_account, on_delete=models.CASCADE,related_name='account_dept' )
    amount     =models.PositiveIntegerField(default=0)
    direction  =models.CharField(max_length=3, choices=(('1','debit'),
                                                        ('-1','credit')))

    coin     = models.ForeignKey(Coin, null=True,blank=True, on_delete=models.SET_NULL )
    narration = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return str(self.entry.id)


# @receiver(post_save, sender=Journal)
# def create_Journal(sender, instance, created, **kwargs):
#     if created:
#         if not instance.journal_2 :
#             secondjournal = Journal.objects.create(
#                     journal_2 = instance,
#                     entry             = instance.entry,
#                     account_credit   = instance.account_dept,
#                     account_dept     = instance.account_credit,
#                     dept             = instance.credit ,
#                     credit            = instance.dept ,
#                     coin             = instance.coin,
#                     narration        = instance.narration,
#                     created_at= instance.created_at,
#                     updated_at= instance.updated_at,
#                     author= instance.author,
#                     )
#             instance.journal_2 = secondjournal
#         instance.save()


#
    # account_credit = models.CharField(choices=tuple((k, v) for (k, v, __, __) in ACCOUNT), max_length=4 )
    # sub_account_credit= models.CharField(choices=tuple((k, v) for (k,  __, __,v) in ACCOUNT), max_length=4, null=True,blank=True )
    # sub_account_dept= models.CharField(choices=tuple((k, v) for (k,  __, __, v) in ACCOUNT), max_length=4, null=True,blank=True )
    # account_dept = models.CharField(choices=tuple((k, v) for (k, v, __, __) in ACCOUNT), max_length=4 )
   # NONE= ''
    # Owner= 'Owner'
    # Customer='Customer'
    # employee='employee'
    # boxes='boxes'
    # Expenses='Expenses'
    # bus='bus'
    # Trading='Trading'
    # liabilities='liabilities'
    # Assets='Assets'
    # ACCOUNT=(
    #     ('1','التأشيرات',Trading,NONE),
    #     ('2','تذاكر طيران',Trading,NONE),
    #     ('3','تذاكر برية',Trading,NONE),
    #     ('4','تذاكر بحرية',Trading,NONE),
    #     ('5','شحن',Trading,NONE),
    #     ('6','حجز فندقي',Trading,NONE),
    #     ('7','مستندات سفر',Trading,NONE),
    #     ('8','مستحقات موظفين',liabilities,NONE),
    #     ('9','عمولات',Trading,NONE),
    #     ('10','تحويل عملة',Trading,NONE),
    #     ('11','الاصول',Trading,NONE),
    #     ('12','أرباح وخسائر',Trading,NONE),
    #     ('13','رصيد بداية المدة',Trading,NONE),
    #     ('14','رصيد مدور',Trading,NONE),
    #     ('15','المالكين','Owner',Owner),
    #     ('16','الزبائن','Assets',Customer),
    #     ('17','شركات التأشيرات',liabilities,Customer),
    #     ('18','شركات نقل جوي',liabilities,Customer),
    #     ('19','شركات نقل بري',liabilities,Customer),
    #     ('20','شركات نقل بحري',liabilities,Customer),
    #     ('21','فنادق',liabilities,Customer),
    #     ('22','شركات شحن',liabilities,Customer),
    #     ('23','شركات تأمين',liabilities,Customer),
    #     ('24','رواتب موظفين',Assets,employee),
    #     ('25','تأمينات اجتماعية',Assets,employee),
    #     ('26','الصناديق',Assets,boxes),
    #     ('27','مصروفات',Assets,Expenses),
    #     ('28','الحافلات',Assets,bus),
        # )
from django.db import models
# from common.models import  BaseModel
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver



# Create your models here.
class Coin(models.Model):

    short_title  = models.CharField(max_length=100, blank=True, null=True,help_text="رمز مختصر ")
    long_title   = models.CharField(max_length=300, blank=True, null=True,help_text="الاسم كامل")
    active       = models.BooleanField(default=False,help_text="الاساسية")#     الربح
    exchange   =  models.DecimalField(max_digits=6, decimal_places=2 ,default=1)
    class Meta:
        verbose_name_plural = 'CURRENCIES'

    def __str__(self):
        return f'{self.short_title}'


class Coin_log(models.Model):
    base_coin = models.ForeignKey(Coin,on_delete=models.CASCADE,related_name='base')
    sec_coin = models.ForeignKey(Coin,on_delete=models.CASCADE,related_name='foreign')
    rate         = models.DecimalField(max_digits=6, decimal_places=2 ,default=1)#
    mult       = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)



@receiver(post_save, sender=Coin)
def create_log(sender, instance,  **kwargs):
    # print ('Instance ')
    base= Coin.objects.filter(active=True)
    if  len(base)>1 :
        # print ('Instance >1')
        for c in base:
            if c == instance:
                continue
            c.active=False
            c.save()


    # else:
    #     print ('Instance updated!')
    #     base= Coin.objects.filter(active=True).order_by('id').first()







# @receiver(pre_save , sender=Coin_log)
# def create_log(sender, instance, created, **kwargs):
#     Coin.objects.all(user=instance)


def AddCurrency():
    from currencies import ISO_4217_CURRENCIES
    for item in ISO_4217_CURRENCIES:#(932, 'ZWL Zimbabwean dollar A/10')
        id = item[0]
        short_title = item[1][:3]
        long_title = item[1][4:]
        try:
            cc =Coin(id=id,short_title=short_title,long_title=long_title)
            cc.save()
        except Exception as e:
            print(item)

class Country(models.Model):

    name_ar             = models.CharField(max_length=100, blank=True, null=True)
    name_en             = models.CharField(max_length=300, blank=True, null=True)
    Alpha_2             = models.CharField(max_length=10, blank=True, null=True)
    Alpha_3             = models.CharField(max_length=10, blank=True, null=True)
    currency_alphabetic = models.CharField(max_length=100, blank=True, null=True)
    currency_name       = models.CharField(max_length=100, blank=True, null=True)
    Arabic_Formal       = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Countries'
    def __str__(self):
        return f'{self.name_ar} {self.name_en}'




class City(models.Model):
   # "Damascus","Damascus","33.5000","36.3000","Syria","SY","SYR","Dimashq","primary","2466000","1760685964"
    id          = models.IntegerField(primary_key=True)
    city        = models.CharField(max_length=100, blank=True, null=True,help_text="الاسم المحلي")
    city_ascii  = models.CharField(max_length=100, blank=True, null=True,help_text="الاسم بالانكليزية")
    country     = models.ForeignKey(Country, on_delete=models.SET_NULL, blank=True, null=True)
    iso2        = models.CharField(max_length=100, blank=True, null=True)
    iso3        = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f'{self.city_ascii}'



class AirPort(models.Model):
    #OSDI,large_airport,Damascus International Airport,2020,AS,SY,SY-DI,Damascus,OSDI,DAM,,"36.51559829711914, 33.4114990234375"
    ident       =  models.CharField(max_length=10, blank=True, null=True)
    airport_type = models.CharField(max_length=100, blank=True, null=True)
    name         = models.CharField(max_length=300, blank=True, null=True)
    iso_country  = models.ForeignKey(Country, on_delete=models.SET_NULL, blank=True, null=True)
    iso_region   = models.CharField(max_length=100, blank=True, null=True)
    municipality = models.ForeignKey(City, on_delete=models.SET_NULL, blank=True, null=True)
    iata_code    = models.CharField(max_length=100, blank=True, null=True,help_text="رمز الاتحاد الدولي")
    name_ar      = models.CharField(max_length=300, blank=True, null=True)
    def __str__(self):
        return f'{self.iata_code}  /{self.name} /{self.iso_country}'



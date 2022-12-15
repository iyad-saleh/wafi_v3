from django import forms

from .models import Country, City, AirPort ,Coin, Coin_log



class CoinForm(forms.ModelForm):
    class Meta:
        model = Coin
        fields = ['short_title','long_title','base','exchange']



class Coin_logForm(forms.ModelForm):
    class Meta:
        model = Coin_log
        fields = ['rate','mult','base_coin','sec_coin']



class CountryForm(forms.ModelForm):
    class Meta:
        model = Country
        fields = ['name_ar','name_en','Alpha_2','Alpha_3','currency_alphabetic','currency_name',
        'Arabic_Formal' ]#

class CityForm(forms.ModelForm):
    class Meta:
        model = City
        fields = ['city','city_ascii','country','iso2',
        'iso3']#,'box'

class AirPortForm(forms.ModelForm):
    class Meta:
        model = AirPort
        fields = ['ident','airport_type','name','iso_country',
        'municipality','iata_code','name_ar']#,'box'

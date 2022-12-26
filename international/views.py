from django.shortcuts import render
from .models import Country, City, AirPort, Coin
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.shortcuts import get_object_or_404


def selectCoin(request):
    for c in request.GET:
        if c.startswith('journal_set'):#journal_set-0-coin
            coin = get_object_or_404(Coin, pk=request.GET.get(c))
            cnt = c.strip('journal_set-').strip('-coin')
            print(coin.exchange,cnt)
            context={
            'exchange':coin.exchange,
            'cnt':int(cnt)
            }
            return render(request, 'coin/coin_ex.html',context)

    # print(request.GET)

def searchAirport(request):

    search_text=None
    if  request.GET.get('origin'):
        search_text = request.GET.get('origin')
    elif request.GET.get('destination'):
        search_text = request.GET.get('destination')
    airports = AirPort.objects.all().order_by('id')
    if search_text:

        airports= AirPort.objects.filter(Q(name__icontains=search_text)|Q(iata_code__icontains=search_text)).distinct().order_by('id')


    paginator = Paginator(airports, 10)
    page = request.GET.get('page', 1)
    try:
        airports = paginator.page(page)
    except PageNotAnInteger:
        airports = paginator.page(1)
    except EmptyPage:
        airports = paginator.page(paginator.num_pages)


    return render(request, 'international/searchAirport.html', {
        'airports':airports, 'page': page
    })


#-------------------- Country --------------------------------

class CountryList(ListView):
    model = Country

class CountryCreate(CreateView):
    model = Country
    fields =  ['name_ar','name_en','Alpha_2','Alpha_3','currency_alphabetic','currency_name',
        'Arabic_Formal' ]

class CountryUpdateView(UpdateView):
    model = Country
    fields =  ['name_ar','name_en','Alpha_2','Alpha_3','currency_alphabetic','currency_name',
        'Arabic_Formal' ]
    success_url ="/"

class CountryDetailView(DetailView):
    model = Country


class CountryDeleteView(DeleteView):
    model = Country
    success_url ="/"

#-------------------- City --------------------------------

class CityList(ListView):
    model = City


class CityCreate(CreateView):
    model = City
    fields = ['city','city_ascii','country','iso2', 'iso3']

class CityUpdateView(UpdateView):
    model = City
    fields = ['city','city_ascii','country','iso2', 'iso3']
    success_url ="/"

class CityDetailView(DetailView):
    model = City

class CityDeleteView(DeleteView):
    model = City
    success_url ="/"

#-------------------- AirPort --------------------------------
class AirPortList(ListView):
    model = AirPort


class AirPortCreate(CreateView):
    model = AirPort
    fields = ['ident','airport_type','name','iso_country',
        'municipality','iata_code','name_ar']


class AirPortUpdateView(UpdateView):
    model = AirPort
    fields = ['ident','airport_type','name','iso_country',
        'municipality','iata_code','name_ar']
    success_url ="/"

class AirPortDetailView(DetailView):
    model = AirPort

class AirPortDeleteView(DeleteView):
    model = AirPort
    success_url ="/"
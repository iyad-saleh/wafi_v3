from django.shortcuts import render
from .models import AirLine,Flight,FlightSchedule,Seat,FlightSeat
from .forms import AirLineForm, FlightForm, FlightScheduleForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from django.shortcuts import get_object_or_404
import json
from django.urls import reverse
from international.models import AirPort


def index(request):
    airlines = AirLine.objects.all()
    form = AirLineForm()
    return render(request, 'airline/index.html',
            {'form': form,
            'airlines':airlines,
            'navbar':'Welcom' ,
            'submenu':'airline'

            })


def airline_list(request):
    airlines = AirLine.objects.all()
    return render(request, 'airline/airline_list.html', {
        'airlines':airlines,
    })



@login_required
def add_airline(request):
    if not request.user.is_MANAGER:
        return HttpResponse(
        status=403,
        headers={
            'HX-Trigger': json.dumps({

               "airlineListChanged": None,
            })
        })
    if request.method == "POST":

        form = AirLineForm(request.POST,request.FILES)
        # print("request.POST: ",request.POST)
        if form.is_valid():
            airline = form.save(commit=False)
            airline.author=request.user
            airline.save()
            return HttpResponse(
                status=204,
                headers={
                    'HX-Trigger': json.dumps({
                        "airlineListChanged": None,
                        "showMessage": f"{airline.name} added."
                    })
                })
        else:
            return render(request, 'airline/airline_form.html', {
        'form': form
    })
    else:

        form = AirLineForm()
    return render(request, 'airline/airline_form.html', {
        'form': form
    })



@login_required
def remove_airline(request):
    pass


@login_required
def edit_airline(request):
    pass



# ------------------------------------------- Flight ----------------------------
def flight_index(request, airline_pk):
    airline = get_object_or_404(AirLine, pk=airline_pk)
    flights = Flight.objects.filter(airline=airline)
    form = FlightForm()
    return render(request, 'flight/flight_index.html', {
        'flights':flights,'form':form,'airline':airline,'navbar':"mycompany",'submenu':airline
    })

def flight_list(request,airline_pk):
    airline = get_object_or_404(AirLine, pk=airline_pk)
    flights = Flight.objects.filter(airline=airline)

    return render(request, 'flight/flight_list.html', {
        'flights':flights,'airline':airline
    })



@login_required
def add_flight(request,airline_pk):
    if not request.user.is_MANAGER:
        return HttpResponse(
        status=403,
        headers={
            'HX-Trigger': json.dumps({

               "flightListChanged": None,
            })
        })
    airline = get_object_or_404(AirLine, pk=airline_pk)
    if request.method == "POST":
        form = FlightForm(request.POST)
        if form.is_valid():
            flight = form.save(commit=False)
            flight.author=request.user
            flight.airline=airline
            flight.save()
            return HttpResponse(
                status=204,
                headers={
                    'HX-Trigger': json.dumps({
                        "flightListChanged": True,
                        "showMessage": f"{airline.name} {flight.flightNo} added."
                    })
                })
        else:
            return render(request, 'flight/flight_form.html', {
        'form': form,'airline':airline
    })
    else:

        form = FlightForm()
    return render(request, 'flight/flight_form.html', {
        'form': form,'airline':airline
    })



@login_required
def remove_flight(request,airline_pk):
    pass


@login_required
def edit_flight(request,airline_pk):
    pass



# -------------------- schedule--------------------

def schedule(request):
    schedules = FlightSchedule.objects.all()
    return render(request, 'schedule/schedule.html', {
        'schedules':schedules,
    })


def schedule_index(request,airline_pk,flight_pk):
    airline = get_object_or_404(AirLine, pk=airline_pk)
    flight = get_object_or_404(Flight,pk = flight_pk)
    schedules = FlightSchedule.objects.filter(flight=flight)
    form = FlightScheduleForm()
    return render(request, 'schedule/schedule_index.html', {
        'flight':flight,
        'form':form,
        'airline':airline,
        'schedules':schedules,
        'navbar':airline,
        'submenu':flight
    })

def schedule_list(request,airline_pk,flight_pk):
    airline = get_object_or_404(AirLine, pk=airline_pk)
    flight = get_object_or_404(Flight,pk = flight_pk)
    schedules = FlightSchedule.objects.filter(flight=flight)
    return render(request, 'schedule/schedule_list.html', {
        'flight':flight,
        'airline':airline,
        'schedules':schedules,

    })


def add_schedule(request,airline_pk,flight_pk):
    if not request.user.is_MANAGER:
        return HttpResponse(
        status=403,
        headers={
            'HX-Trigger': json.dumps({

               "flightListChanged": None,
            })
        })
    airline = get_object_or_404(AirLine, pk=airline_pk)
    flight = get_object_or_404(Flight,pk = flight_pk)
    if request.method == "POST":
        # changed_data = dict(request.POST)
        # form = FlightScheduleForm(data = changed_data)

        form = FlightScheduleForm(request.POST)
        # print("departueTime",request.POST.get('departueTime'))
        if form.is_valid():
            # form.cleaned_data['origin'] =get_object_or_404(AirPort,iata_code=request.POST.get('origin')).id
            # form.cleaned_data['destination'] = get_object_or_404(AirPort,iata_code=request.POST.get('destination')).id
            # print('origin',form.cleaned_data['origin'])
            # print('destination',form.cleaned_data['destination'])
            schedule = form.save(commit=False)
            schedule.origin=get_object_or_404(AirPort,iata_code=request.POST.get('origin'))
            schedule.destination=get_object_or_404(AirPort,iata_code=request.POST.get('destination'))
            schedule.author=request.user
            schedule.flight=flight
            schedule.save()
            return HttpResponse(
                status=204,
                headers={
                    'HX-Trigger': json.dumps({
                        "scheduleListChanged": True,
                        "showMessage": f"{airline.name} {flight.flightNo} {schedule} added."
                    })
                })
        else:
            print('form not valid..............',form.errors)
            return render(request, 'schedule/schedule_form.html', {
        'form': form,'airline':airline,'flight':flight
    })
    else:

        form = FlightScheduleForm()
    return render(request, 'schedule/schedule_form.html', {
        'form': form,'airline':airline,'flight':flight
    })


def remove_schedule(request,airline_pk,flight_pk):
    pass


def edit_schedule(request,airline_pk,flight_pk):
    pass


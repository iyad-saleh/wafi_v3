from django.shortcuts import render
from company.models import Company

from django.utils import translation
from django.http import HttpResponseRedirect
# from airline.models import FlightSchedule





def set_language_from_url(request, user_language):
    translation.activate(user_language)
    request.session[translation.LANGUAGE_SESSION_KEY] = user_language
    # I use HTTP_REFERER to direct them back to previous path
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

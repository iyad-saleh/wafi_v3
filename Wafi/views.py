from django.shortcuts import render
from company.models import Company
import json
from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse


def dashboard(request):
    if hasattr( request.user  ,'is_MANAGER' ) :


        return render(request, 'dashboard/dashboard.html')
    return HttpResponse(
        status=403,
        headers={
            'HX-Trigger': json.dumps({

               "customerListChanged": None,
            })
        })



@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]


        context['segment'] = load_template

        html_template = loader.get_template('pages/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('pages/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('pages/page-500.html')
        return HttpResponse(html_template.render(context, request))

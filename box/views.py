import json
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from django.shortcuts import get_object_or_404

from .models import Box
from .forms import BoxForm
from django.contrib.auth.decorators import user_passes_test


@user_passes_test(lambda u: u.is_MANAGER)
def index(request):
    form = BoxForm()
    return render(request, 'box/index.html',{'form':form})

@user_passes_test(lambda u: u.is_MANAGER)
def box_list(request):

    boxs = Box.objects.all()
    return render(request, 'box/box_list.html', {
        'boxs':boxs
    })

@user_passes_test(lambda u: u.is_MANAGER)
def add_box(request):
    if not request.user.is_MANAGER:
        return HttpResponse(
        status=403,
        headers={
            'HX-Trigger': json.dumps({

               "boxListChanged": None,
            })
        })
    if request.method == "POST":
        form = BoxForm(request.POST)
        if form.is_valid():

            box = form.save(commit=False)
            box.author=request.user
            box.save()
            return HttpResponse(
                status=204,
                headers={
                    'HX-Trigger': json.dumps({
                        "boxListChanged": None,
                        "showMessage": f"{box.name} added."
                    })
                })
        else:
            return render(request, 'box/box_form.html', {'form': form   })
    else:

        form = BoxForm()
    return render(request, 'box/box_form.html', {
        'form': form
    })

@user_passes_test(lambda u: u.is_MANAGER)
def edit_box(request, pk):
    box = get_object_or_404(Box, pk=pk)
    if request.method == "POST":
        form = BoxForm(request.POST, instance=box)
        if form.is_valid():
            box = form.save(commit=False)
            box.author=request.user
            box.save()
            return HttpResponse(
                status=204,
                headers={
                    'HX-Trigger': json.dumps({
                        "boxListChanged": None,
                        "showMessage": f"{box.name} updated."})})
        else:
            return render(request, 'box/box_form.html', {'form': form})
    else:
        form = BoxForm(instance=box)

    return render(request, 'box/box_form.html', {
        'form': form,
        'box': box,
    })

@user_passes_test(lambda u: u.is_MANAGER)
@ require_POST
def remove_box(request, pk):
    box = get_object_or_404(Box, pk=pk)
    box.soft_delete()
    return HttpResponse(
        status=204,
        headers={
            'HX-Trigger': json.dumps({
                "boxListChanged": None,
                "showMessage": f"{box.name} deleted."
            })
        })



from django.shortcuts import render
from .forms import ExplorinForm
from .models import *

def Form(request):
    formdata = ExplorinForm()

    if request.method == 'POST':
        formdata = ExplorinForm(request.POST)
        if formdata.is_valid():
            formdata.save()

    context = {'formdata' : formdata}
    return render(request,"form.html",context)


def Table(request):
    form = Applicants.objects.all()

    context = {'form' : form}
    return render(request,"table.html",context)

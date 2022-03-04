from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
from .forms import NameForm
from .models import applicants

def index(request):
    return render(request, "sample.html")

def form(request):
    data = NameForm()
    
    #postMethod
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            form.save()

    #getMethod
    context = {'data': data}
    return render(request, "form.html", context)

def table(request):
    data= applicants.objects.all()
    context= {'data':data}
    return render(request, "table.html",context)


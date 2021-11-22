from django.shortcuts import render
from .models import Destination
def homepage(request):    
    dests=Destination.objects.all()
    return render(request,'index.html',{'dests':dests})

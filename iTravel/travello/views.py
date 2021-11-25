from django.shortcuts import render
from .models import Destination
def homepage(request):    
    dests=Destination.objects.all()
    return render(request,'index.html',{'dests':dests})

def dest_details(request,dest_id):
    dest=list(Destination.objects.filter(id=dest_id))
    if dest:
        return render(request,'destination.html',{'dest':dest[0]})

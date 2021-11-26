from django.shortcuts import render,redirect
from .models import Destination
from .forms import DestinationForm
from django.contrib import messages
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import DestinationSerializer

@api_view(['GET'])
def get_all_destinations(request):
    dests=Destination.objects.all()
    serializer=DestinationSerializer(dests,many=True)
    return Response(serializer.data)



def homepage(request):    
    dests=Destination.objects.all()
    return render(request,'index.html',{'dests':dests})

def dest_details(request,id):
    dest=list(Destination.objects.filter(id=id))[0]
    if dest:
        d=request.session.setdefault('recent_destinations',{})
        d[dest.id]=dest.name
        request.session['recent_destinations']=d
        return render(request,'destination.html',{'dest':dest})

def dest_add(request):
    if request.method=='POST':
        form = DestinationForm(request.POST,request.FILES)
        print(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            messages.info(request,'Error while creating Destination')
    return render(request,'destinationForm.html',{'form':DestinationForm()})
 

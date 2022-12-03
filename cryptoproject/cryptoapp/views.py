from django.http import HttpResponse
from django.shortcuts import render
from .models import  Place

# Create your views here.
def demo(request):
    obj=Place.objects.all()

    return  render(request,"index.html",{'result':obj},)
#def home(request):
   # return render(request,"blog.html")
#def about(request):
 #   return render(request,'about.html')
#def contract(request):
 #   return render(request,'mido.html')
#def details(reqiest):
 #   return  HttpResponse('DETAILS')
#def thanks(request):
 #   return  HttpResponse('THANKS')
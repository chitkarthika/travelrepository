from django.http import HttpResponse
from django.shortcuts import render
from .models import place, scientist
# Create your views here.
def display(request):
    obj = place.objects.all()
    obj1 = scientist.objects.all()
    return render(request, "index.html", {'result': obj, 'result1': obj1})

def homepg(request):
    return render(request,"home.html")
def about(request):
    return render(request,"about.html")
def contact(request):
    return HttpResponse("============Thanks for contacting us============")
def details(request):
    return render(request,"detail.html")
def thanks(request):
    return HttpResponse("$$$$$$$$  $$$$$$$$ THANK YOU $$$$$$$$ $$$$$$$$")
def contact(request):
    return render(request,"contact.html")

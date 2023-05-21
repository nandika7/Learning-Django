from django.shortcuts import render
from django.http import HttpResponse

def hello(request):
    return HttpResponse("hi from hello function")

def home(request):
    #while 2==2:
        #print("stuck in while loop")
    return render(request,"myapp/home.html")




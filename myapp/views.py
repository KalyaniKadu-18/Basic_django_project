from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

# Create your views here.
def myfunctioncall(request):
    return HttpResponse("Hello World!")

def myfunctionabout(request):
    return HttpResponse("About Response!")

def myfunctionadd(request,a,b):
    return HttpResponse(a+b)

def intro(request,name,age):
    mydict = {
        "name":name,
        "age":age
    }
    return JsonResponse(mydict)

def demo(request):
    return render(request,'index.html')

def demosecond(request):
    return render(request,'second.html')

def demothird(request):
    var = "hello!!"
    greeting = "Hiiii!"
    fruits = ["apple","mango","chickoo"]
    mydictionary = {
        "var":var,
        "msg":greeting,
        "myfruits":fruits
    }
    return render(request,'third.html',context=mydictionary)
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
@csrf_exempt
def show(req):
    if  req.method=="POST":
            print(req.POST.get("name"))
            print(req.POST.get("age"))
            return HttpResponse("hello from app")
    return HttpResponse("invalid")
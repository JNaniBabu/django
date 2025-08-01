from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .serilalizer import sample_serializer
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.

def message(req):
    return HttpResponse("hello")

@csrf_exempt
def getusers(req):
    d=json.loads(req.body)
    con_data=sample_serializer(data=d)
    if con_data.is_valid():
        con_data.save()
        return HttpResponse("hello")
    return HttpResponse("nothing")
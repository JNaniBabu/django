from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

def details(self):
    return JsonResponse({"name":"jakkulananibabu"})


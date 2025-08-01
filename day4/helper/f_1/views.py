from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def help(req):
    return HttpResponse ("hello ")
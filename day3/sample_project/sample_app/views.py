from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from . import product
# Create your views here.
@csrf_exempt
def checking(req,id):
        p=product.product_list
        if id < 0 or id >20:
          return HttpResponse ("ID IS NOT FOUND")
        else:
              for i in p:
                if i["id"] == id:
                      return JsonResponse({"data":i})
       
        
import json
import bcrypt
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .serializer import sample_serializer
from .models import users

# from .

# Create your views here.

def message(req):
    return HttpResponse("message")

def getuser(req):
    obj=json.loads(req.body)
    data=users.objects.get(user_name=obj["user_name"])
    s_data=sample_serializer(data)
    plain_pass=obj["password"].encode("utf-8")
    stored_pass=s_data.data["password"].encode("utf-8")
    same=bcrypt.checkpw(plain_pass,stored_pass)
    print(same)
    return HttpResponse("hello")

def postuser(req):
    data=json.loads(req.body)
    password=data["password"]
    password=password.encode('utf-8')
    salt=bcrypt.gensalt(10)
    hashed_pass=bcrypt.hashpw(password,salt)
    hashed_pass=hashed_pass.decode('utf-8')
    data["password"]=hashed_pass
    converted_Data=sample_serializer(data=data)
    if converted_Data.is_valid():
        converted_Data.save()
        return HttpResponse("successful",status=201)
    return HttpResponse("failed")
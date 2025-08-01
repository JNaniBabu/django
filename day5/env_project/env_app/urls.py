from django.urls import path
from . import views

urlpatterns=[
    path("msg/",view=views.message),
    path('getuser/',view=views.getusers)
]
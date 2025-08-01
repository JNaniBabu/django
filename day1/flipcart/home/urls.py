from django.urls import path
from . import views

urlpatterns=[
    path("home/",view=views.home)
]



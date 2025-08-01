from django.urls import path

from . import  views

urlpatterns=[
    path("show/",view=views.show)
]
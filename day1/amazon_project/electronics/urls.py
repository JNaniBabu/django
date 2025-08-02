from django.urls import path
from . import views

urlpatterns=[
    path("details/",view=views.details)
]
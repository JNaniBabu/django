from django.urls import path
from . import views

urlpatterns=[
    path("msg/",view=views.show)
]
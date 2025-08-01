from django.urls import path
from . import views

urlpatterns=[
    path("check/<int:id>",view=views.checking)
]
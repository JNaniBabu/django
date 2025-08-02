from django.urls import path
from . import views

urlpatterns=[
    path("post/",view=views.help)
]
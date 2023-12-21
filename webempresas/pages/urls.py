from django.urls import path
from .views import *

urlpatterns = [
    path('<slug:slug>/', page, name="page"),
]
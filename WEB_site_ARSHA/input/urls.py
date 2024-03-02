from django.urls import path
from .views import add_inp
urlpatterns = [
    path("", add_inp, name="inputadd")
]

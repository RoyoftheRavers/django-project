from django.urls import path
from . import views

urlpatterns = [
    path('', views.football_home, name='football_home'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('callback', views.callback),
    path('teststage', views.test_stage),
]
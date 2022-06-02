from django.urls import path
from . import views

urlpatterns = [
    path('getPost/', views.getPost),
    path('setPost/', views.setPost),
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),  # URL is now available as 'dashboard'
]
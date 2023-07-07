from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView, name='index_view'),
    path('login', views.LoginView, name='login_view'),
    path('dashboard', views.DashboardView, name='dashboard_view'),
]
from django.contrib import admin
from django.urls import path, include
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views as home_views

urlpatterns = [
   path('home/', home_views.home, name='home'),
   path('animals/', home_views.animals, name='animals'),
   path('staff/', home_views.staff, name='staff'),
   path('login/', home_views.login, name='login'),

   ]
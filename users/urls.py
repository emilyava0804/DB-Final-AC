from django.contrib import admin
from django.urls import path, include
from django.contrib import admin
from django.urls import path, include
from . import views as users_views

urlpatterns = [
   path('staff_home/', users_views.staff_home, name='staff-home'),
   path('staff_staff/', users_views.staff_staff, name='staff-staff'),
   ]
from django.contrib import admin
from django.urls import path, include
from django.contrib import admin
from django.urls import path, include
from . import views as users_views
from . views import staff_animals

urlpatterns = [
   path('staff_home/', users_views.staff_home, name='staff-home'),
   path('staff_staff/', users_views.staff_staff, name='staff-staff'),
   path('staff_animals/', staff_animals.as_view(), name='staff-animals'),
   path('staff_exhibits/', users_views.staff_exhibits, name='staff_exhibits'),
   ]
from django.contrib import admin
from .models import employee, employeePhone, park, volunteer, volunteerPhone, animalFood, exhibit, animal, specialNeed, specialAnimal

# Register your models here.
admin.site.register(employee)
admin.site.register(employeePhone)
admin.site.register(park)
admin.site.register(volunteer)
admin.site.register(volunteerPhone)
admin.site.register(animalFood)
admin.site.register(exhibit)
admin.site.register(animal)
admin.site.register(specialNeed)
admin.site.register(specialAnimal)
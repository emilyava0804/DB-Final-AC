from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from . models import employee, employeePhone, animal

class UserRegisterForm(UserCreationForm):
	email = forms.EmailField()

	class Meta:
		model = User 
		fields = ['username', 'email', 'password1', 'password2']


class newEmployeeForm(forms.ModelForm):
	class Meta:
		model = employee
		fields = ['employeeType', 'employeeDOB', 'fname', 'lname', 'salary']


class newEmployeePhone(forms.ModelForm):
	class Meta:
		model = employeePhone
		fields = ['employeeID', 'ePhoneNumber']


class animalForm(forms.ModelForm):
	class Meta:
		model = animal
		fields = ('animalName', 'animalAge', 'animalGender', 'exhibitID',)

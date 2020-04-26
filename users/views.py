from django.shortcuts import render, redirect
from . forms import UserRegisterForm
from django.views.generic import ListView, DetailView, UpdateView
from . models import employee, employeePhone, volunteer, volunteerPhone

# Create your views here.
def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			return redirect('staff-home')
	else:
		form = UserRegisterForm()
	return render(request, 'users/register.html', {'form': form})


def staff_home(request):
    return render(request, 'users/staff_home.html', {'title': 'Staff-Home'})


def staff_staff(request):
	employees = employee.objects.all()
	ephones = employeePhone.objects.all()
	volunteers = volunteer.objects.all()
	volunteerPhones = volunteerPhone.objects.all()
	context= {'employees': employees, 'ephones': ephones, 'volunteers': volunteers, 'volunteerPhones': volunteerPhones}

	return render(request, 'users/staff_staff.html', context)


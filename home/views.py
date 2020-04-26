from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html', {'title': 'Home'})


def animals(request):
    return render(request, 'animals.html', {'title': 'Animals'})

def staff(request):
	return render(request, 'staff.html', {'title': 'Staffs'})

def login(request):
    return render(request, 'login.html', {'title': 'Login'})
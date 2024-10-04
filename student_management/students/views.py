

# Create your views here.
# views.py in students app
from django.forms import Form
from django.shortcuts import render
from .models import Student

def custom_admin_view(request):
    students = Student.objects.all()
    return render(request, 'students/custom_admin.html', {'students': students})

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from .forms import RegisterForm

from django.shortcuts import redirect

def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # After successful registration, redirect to login
    else:
        form = RegisterForm()
    return render(request, 'students/register.html', {'form': form})

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # Redirect after login
    else:
        form = AuthenticationForm()
    return render(request, 'students/login.html', {'form': form})

from django.contrib.auth import logout

def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect('login')
    
from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from .forms import StudentForm

   # Create new student
def student_create(request):
       form = StudentForm(request.POST or None)
       if form.is_valid():
           form.save()
           return redirect('student_list')
       return render(request, 'students/student_form.html', {'form': form})

   # List students
def student_list(request):
       students = Student.objects.all()
       return render(request, 'students/student_list.html', {'students': students})

   # Update student
def student_update(request, pk):
       student = get_object_or_404(Student, pk=pk)
       form = StudentForm(request.POST or None, instance=student)
       if form.is_valid():
           form.save()
           return redirect('student_list')
       return render(request, 'students/student_form.html', {'form': form})

   # Delete student
def student_delete(request, pk):
       student = get_object_or_404(Student, pk=pk)
       if request.method == "POST":
           student.delete()
           return redirect('student_list')
       return render(request, 'students/student_confirm_delete.html', {'student': student})
# students/views.py

from django.shortcuts import render
from django.http import HttpResponse

def custom_view(request):
    # You can return a simple response or render a template
    return HttpResponse("This is the custom view!")

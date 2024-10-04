"""
URL configuration for student_management project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from students.admin import admin_site
urlpatterns = [
    path('admin/', admin_site.urls),
    path('students/', include('students.urls')),
]
# urls.py in students app
from django.urls import path
from students.views import custom_admin_view

urlpatterns = [
    path('admin/custom/', custom_admin_view, name='custom_admin'),
]
from django.urls import path
from students.views import register_view, login_view, logout_view
urlpatterns = [
       path('register/', register_view, name='register'),
       path('login/', login_view, name='login'),
       path('logout/', logout_view, name='logout'),
   ]
from django.urls import path
from students.views import student_create, student_list, student_update, student_delete
urlpatterns = [
       path('students/', student_list, name='student_list'),
       path('students/new/', student_create, name='student_create'),
       path('students/<int:pk>/edit/', student_update, name='student_update'),
       path('students/<int:pk>/delete/', student_delete, name='student_delete'),
   ]
   
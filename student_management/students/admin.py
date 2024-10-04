
from django import views
from django.contrib import admin

from .models import Student, Course

class CourseInline(admin.TabularInline):
    model = Course.students.through
    extra = 1

class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone')
    search_fields = ('first_name', 'last_name', 'email')
    inlines = [CourseInline]
    pass

class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)

admin.site.register(Student, StudentAdmin)
admin.site.register(Course, CourseAdmin)
# admin.py
from django.urls import path
from django.http import HttpResponse
from django.contrib import admin

# Custom view
def custom_admin_view(request):
    return HttpResponse("This is a custom admin view!")

# Registering custom URL in the admin
class CustomAdminSite(admin.AdminSite):
    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('custom/', self.admin_view(custom_admin_view)),
        ]
        return custom_urls + urls

# Replace the default admin site with the custom one
admin_site = CustomAdminSite(name='custom_admin')
admin_site.register(Student)
admin_site.register(Course)
# admin.py

from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

# Custom view function
def custom_admin_view(request):
    return HttpResponse("This is a custom admin view!")

# Custom Admin Site
class CustomAdminSite(admin.AdminSite):
    site_header = 'My Custom Admin'
    site_title = 'Admin Panel'
    index_title = 'Welcome to the Custom Admin'

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('custom/', self.admin_view(custom_admin_view))
        ]
        return custom_urls + urls

# Create an instance of your custom admin site
admin_site = CustomAdminSite(name='custom_admin')

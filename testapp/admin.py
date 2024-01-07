from django.contrib import admin
from testapp.models import Student
# Register your models here.

class stuadmin(admin.ModelAdmin):
    list_display = ['name','rno']
admin.site.register(Student,stuadmin)
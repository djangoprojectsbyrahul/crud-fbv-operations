from django.contrib import admin
from testapp.models import StudentRegister

class StudentRegisterAdmin(admin.ModelAdmin):
    list_display = ['name','marks']

# Register your models here.
admin.site.register(StudentRegister,StudentRegisterAdmin)

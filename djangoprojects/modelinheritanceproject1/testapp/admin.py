from django.contrib import admin
from testapp.models import Student,Student1,Teacher,Teacher1,ContactInfo1,Parent,Child,SubChild
# Register your models here.
admin.site.register(ContactInfo1)
admin.site.register(Student1)
admin.site.register(Teacher1)
admin.site.register(Parent)
admin.site.register(Child)
admin.site.register(SubChild)

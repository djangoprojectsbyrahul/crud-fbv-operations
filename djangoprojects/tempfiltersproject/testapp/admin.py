from django.contrib import admin
from testapp.models import FilterDemo

# Register your models here.


class FilterDemoAdmin(admin.ModelAdmin):
    list_display = ['name', 'subject', 'department', 'date']


admin.site.register(FilterDemo, FilterDemoAdmin)

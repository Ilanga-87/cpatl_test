from django.contrib import admin

from .models import Subdivision, Employee


class SubdivisionAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent')


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'position', 'subdivision')


admin.site.register(Subdivision, SubdivisionAdmin)
admin.site.register(Employee, EmployeeAdmin)

from django.contrib import admin


from .models import Employee


class EmployeeAdmin(admin.ModelAdmin):
    fields = ['name', 'email','contact',]

admin.site.register(Employee, EmployeeAdmin)

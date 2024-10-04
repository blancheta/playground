from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.contrib.auth.models import Group

from accounts.models import Group as NewGroup, Employee

from django.contrib.auth.admin import UserAdmin

class EmployeeAdmin(UserAdmin):
    pass


admin.site.register(Employee, EmployeeAdmin)

class GroupAdmin(ModelAdmin):

    fields = ("name", "permissions")


# Register your models here.
admin.site.register(NewGroup, GroupAdmin)
admin.site.unregister(Group)

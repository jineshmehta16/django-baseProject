from django.contrib import admin

from .models import Users
from .models import Roles


@admin.register(Users)
class UserAdmin(admin.ModelAdmin):
    list_display = ['firstName', 'lastName', 'id', 'userId', 'emailId', 'contactNumber']


@admin.register(Roles)
class RoleAdmin(admin.ModelAdmin):
    list_display = ['roleId', 'roleName']






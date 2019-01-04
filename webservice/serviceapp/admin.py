from django.contrib import admin

from .models import Users
from .models import Roles
from .models import Leads


@admin.register(Roles)
class RoleAdmin(admin.ModelAdmin):
    list_display = ['roleId', 'roleName']


@admin.register(Users)
class UserAdmin(admin.ModelAdmin):
    list_display = ['firstName', 'lastName', 'id', 'userId', 'emailId', 'contactNumber']


@admin.register(Leads)
class LeadAdmin(admin.ModelAdmin):
    list_display = ['leadId', 'firstName', 'lastName','callStatus', 'emailId', 'contactNumber']









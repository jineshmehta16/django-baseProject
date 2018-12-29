from django.contrib import admin

from .models import Users

class UserAdmin(admin.ModelAdmin):
    admin.site.register(Users)
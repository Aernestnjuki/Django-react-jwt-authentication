from django.contrib import admin
from .models import User, User_Profile

class User_Admin_modification(admin.ModelAdmin):
    list_display = ['username', 'email']

class User_Profile_Admin_Modification(admin.ModelAdmin):
    list_display = ['user', 'full_name', 'verified']

admin.site.register(User, User_Admin_modification)
admin.site.register(User_Profile, User_Profile_Admin_Modification)

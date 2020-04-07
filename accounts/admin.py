from django.contrib import admin
from .models import Userprofile
# from .models import Register
# Register your models here.
# class RegisterDisplay(admin.ModelAdmin):
#     list_display = ('id','firstname','username','email','S_reviewer','sign_time')
#
# admin.site.register(Register,RegisterDisplay)
from django.contrib.auth.models import User

class MyUserAdmin(admin.ModelAdmin):
    list_display = ('id','username', 'email', 'is_active', 'last_login','is_staff')

admin.site.unregister(User)
admin.site.register(User, MyUserAdmin)
admin.site.register(Userprofile)
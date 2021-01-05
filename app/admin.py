from django.contrib import admin
from .models import Adminmodel, Usermodel

# Register your models here.

@admin.register(Adminmodel)
class AdminmodelAdmin(admin.ModelAdmin):
    list_display = ('id', 'adminid', 'user', 'gender', 'is_active')


@admin.register(Usermodel)
class UsermodelAdmin(admin.ModelAdmin):
    list_display = ('id', 'userid', 'user', 'gender', 'is_active')

from django.contrib import admin

from .models import *
# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'admnno')
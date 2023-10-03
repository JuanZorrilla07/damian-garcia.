from django.contrib import admin

# Register your models here.
from .models import AuthGroup, AuthPermission

admin.site.register(AuthGroup)
admin.site.register(AuthPermission)
from django.contrib import admin
from .models import ManagementUser
# Register your models here.
class AdminUser(admin.ModelAdmin):
    list_display = [
        "first_name","last_name","phone_number",
        "email","username","password"
    ]
admin.site.register(ManagementUser, AdminUser)
from django.contrib.auth import get_user_model
from django.contrib import admin

CustomUser = get_user_model()
class CustomUserAdmin(admin.ModelAdmin):
    model = CustomUser
    list_display = ['username', 'email']


admin.site.register(CustomUser, CustomUserAdmin)

from django.contrib import admin
from .models.user import CustomUser
from django.contrib.auth.admin import UserAdmin

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ('email', 'get_full_name', 'is_staff', 'is_superuser', 'is_verified', 'is_active', 'date_joined')
    search_fields = ('email', 'first_name', 'second_name')
    list_filter = ('is_staff', 'is_superuser', 'is_verified', 'is_active')

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'second_name')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'second_name', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )

    ordering = ('email',)
    filter_horizontal = ('groups', 'user_permissions',)

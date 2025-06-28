from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import CustomUser
from .forms import SiteAdminUserCreationForm

@admin.register(CustomUser)
class UserAdmin(BaseUserAdmin):
    add_form = SiteAdminUserCreationForm
    list_display = ('email', 'is_municipal', 'is_public', 'is_superuser', 'first_name', 'last_name', 'middle_name', 'is_google')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'middle_name', 'last_name')}),
        ('Permissions', {'fields': ('is_staff', 'is_superuser', 'is_municipal', 'is_public')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'middle_name', 'last_name', 'password1', 'password2', 'is_municipal', 'is_public'),
        }),
    )

    ordering = ('email',)
    search_fields = ('email',)
    list_filter = ("is_municipal", "is_public")
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


from .form import Sign_Up_form, CustomUserForm

# Register your models here.
User = get_user_model()



class CustomUserAdmin(UserAdmin):
    add_form = Sign_Up_form
    form = CustomUserForm

    list_display = ('email', 'is_staff', 'is_active',)
    list_filter = ('email', 'is_staff', 'is_active',)

    fieldsets = (
        (None, {'fields' : ('email', 'password')}),
        ('Permission', {'fields' : ('is_staff', 'is_active')})
    )

    add_fieldsets = (
        (None, {
            'classes' : ('wide',),
            'fields' : ('email', 'password1', 'password2', 'is_staff', 'is_active')
        }),
    )

    search_fields = ('email',)
    ordering = ('email',)


admin.site.unregister(Group)
admin.site.register(CustomUser, CustomUserAdmin)
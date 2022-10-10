from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from django.utils.translation import gettext_lazy

from core import models

# Register your models here.
class UserAdmin(BaseUserAdmin):
    ordering=['id']
    list_display=['email','name']

    fieldsets=(
        (None,{'fields':('email','password')}),
        (gettext_lazy('Personal Info'),{'fields':('name',)}),
        (
            gettext_lazy('Permissions'),{
                'fields':(
                    'is_active',
                    'is_staff',
                    'is_superuser',
                )
            }
        ),
        (gettext_lazy('Important Dates'),{'fields':('last_login',)}),

    )
    readonly_fields=['last_login']


admin.site.register(models.User, UserAdmin)
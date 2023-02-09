from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Accounts

# Register your models here.
class AccountAdmin(UserAdmin):
    list_display=('email','first_name','last_name','last_login','is_active')
    list_display_links=('first_name','last_name','email')
    readonly_fields=('last_login','joined_date')

    filter_horizontal=()
    list_filter=()
    fieldsets=()

admin.site.register(Accounts,AccountAdmin)

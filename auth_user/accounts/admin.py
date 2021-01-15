from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from accounts.models import CustomUser

class CustomAdmin(UserAdmin):
    list_display        = ('email', 'username', 'date_joined', 'last_login', 'is_admin', ) 
    search_fields       = ('email', 'username', 'date_joined', 'is_admin',)
    ordering            = ('username',)
    readonly_fields     = ('date_joined', 'last_login')
    
    # when clicking user name for details.
    fieldsets           = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('username',)}),
        ('Permissions', {'fields': ('is_admin', 'date_joined', 'last_login',)}), # To call non editable attributes, you should set 'readonly_fields' above..
    )
    
    # for Creating user form
    add_fieldsets       = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1', 'password2'),
        }),
    )
    
    filter_horizontal   = () # I don't know what it is..
    list_filter         = ('is_admin',) # filter displaying one side of the admin site.
    
admin.site.register(CustomUser, CustomAdmin)
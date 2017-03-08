from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from .forms import UserChangeForm
from .forms import UserCreationForm
from .models import User

class UserAdmin(UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = [
        'email',
        'surname',
        'firstname',
        'patronymic',
        'status',
        'category',
        'is_ban',
    ]

    list_filter = ('status','category',)

    fieldsets = (
                ('Personal info', {
                 'fields': (
                     'firstname',
                     'surname',
                     'patronymic',
                     'category',
                     'status',
                     'is_ban',
                     'birthday',
                     'balance',
                     )}),
                ('Contacts', {
                 'fields': (
                     'email',
                     'phone',
                     'country',
                     'region',
                     'city',
                     'index',
                     'street',
                     'home',
                     'office',
                     )}),
                ('Permissions', {'fields': ('is_admin',)}),
                ('Important dates', {'fields': ('last_login',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'date_of_birth',
                'email',
                'password1',
                'password2'
            )}
         ),
    )

    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()

admin.site.register(User, UserAdmin)
admin.site.unregister(Group)

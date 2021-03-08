from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models

# Register your models here.

@admin.register(models.User)
class CustomUserAdmin(UserAdmin):
    """ Custom User Admin """
    
    fieldsets=UserAdmin.fieldsets+(
        #튜플의 첫 줄 = fieldset의 title을 저장하는 곳
        #튜플 안의 리스트 = fieldset의 field들
        (
            "Custom field",
            {
                "fields":(
                    "avatar",
                    "gender",
                    "bio",
                    "birthdate",
                    "language",
                    "currency",
                    "superhost"
                )
            }
        ),
    )
    pass

# admin.site.register(models.User.CustomUserAdmin)
# @admin.register(models.User)와 같은 말
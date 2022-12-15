from django.contrib import admin
from .models import User, Item, Question, Bid
from .forms import RegisterForm
from django.contrib.auth.admin import UserAdmin

class CustomUserAdmin(UserAdmin):
    model = User
    add_form = RegisterForm
    fieldsets = (
        *UserAdmin.fieldsets,
        (
            'Details',
            {
                'fields':(
                    'DOB',
                    'image',
                )
            }
        )
    )
    
            
            
# Register your models here.
admin.site.register(Item)
admin.site.register(User, CustomUserAdmin)
admin.site.register(Question)
admin.site.register(Bid)

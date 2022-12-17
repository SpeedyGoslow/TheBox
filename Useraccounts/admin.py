from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import SmeCustomUserCreationForm,SmeCustomUserChangeForm
from .models import SmeCustomUser

# Register your models here.
class SmeCustomAdmin(UserAdmin):
    add_form= SmeCustomUserCreationForm
    form = SmeCustomUserChangeForm
    model = SmeCustomUser
    list_display = ["email","username","SME_Name","SME_Address","SME_Phone","is_staff"]
    fieldsets = UserAdmin.fieldsets +((None,{"fields":("SME_Name",)}),(None,{"fields":("SME_Address",)}),(None,{"fields":("SME_Phone",)}),)
    add_fieldsets = UserAdmin.add_fieldsets +((None,{"fields":("SME_Name",)}),(None,{"fields":("SME_Address",)}),(None,{"fields":("SME_Phone",)}),) 
    
    
admin.site.register(SmeCustomUser,SmeCustomAdmin)
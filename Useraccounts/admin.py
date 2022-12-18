from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import ManufacturerCustomUserCreationForm,ManufacturerCustomUserChangeForm
from .models import ManufacturerCustomUser

# Register your models here.
class ManufacturerCustomAdmin(UserAdmin):
    add_form= ManufacturerCustomUserCreationForm
    form = ManufacturerCustomUserChangeForm
    model = ManufacturerCustomUser
    list_display = ["email","username","Manufacturer_Name","Manufacturer_Address","Manufacturer_Phone","is_staff"]
    fieldsets = UserAdmin.fieldsets +((None,{"fields":("Manufacturer_Name",)}),(None,{"fields":("Manufacturer_Address",)}),(None,{"fields":("Manufacturer_Phone",)}),)
    add_fieldsets = UserAdmin.add_fieldsets +((None,{"fields":("Manufacturer_Name",)}),(None,{"fields":("Manufacturer_Address",)}),(None,{"fields":("Manufacturer_Phone",)}),) 
    
    
admin.site.register(ManufacturerCustomUser,ManufacturerCustomAdmin)
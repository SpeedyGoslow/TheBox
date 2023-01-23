from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import ManufacturerCustomUser

class ManufacturerCustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = ManufacturerCustomUser
        fields = UserCreationForm.Meta.fields +("Manufacturer_Name","Manufacturer_Address","Manufacturer_Phone",)
        

class ManufacturerCustomUserChangeForm(UserChangeForm):
    class Meta:
        model = ManufacturerCustomUser
        fields = UserChangeForm.Meta.fields
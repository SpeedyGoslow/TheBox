from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import SmeCustomUser

class SmeCustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = SmeCustomUser
        fields = UserCreationForm.Meta.fields +("SME_Name","SME_Address","SME_Phone",)
        

class SmeCustomUserChangeForm(UserChangeForm):
    class Meta:
        model = SmeCustomUser
        fields = UserChangeForm.Meta.fields
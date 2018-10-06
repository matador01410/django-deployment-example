from django import forms
from first_app.models import User

class NewUserForms(forms.ModelForm):
    class Meta():
        model = User
        fields = '__all__'

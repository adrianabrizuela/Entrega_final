from django import forms
from django.contrib.auth.models import User



class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']


class PostSearchForm(forms.Form):
    titulo = forms.CharField(
        max_length=50, required=True, label="Ingresar nombre de la sala"
    )


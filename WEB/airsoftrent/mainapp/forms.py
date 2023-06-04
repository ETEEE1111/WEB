from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django import forms


class AuthUserForm(AuthenticationForm, forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')
    
    def __init__(self, *args,**kwards):
        super().__init__(*args, **kwards)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
from django import forms
from django.contrib.auth import get_user_model,authenticate
from django.contrib.auth.forms import AuthenticationForm
# from django.contrib.auth.forms import UserCreationForm
User = get_user_model()

class RegisterForm(forms.ModelForm):
    confirm_password = forms.CharField(max_length=40, widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Confirm Password'
    }),)
    class Meta:
        model = User
        fields = (
            'first_name', 
            'last_name', 
            'email', 
            'password',
            "username"
            )

        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'First name'
            }),
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'username'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Last name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Email'
            }),
            'password': forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Password'
            }),
       
        }

    def clean(self):
            password = self.cleaned_data['password']
            confirm_password = self.cleaned_data['confirm_password']
            if password != confirm_password:
                raise forms.ValidationError('Password and Confirm password is not same')
            return super().clean()

    def save(self, *args, **kwargs):
        user = super().save(*args, **kwargs)
        user.set_password(self.cleaned_data['password'])
        user.save()
        return user

class LoginForm(AuthenticationForm):
   username = forms.CharField(max_length=40, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Username'
    }),)

   password = forms.CharField(max_length=40, widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Password'
    }),)
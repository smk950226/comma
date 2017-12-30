from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Profile

class SignupForm(UserCreationForm):
    name = forms.CharField(label = '이름', required=True, widget = forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': '이름',
    }))
    email = forms.EmailField(label = 'E-mail', required=True, widget = forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'E-mail',
    }))
    univ = forms.CharField(label = '대학교', required=True, widget = forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': '대학교',
    }))
    major = forms.CharField(label = '전공', required=True, widget = forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': '전공',
    }))
    group = forms.CharField(label = '요일조', required=True, widget = forms.Select(attrs={
        'class': 'form-control',
        'placeholder': '요일조',
    }))

    def save(self):
        user = super().save()

        profile = Profile.objects.create(
            user = user,
            email = self.cleaned_data['email'],
            univ = self.cleaned_data['univ'],
            major = self.cleaned_data['major'],
            group = self.cleaned_data['group'],
        )

        return user
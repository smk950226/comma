from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Profile
from django.utils.safestring import mark_safe


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
    }, choices = (
        ('Tue', '화요일조'),
        ('Wed', '수요일조'),
        ('Thu', '목요일조'),
        ('Fri', '금요일조'),)))

    key = forms.CharField(label = 'Key', help_text = '각 조의 조장님께 받은 Key를 입력해 주세요.')

    def clean_key(self):
        key = self.cleaned_data.get('key', None)
        if key != 'comma2018': #원하는 key 입력
            raise forms.ValidationError(mark_safe('<p style="color: red;">key를 잘못 입력하셨습니다.</p>'))
        return key

    def save(self):
        user = super().save()

        profile = Profile.objects.create(
            user = user,
            name = self.cleaned_data['name'],
            email = self.cleaned_data['email'],
            univ = self.cleaned_data['univ'],
            major = self.cleaned_data['major'],
            group = self.cleaned_data['group'],
        )

        return user
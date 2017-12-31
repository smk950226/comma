from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Profile
from django.utils.safestring import mark_safe
from django.core.exceptions import ValidationError
from django.utils.translation import gettext, gettext_lazy as _
from django.contrib.auth import password_validation #변경함


class SignupForm(UserCreationForm):
    error_messages = {
        'password_mismatch': _( mark_safe('<p style="color: red;">비밀번호가 일치하지 않습니다.</p>')),
    }

    password1 = forms.CharField(
        label=_("비밀번호"),
        strip=False,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': '비밀번호',
        }),
        help_text='8자 이상 입력해 주세요. 숫자로만 구성된 비밀번호는 사용하실 수 없습니다.',
    )
    password2 = forms.CharField(
        label=_("비밀번호 확인"),
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': '비밀번호 확인',
        }),
        strip=False,
        help_text=_("비밀번호를 한번 더 입력해 주세요."),
    )

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

    key = forms.CharField(label = 'Key', required=True, widget = forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Key',
    }), help_text = '각 조의 조장님께 받은 Key를 입력해 주세요.')

    def clean_key(self):
        key = self.cleaned_data.get('key', None)
        if key != 'comma2018': #원하는 key 입력
            raise forms.ValidationError(mark_safe('<p style="color: red;">key를 잘못 입력하셨습니다.</p>'))
        return key

    def clean_email(self):
        email = self.cleaned_data.get('email', None)
        qs = Profile.objects.filter(email = email)

        if qs:
            raise ValidationError(mark_safe('<p style="color: red;">E-mail이 중복됩니다.</p>'))

        return email

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()

        profile = Profile.objects.create(
            user = user,
            name = self.cleaned_data['name'],
            email = self.cleaned_data['email'],
            univ = self.cleaned_data['univ'],
            major = self.cleaned_data['major'],
            group = self.cleaned_data['group'],
        )

        return user
from django import forms
from .models import ActPhoto

class ActPhotoForm(forms.ModelForm):
    class Meta:
        model = ActPhoto
        fields = '__all__'
        widgets = {
            'photo': forms.FileInput(attrs={
                'value': '이미지',
            }),
            'year': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': '활동연도',
            }),
            'date': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '2017.01.01',
            }),
            'site': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '활동장소'
            }),
        }
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserModel
from django.core.exceptions import ValidationError
from .models import *

class AddPostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cat'].empty_label = "Категорію не обрано!"

    class Meta:
        model = Women
        fields = ['title', 'slug', 'content', 'photo', 'is_published', 'cat']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'content': forms.Textarea(attrs={'cols': 60, 'rows': 10}),

        }
        # fields = '__all__'

    # title = forms.CharField(max_length=255, label="Назва", widget=forms.TextInput(attrs={'class': 'form-input'}))
    # slug = forms.SlugField(max_length=255, label="URL")
    # content = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}), label="Зміст")
    # is_published = forms.BooleanField(label="Публікація", required=False, initial=True)
    # cat = forms.ModelChoiceField(queryset=Category.objects.all(), label="Категорія", empty_label="Категорію не обрано")

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title)>200:
            raise ValidationError('Довжина перевищує 200 символів')
        
        return title


class RegisterUserForm(UserCreationForm):

    username = forms.CharField(label="Логін", widget = forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label="Email", widget=forms.EmailInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label="Пароль", widget = forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label="Повтор паролю", widget = forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = UserModel
        fields = ('username', 'email', 'password1', 'password2')

        # widgets = {
        #     'username': forms.TextInput(attrs={'class': 'form-input'}),
        #     'password1': forms.PasswordInput(attrs={'class': 'form-input'}),
        #     'password2': forms.PasswordInput(attrs={'class': 'form-input'}),
        # }


# class AuthenticationForm(UserCreationForm):

    

from django import forms
from django.contrib.auth.forms import UserCreationForm
from home.models import *
from django.forms import TextInput, Textarea


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = [
            'name', 'email', 'message'
        ]


class NewUserForm(UserCreationForm):
    phone = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'phone', 'email', 'password1', 'password2']
        widgets = {
            'first_name': TextInput(attrs={'type': 'text', 'placeholder': 'Ism'}),
            'last_name': TextInput(attrs={'text': 'text', 'placeholder': 'Familiya'}),
            'phone': TextInput(attrs={'type': 'text', 'placeholder': 'Telefon raqam'}),
            'email': TextInput(attrs={'type': 'email', 'placeholder': 'Elektron pochta'}),
            'password1': TextInput(attrs={'type': 'password', 'placeholder': 'Yangi parol'}),
            'password2': TextInput(attrs={'type': 'password', 'placeholder': 'Parolni takrorlang'}),
        }

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.phone = self.cleaned_data['phone']
        if commit:
            user.save()
        return user

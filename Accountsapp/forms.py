from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm

from .models import User


class RegistrationForm(UserCreationForm):
    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        try:
            _ = User.objects.get(email=email)
        except User.DoesNotExist:
            return email
        raise forms.ValidationError(f"Email {email} is already in use.")

    def clean_user_id(self):
        user_id = self.cleaned_data['user_id']
        try:
            _ = User.objects.get(user_id=user_id)
        except User.DoesNotExist:
            return user_id
        raise forms.ValidationError(f"User_id {user_id} is already in use.")

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        try:
            _ = User.objects.get(phone=phone)
        except User.DoesNotExist:
            return phone
        raise forms.ValidationError(f"Phone {phone} is already in use.")

    class Meta:
        model = User
        fields = ('user_id', 'username', 'email', 'phone')


class AuthenticationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('user_id', 'password')

    def clean(self):
        if self.is_valid():
            user_id = self.cleaned_data['user_id']
            password = self.cleaned_data['password']
            if not authenticate(user_id=user_id, password=password):
                raise forms.ValidationError("Invalid login")

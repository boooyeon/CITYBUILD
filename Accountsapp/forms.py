from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from .models import User
USER_INFO = ['username', 'user_id', 'password1', 'email', 'phone']
USER_UPDATE = ['user_id', 'username', 'email', 'phone']

class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = (*USER_INFO,)
    
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

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = (*USER_UPDATE,)

    def clean_password(self):
        return self.initial["password"]


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

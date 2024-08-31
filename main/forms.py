from django import forms
from .models import Users


class LoginUser(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(max_length=50)

    def clean_username(self):
        username = self.cleaned_data['username']
        if Users.objects.get(username=username) is not None:
            return username
        raise forms.ValidationError('Username does not exist')


class RegisterUser(forms.ModelForm):
    class Meta:
        model = Users
        fields = ['username', 'first_name', 'last_name', 'email', 'gender', 'city', 'phone', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }

    def clean_username(self):
        username = self.cleaned_data['username']
        if Users.objects.filter(username=username).exists():
            raise forms.ValidationError('Username already exists.')
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        if '@' not in email:
            raise forms.ValidationError('Email must contain @.')
        return email

    def save(self, commit = True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user

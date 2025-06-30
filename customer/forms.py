from django import forms
from .models import Customer
from django.core.exceptions import ValidationError

class CustomerRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label="Password")
    confirm_password = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")
    age = forms.IntegerField(label="Age")  # Ensures age is included as a field

    class Meta:
        model = Customer
        fields = ['username', 'first_name', 'last_name', 'email', 'mobile_number', 'age', 'password', 'confirm_password']

    def clean_password(self):
        password = self.cleaned_data.get('password')

        # Password validation rules
        if len(password) < 8:
            raise ValidationError("Password must be at least 8 characters long.")
        if not any(char.isupper() for char in password):
            raise ValidationError("Password must contain at least one uppercase letter.")
        if not any(char.isdigit() for char in password):
            raise ValidationError("Password must contain at least one digit.")
        return password

    def clean_age(self):
        age = self.cleaned_data.get('age')
        if age < 14:
            raise ValidationError("You must be at least 14 years old to register.")
        return age

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password and confirm_password and password != confirm_password:
            self.add_error('confirm_password', "Passwords do not match.")
        return cleaned_data

    def save(self, commit=True):
        customer = super().save(commit=False)
        customer.set_password(self.cleaned_data["password"])  # Hash the password
        if commit:
            customer.save()
        return customer

from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import UserProfile

# Custom signup form extending Django's built-in UserCreationForm
class SignupForm(UserCreationForm):
    # Add email field and make it required
    email = forms.EmailField(required=True)

    class Meta:
        # Use our custom UserProfile model
        model = UserProfile
        # Specify which fields to include in the form
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']

# Custom login form extending Django's built-in AuthenticationForm
class LoginForm(AuthenticationForm):
    # Add optional remember me checkbox
    remember_me = forms.BooleanField(required=False)
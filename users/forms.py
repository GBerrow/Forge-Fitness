from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import UserProfile, PracticeNote

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

class PracticeNoteForm(forms.ModelForm):
    """Form for creating and editing practice notes"""
    
    class Meta:
        model = PracticeNote
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g., My Weekly Training Plan'
            }),
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Write your thoughts, plans, or goals here...'
            })
        }
    
    def __init__(self, *args, **kwargs):
        self.page = kwargs.pop('page', None)
        super().__init__(*args, **kwargs)
        
        # Set page-specific placeholders
        if self.page:
            context = self.get_page_context()
            self.fields['content'].widget.attrs['placeholder'] = context.get('placeholder', '')
    
    def get_page_context(self):
        """Get page-specific context for form"""
        contexts = {
            'training': {
                'placeholder': 'e.g., "3-day split: Push, Pull, Legs" or "Focus on progressive overload"'
            },
            'activity': {
                'placeholder': 'e.g., "20-minute walk every morning" or "Stretch routine in the evening"'
            },
            'progression': {
                'placeholder': 'e.g., "Run 5K non-stop in 3 weeks" or "Lose 5kg over 3 months"'
            }
        }
        return contexts.get(self.page, {})

class UserProfileForm(forms.ModelForm):
    """Form for updating user profile"""
    
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'bio', 'profile_picture']
        widgets = {
            'bio': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Tell us about your fitness journey...'
            })
        }
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.exceptions import ValidationError
from django.core.files.uploadedfile import UploadedFile
from PIL import Image
import os
from .models import UserProfile, PracticeNote, UserSettings

# Custom signup form extending Django's built-in UserCreationForm
class SignupForm(UserCreationForm):
    """Enhanced signup form with better validation"""
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
        }
    
    def clean_email(self):
        """Ensure email is unique"""
        email = self.cleaned_data.get('email')
        if UserProfile.objects.filter(email=email).exists():
            raise ValidationError('A user with this email already exists.')
        return email
    
    def clean_username(self):
        """Additional username validation"""
        username = self.cleaned_data.get('username')
        if len(username) < 3:
            raise ValidationError('Username must be at least 3 characters long.')
        return username

# Custom login form extending Django's built-in AuthenticationForm
class LoginForm(AuthenticationForm):
    # Add optional remember me checkbox
    remember_me = forms.BooleanField(required=False)

class PracticeNoteForm(forms.ModelForm):
    """Form for creating and editing practice notes with better validation"""
    
    class Meta:
        model = PracticeNote
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g., My Weekly Training Plan',
                'maxlength': '200'
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
    
    def clean_title(self):
        """Validate title"""
        title = self.cleaned_data.get('title', '').strip()
        
        if not title:
            raise ValidationError('Title is required.')
        
        if len(title) > 200:
            raise ValidationError('Title must be less than 200 characters.')
        
        return title
    
    def clean_content(self):
        """Validate content"""
        content = self.cleaned_data.get('content', '').strip()
        
        if not content:
            raise ValidationError('Content is required.')
        
        if len(content) > 2000:  # Set a reasonable limit
            raise ValidationError('Content must be less than 2000 characters.')
        
        return content
    
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
    """Form for updating user profile with enhanced validation"""
    
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'email', 'bio', 'profile_picture']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'bio': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Tell us about your fitness journey...',
                'maxlength': '500'
            }),
            'profile_picture': forms.FileInput(attrs={
                'class': 'form-control',
                'accept': 'image/*'
            }),
        }
    
    def clean_profile_picture(self):
        """Enhanced validation for profile picture uploads"""
        picture = self.cleaned_data.get('profile_picture')
        
        if picture:
            # Check file size (5MB max)
            if picture.size > 5 * 1024 * 1024:
                raise ValidationError('Image file too large. Maximum size is 5MB.')
            
            # Check file type
            if not picture.content_type.startswith('image/'):
                raise ValidationError('File must be an image.')
            
            # Validate file extension
            valid_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.webp']
            file_extension = os.path.splitext(picture.name)[1].lower()
            if file_extension not in valid_extensions:
                raise ValidationError('Invalid file type. Please use: JPG, JPEG, PNG, GIF, or WebP.')
            
            # Optional: Check image dimensions using PIL
            try:
                image = Image.open(picture)
                # Check if image is too large (e.g., max 2048x2048)
                if image.width > 2048 or image.height > 2048:
                    raise ValidationError('Image dimensions too large. Maximum size is 2048x2048 pixels.')
            except Exception:
                raise ValidationError('Invalid image file.')
        
        return picture
    
    def clean_bio(self):
        """Validate bio length and content"""
        bio = self.cleaned_data.get('bio', '').strip()
        
        if len(bio) > 500:
            raise ValidationError('Bio must be less than 500 characters.')
        
        return bio

class UserSettingsForm(forms.ModelForm):
    """Form for user account settings"""
    class Meta:
        model = UserSettings
        fields = ['account_status', 'email_notifications']
        widgets = {
            'account_status': forms.Select(attrs={'class': 'form-control'}),
            'email_notifications': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

class AccountDeleteForm(forms.Form):
    """Form for account deletion confirmation"""
    confirmation = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Type "DELETE" to confirm'
        })
    )
    
    def clean_confirmation(self):
        confirmation = self.cleaned_data.get('confirmation')
        if confirmation != 'DELETE':
            raise forms.ValidationError('Please type "DELETE" to confirm account deletion.')
        return confirmation
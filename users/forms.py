from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate
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
    """Custom login form that accepts both username and email"""
    
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Username or Email',
            'autofocus': True
        }),
        label='Username or Email'
    )
    
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Password'
        }),
        label='Password'
    )
    
    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username is not None and password:
            self.user_cache = authenticate(
                self.request, 
                username=username, 
                password=password
            )
            if self.user_cache is None:
                raise forms.ValidationError(
                    'Please enter a correct username/email and password. '
                    'Note that both fields may be case-sensitive.'
                )
            else:
                self.confirm_login_allowed(self.user_cache)

        return self.cleaned_data

# Alias for backward compatibility
EmailOrUsernameAuthenticationForm = LoginForm

# ORIGINAL PracticeNoteForm (keep for activity and progression pages)
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

# TrainingNoteForm (specialized for training page)
class TrainingNoteForm(forms.ModelForm):
    """Enhanced form for training notes with structured fields"""
    
    class Meta:
        model = PracticeNote
        fields = ['title', 'content', 'gym_days_per_week', 'weekly_split', 
                 'session_rating', 'what_went_well', 'what_to_improve', 'exercises_completed']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g., Week 1 Training Plan'
            }),
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Overall training notes and goals...'
            }),
            'gym_days_per_week': forms.Select(attrs={
                'class': 'form-control'
            }, choices=[(i, f'{i} days') for i in range(1, 8)]),
            'weekly_split': forms.Select(attrs={
                'class': 'form-control'
            }),
            'session_rating': forms.Select(attrs={
                'class': 'form-control'
            }, choices=[(i, f'{i} star{"s" if i != 1 else ""}') for i in range(1, 6)]),
            'what_went_well': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 2,
                'placeholder': 'What went well in this session?'
            }),
            'what_to_improve': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 2,
                'placeholder': 'What could be improved next time?'
            }),
            'exercises_completed': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'List exercises: Bench Press 3x8, Squats 3x10, etc.'
            })
        }
    
    def __init__(self, *args, **kwargs):
        self.page = kwargs.pop('page', None)
        super().__init__(*args, **kwargs)
    
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
        
        if len(content) > 2000:
            raise ValidationError('Content must be less than 2000 characters.')
        
        return content

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
            # Check if it's a new upload (has content_type) or existing file
            if hasattr(picture, 'content_type'):
                # It's a new upload, validate it
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
            
            # If it's an existing file (no content_type), just return it
        
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
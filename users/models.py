from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

class UserProfile(AbstractUser):
    """
    Extended User model for the educational fitness dashboard
    WHY: Adds bio and profile picture for personalization
    """
    bio = models.TextField(max_length=500, blank=True, null=True, help_text="Tell us about your fitness journey")
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    
    class Meta:
        verbose_name = "User Profile"
        verbose_name_plural = "User Profiles"
    
    def __str__(self):
        return self.username

class UserSettings(models.Model):
    """
    User account settings and preferences
    WHY: Allows users to manage their account status
    """
    ACCOUNT_STATUS_CHOICES = [
        ('active', 'Active'),
        ('inactive', 'Inactive'),
        ('private', 'Private'),
    ]
    
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    account_status = models.CharField(max_length=20, choices=ACCOUNT_STATUS_CHOICES, default='active')
    email_notifications = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "User Settings"
        verbose_name_plural = "User Settings"
    
    def __str__(self):
        return f"{self.user.username}'s Settings"

class PracticeNote(models.Model):
    """
    User's personal notes on fitness concepts (MAIN CRUD FEATURE)
    WHY: Page-specific practice areas for educational engagement
    """
    PAGE_CHOICES = [
        ('training', 'Training'),
        ('activity', 'Activity'), 
        ('progression', 'Progression'),
    ]
    
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    page = models.CharField(max_length=20, choices=PAGE_CHOICES)
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = "Practice Note"
        verbose_name_plural = "Practice Notes"
    
    def __str__(self):
        return f"{self.user.username} - {self.page} - {self.title}"
    
    def get_page_context(self):
        """Return page-specific context for prompts and guidance"""
        contexts = {
            'training': {
                'prompt_title': '📝 Plan Your Training Approach',
                'prompt_text': "Based on what you've just read, outline a simple weekly training plan or focus area you want to work on.",
                'placeholder': 'e.g., "3-day split: Push, Pull, Legs" or "Focus on progressive overload"',
                'icon': '🏋️'
            },
            'activity': {
                'prompt_title': '🏃 Practice Logging Your Daily Activity',
                'prompt_text': "List some activities or movement goals you'd like to include in your day. These could be workouts, steps, or just staying active.",
                'placeholder': 'e.g., "20-minute walk every morning" or "Stretch routine in the evening"',
                'icon': '🏃'
            },
            'progression': {
                'prompt_title': '🎯 Set Your Short and Long-Term Goals',
                'prompt_text': "Reflect on your goals based on what you've learned. What's your short-term goal? What bigger milestone are you aiming for?",
                'placeholder': 'e.g., "Run 5K non-stop in 3 weeks" or "Lose 5kg over 3 months"',
                'icon': '🎯'
            }
        }
        return contexts.get(self.page, {})

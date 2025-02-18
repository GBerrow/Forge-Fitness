from django.db import models
from django.contrib.auth.models import AbstractUser

# UserProfile extends the base Django user to add custom fields
class UserProfile(AbstractUser):
    # Store user profile pictures in 'profile_pics' directory
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    # Text field for user's personal description
    bio = models.TextField(null=True, blank=True)
    # Automatically set when user account is created
    created_at = models.DateTimeField(auto_now_add=True)

    # Display username when UserProfile object is printed
    def __str__(self):
        return self.username

# Settings for user account management
class UserSettings(models.Model):
    # Define possible account status choices
    ACCOUNT_STATUS = [
        ('active', 'Active'),
        ('deactivated', 'Deactivated'),
    ]
    # Link settings to a specific user (one-to-one relationship)
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    # Track whether account is active or deactivated
    account_status = models.CharField(max_length=15, choices=ACCOUNT_STATUS, default='active')

    # Display format: "username - status"
    def __str__(self):
        return f"{self.user.username} - {self.account_status}"

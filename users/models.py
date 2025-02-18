from django.db import models
from django.contrib.auth.models import AbstractUser

class UserProfile(AbstractUser):
    """
    Custom user model that extends Django's built-in AbstractUser.
    Provides additional fields and functionality for user profiles.
    """
    # Profile picture field - stores user uploaded images
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    
    # Bio field - allows users to write about themselves
    bio = models.TextField(null=True, blank=True)
    
    # Timestamp for account creation
    created_at = models.DateTimeField(auto_now_add=True)

    # Group relationships - manages user group memberships
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='userprofile_set',
        blank=True,
        verbose_name='groups',
        help_text='The groups this user belongs to.'
    )
    
    # User permissions - manages specific user permissions
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='userprofile_set',
        blank=True,
        verbose_name='user permissions',
        help_text='Specific permissions for this user.'
    )

    def __str__(self):
        """Returns username for string representation of the model"""
        return self.username

class UserSettings(models.Model):
    """
    Manages user account settings and preferences.
    Stores account status and other user-specific settings.
    """
    # Define possible account statuses
    ACCOUNT_STATUS = [
        ('active', 'Active'),
        ('deactivated', 'Deactivated'),
    ]

    # One-to-one relationship with UserProfile
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    
    # Current status of the user account
    account_status = models.CharField(max_length=15, choices=ACCOUNT_STATUS, default='active')

    def __str__(self):
        """Returns formatted string with username and account status"""
        return f"{self.user.username} - {self.account_status}"

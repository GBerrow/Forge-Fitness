from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        """Create and return a regular user with an email and password."""
        if not email:
            raise ValueError("Users must have an email address")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)  # Hash password
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """Create and return a superuser with an email and password."""
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(email, password, **extra_fields)

class User(AbstractBaseUser):
    """Custom User Model for Authentication and Profile Management"""

    # Primary Key - Unique identifier for each user
    user_id = models.AutoField(primary_key=True)

    # Personal Information - Basic user details
    first_name = models.CharField(max_length=50)  # User's first name
    last_name = models.CharField(max_length=50)   # User's last name
    email = models.EmailField(unique=True)        # Unique email for authentication

    # Authentication - Security related fields
    password_hash = models.TextField()  # Securely stored by Django's password hashing

    # Profile - Optional user profile information
    profile_picture = models.CharField(max_length=255, blank=True, null=True)  # URL to profile image
    bio = models.TextField(blank=True, null=True)  # User's biography or description
    
    # Account Status - Metadata
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp of account creation

    # User Manager - Custom manager for user operations
    objects = UserManager()

    # Authentication Configuration - Django specific settings
    USERNAME_FIELD = "email"  # Use email as the unique identifier
    REQUIRED_FIELDS = ["first_name", "last_name"]  # Required fields during user creation

    def __str__(self):
        return self.email  # String representation of user object
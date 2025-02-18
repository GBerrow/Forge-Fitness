from django.contrib import admin
from .models import UserProfile, UserSettings

# Configure the admin interface for UserProfile
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    # Fields to display in the admin list view
    list_display = ('id', 'first_name', 'last_name', 'email', 'created_at')
    
    # Enable searching by these fields
    search_fields = ('email', 'first_name', 'last_name')
    
    # Add filter options by creation date
    list_filter = ('created_at',)
    
    # Sort users by creation date (newest first)
    ordering = ('-created_at',)
    
    # Prevent modification of creation date
    readonly_fields = ('created_at',)

# Configure the admin interface for UserSettings
@admin.register(UserSettings)
class UserSettingsAdmin(admin.ModelAdmin):
    # Fields to display in the admin list view
    list_display = ('user', 'account_status')
    
    # Add filter options by account status
    list_filter = ('account_status',)
    
    # Enable searching by user's email
    search_fields = ('user__email',)
    
    # Sort settings by username
    ordering = ('user',)

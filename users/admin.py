from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UserProfile, UserSettings, PracticeNote

@admin.register(UserProfile)
class UserProfileAdmin(UserAdmin):
    """Custom admin for UserProfile"""
    # Add the bio and profile_picture fields to the existing UserAdmin fieldsets
    fieldsets = UserAdmin.fieldsets + (
        ('Profile Info', {'fields': ('bio', 'profile_picture', 'created_at')}),
    )
    readonly_fields = ('created_at',)
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'created_at')

@admin.register(UserSettings)
class UserSettingsAdmin(admin.ModelAdmin):
    list_display = ('user', 'account_status', 'email_notifications', 'created_at')
    list_filter = ('account_status', 'email_notifications')
    search_fields = ('user__username',)

@admin.register(PracticeNote)
class PracticeNoteAdmin(admin.ModelAdmin):
    list_display = ('user', 'page', 'title', 'created_at')
    list_filter = ('page', 'created_at')
    search_fields = ('user__username', 'title', 'content')
    readonly_fields = ('created_at', 'updated_at')

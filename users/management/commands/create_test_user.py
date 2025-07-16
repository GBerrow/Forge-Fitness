from django.core.management.base import BaseCommand
from users.models import UserProfile, UserSettings

class Command(BaseCommand):
    help = 'Create a test user for production'

    def handle(self, *args, **options):
        # Check if test user already exists
        if UserProfile.objects.filter(username='testuser').exists():
            self.stdout.write(self.style.WARNING('Test user already exists'))
            return

        try:
            # Create test user
            user = UserProfile.objects.create_user(
                username='testuser',
                email='test@example.com',
                password='testpass123',
                first_name='Test',
                last_name='User'
            )
            
            # Create user settings
            UserSettings.objects.create(user=user)
            
            self.stdout.write(
                self.style.SUCCESS(f'Successfully created test user: {user.username}')
            )
            
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'Error creating test user: {str(e)}')
            )
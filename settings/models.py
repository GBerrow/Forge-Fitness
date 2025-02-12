from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Settings(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    account_status = models.CharField(
        max_length=15,
        choices=[('active', 'Active'), ('deactivated', 'Deactivated')],
        default='active'
    )

    def __str__(self):
        return f"{self.user.email} - {self.account_status}"

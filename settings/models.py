class UserSettings(models.Model):
    """Stores user-specific settings and preferences"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    theme_preference = models.CharField(max_length=10, choices=[("light", "Light"), ("dark", "Dark")])
    unit_preference = models.CharField(max_length=10, choices=[("metric", "Metric"), ("imperial", "Imperial")])
    notification_frequency = models.CharField(max_length=20, choices=[("daily", "Daily"), ("weekly", "Weekly"), ("never", "Never")])
    quiet_hours_start = models.TimeField(null=True, blank=True)
    quiet_hours_end = models.TimeField(null=True, blank=True)
    two_factor_enabled = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} Settings"

class Activity(models.Model):
    """Tracks user physical activities"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    activity_type = models.CharField(max_length=50)  # e.g., Running, Walking
    steps = models.IntegerField(default=0)
    distance = models.FloatField(help_text="Distance covered (km or miles)")
    calories_burned = models.FloatField()
    duration = models.IntegerField(help_text="Duration in minutes")
    date = models.DateField()

    def __str__(self):
        return f"{self.user.username} - {self.activity_type} on {self.date}"

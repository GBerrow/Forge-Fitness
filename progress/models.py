class Progress(models.Model):
    """Tracks user goals and milestones"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    goal = models.CharField(max_length=255)
    progress_percentage = models.FloatField(default=0)
    milestones = models.TextField()
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} - {self.goal} ({self.progress_percentage}%)"

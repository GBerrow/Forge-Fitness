class TrainingPlan(models.Model):
    """Stores user-created training plans"""
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Achievement(models.Model):
    """Stores badges earned by users"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    badge = models.CharField(max_length=100)  # e.g., "Steps Champion"
    date_earned = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.badge}"

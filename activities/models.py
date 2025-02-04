class DaillyActivity(models.Model):
    """Tracks user physical activities"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    activity_type = models.CharField(max_length=50)  # e.g., Running, Walking
    steps = models.PositiveIntegerField(default=0)
    progress_percentage = models.FloatField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])
    distance = models.FloatField(help_text="Distance covered (km or miles)")
    calories_burned = models.FloatField()
    duration = models.IntegerField(help_text="Duration in minutes")
    date = models.DateField()

    def __str__(self):
        return f"{self.user.username} - {self.activity_type} on {self.date}"

class WorkoutLogs(models.Model):
    """Logs user workouts with sets and reps"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    enrolled_users = models.ManyToManyField(User, related_name="enrolled_classes")
    workout_name = models.CharField(max_length=100)
    sets = models.PositiveIntegerField()
    reps = models.PositiveIntegerField()
    weight = models.FloatField(null=True, blank=True)  # Optional
    date = models.DateField()

    def __str__(self):
        return f"{self.user.username} - {self.workout_name} on {self.date}"
    
class Achievements(models.Model):
    """Stores badges earned by users"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    badge = models.CharField(max_length=100)  # e.g., "Steps Champion"
    date_earned = models.DateField(default=timezone.now)

    def __str__(self):
        return f"{self.user.username} - {self.badge}"


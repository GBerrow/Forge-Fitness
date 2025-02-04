class Workouts(models.Model):
    """Logs user workouts with sets and reps"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    workout_name = models.CharField(max_length=100)
    sets = models.PositiveIntegerField()
    reps = models.PositiveIntegerField()
    weight = models.FloatField(null=True, blank=True)  
    date = models.DateField()

    def __str__(self):
        return f"{self.user.username} - {self.workout_name} on {self.date}"

class TrainingPlans(models.Model):
    """Stores user-created training plans"""
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
      
class Classes(models.Model):
    """Stores pre-recorded, guided video classes"""
    title = models.CharField(max_length=255)
    description = models.TextField()
    video_url = models.URLField()
    duration = models.DurationField()
    instructor = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title 
    

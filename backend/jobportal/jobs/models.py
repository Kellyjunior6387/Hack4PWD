# jobs/models.py
from django.db import models
from django.utils import timezone
from users.models import User  # Import User model to reference employer

class Job(models.Model):
   
    id = models.AutoField(primary_key=True)  # Auto-incremented primary key
    title = models.CharField(max_length=100)
    description_id = models.TextField()  # Stores detailed job description
    employer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='jobs')  # Reference to User model
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    type = models.CharField(max_length=20)
    accessibility_tags = models.CharField(max_length=255)
    status = models.CharField(max_length=10, default='open')  # New status field

    def __str__(self):
        return self.title


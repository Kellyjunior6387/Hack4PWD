# jobs/models.py
from django.db import models
from django.utils import timezone
from users.models import User  # Import User model to reference employer

class Job(models.Model):
    JOB_TYPE_CHOICES = [
        ('full_time', 'Full-time'),
        ('part_time', 'Part-time'),
        ('contract', 'Contract'),
        ('freelance', 'Freelance'),
        ('internship', 'Internship'),
    ]
    STATUS_CHOICES = [
        ('open', 'Open'),
        ('closed', 'Closed'),
        ('applied', 'Applied'),
    ]

    id = models.AutoField(primary_key=True)  # Auto-incremented primary key
    title = models.CharField(max_length=100)
    description_id = models.TextField()  # Stores detailed job description
    employer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='jobs')  # Reference to User model
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    type = models.CharField(max_length=20, choices=JOB_TYPE_CHOICES)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='open')  # New status field

    def __str__(self):
        return self.title
    

class AccessibilityTag(models.Model):
    TAG_CHOICES = [
        ('sign_language_friendly', 'Sign Language Friendly'),
        ('remote_friendly', 'Remote Friendly'),
        ('wheelchair_accessible', 'Wheelchair Accessible'),
        ('braille_available', 'Braille Available'),
        # Add more tags as needed
    ]

    id = models.AutoField(primary_key=True)  # Auto-incremented primary key
    job = models.ForeignKey('Job', on_delete=models.CASCADE, related_name='accessibility_tags')  # Links to Job
    tags = models.CharField(max_length=50, choices=TAG_CHOICES)  # Tag indicating accessibility features

    def __str__(self):
        return f"{self.tags} for Job ID: {self.job.id}"
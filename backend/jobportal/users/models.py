from django.db import models
# users/models.py
from django.utils import timezone

class User(models.Model):
    """Model to implement a jobseeker or employer"""
    ROLE_CHOICES = [
        ('job_seeker', 'Job Seeker'),
        ('employer', 'Employer'),
    ]

    DISABILITY_CHOICES = [
        ('hearing', 'Hearing Impairment'),
        ('visual', 'Visual Impairment'),
        ('mobility', 'Mobility Impairment'),
        ('neurodivergent', 'Neurodivergent'),
        ('bipolar', 'Bipolar'),
    ]

    id = models.AutoField(primary_key=True)  # Auto-incremented ID
    email = models.EmailField(unique=True)  # Unique email for each user
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=255)  # Password will be hashed
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    disability_type = models.CharField(max_length=20, null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email


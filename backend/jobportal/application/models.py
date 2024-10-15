from django.db import models
from django.conf import settings

class Job(models.Model):
    """Model representing job postings."""
    title = models.CharField(max_length=255)  # Job title
    description = models.TextField()  # Job description
    employer = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name='jobs'
    )  # Link to employer (CustomUser)
    location = models.CharField(max_length=255)  # Job location
    salary = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # Optional salary field
    date_posted = models.DateTimeField(auto_now_add=True)  # Automatically set to now when the job is created

    def __str__(self):
        return self.title


class Application(models.Model):
    """Model representing job applications submitted by job seekers."""
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='applications')  # Job being applied for
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='applications')  # Job seeker (CustomUser)
    date_applied = models.DateTimeField(auto_now_add=True)  # Automatically set to now when the application is created
    status = models.CharField(max_length=50, default='Pending')  # Application status

    def __str__(self):
        return f"{self.user.username} applied for {self.job.title} - Status: {self.status}"


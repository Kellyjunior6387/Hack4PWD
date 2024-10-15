from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    """Custom user model that extends the default Django user model."""
    email = models.EmailField(unique=True, verbose_name='email address')  # Unique email field
    bio = models.TextField(null=True, blank=True)  # Optional field for a brief bio
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)  # Optional profile picture

    USERNAME_FIELD = 'email'  # Use email for authentication
    REQUIRED_FIELDS = ['username']  # Required fields for creating a superuser

    def __str__(self):
        return self.email  
    
    class UserProfile(models.Model):
    """Profile model for storing additional user information."""
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)  # One-to-one relationship with CustomUser
    date_of_birth = models.DateField(null=True, blank=True)  # Optional field for date of birth
    location = models.CharField(max_length=255, null=True, blank=True)  # Optional field for location
    skills = models.TextField(null=True, blank=True)  # Optional field for user skills

    def __str__(self):
        return f"{self.user.username}'s Profile"  # String representation of the user profile
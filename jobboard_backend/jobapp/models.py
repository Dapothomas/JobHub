from django.contrib.auth.models import AbstractUser, User
from django.db import models
from django.template import defaultfilters 
from django.conf import settings 

class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        ('jobseeker', 'Job Seeker'),
        ('employer', 'Employer'),
    )
    
    user_type = models.CharField(
        max_length=20, 
        choices=USER_TYPE_CHOICES, 
        # default='job_seeker'
    )
    
    # Optional additional fields
    company_name = models.CharField(max_length=255, blank=True, null=True)
    profile_description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.username


class Category(models.Model):
    title = models.CharField(max_length=255)
    
    class Meta:
        ordering = ('title',)
        
        
class Job(models.Model):
    category = models.ForeignKey("Category", related_name='jobs', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    position_salary = models.CharField(max_length=255) 
    position_location = models.CharField(max_length=255) 
    company_name = models.CharField(max_length=255) 
    company_location = models.CharField(max_length=255) 
    company_email = models.EmailField() 
    created_at = models.DateTimeField(auto_now_add=True) 
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,  # Dynamic reference to current user model
        on_delete=models.CASCADE,
        related_name='created_jobs'  # Helpful for reverse lookups
    )
    
    class Meta:
        ordering = ('-created_at',)
        
    def created_at_formatted(self):
        return defaultfilters.date(self.created_at, 'M d, Y')
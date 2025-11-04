from django.db import models

class LearningJourney(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date_learned = models.DateField()
    category = models.CharField(max_length=100)
    
    def __str__(self):
        return self.title

class AboutMe(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    email = models.EmailField()
    interests = models.TextField()
    profile_picture = models.ImageField(
        upload_to='profile_pictures/',
        blank=True,
        null=True,
        help_text="Upload your profile picture"
    )
    
    def __str__(self):
        return self.name

class AdminScreenshot(models.Model):
    SCREENSHOT_TYPES = [
        ('learning_journey', 'Learning Journey Admin'),
        ('about_me', 'About Me Admin'),
        ('general', 'General Admin'),
    ]
    
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    screenshot = models.ImageField(upload_to='admin_screenshots/')
    screenshot_type = models.CharField(max_length=20, choices=SCREENSHOT_TYPES)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
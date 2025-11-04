from django.contrib import admin
from .models import LearningJourney, AboutMe, AdminScreenshot

@admin.register(LearningJourney)
class LearningJourneyAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'date_learned']
    list_filter = ['category', 'date_learned']

@admin.register(AboutMe)
class AboutMeAdmin(admin.ModelAdmin):
    list_display = ['name', 'email']
    readonly_fields = ['profile_picture_preview']
    
    def profile_picture_preview(self, obj):
        if obj.profile_picture:
            return f'<img src="{obj.profile_picture.url}" style="max-width: 200px; max-height: 200px;" />'
        return "No profile picture uploaded"
    
    profile_picture_preview.allow_tags = True
    profile_picture_preview.short_description = "Profile Picture Preview"

@admin.register(AdminScreenshot)
class AdminScreenshotAdmin(admin.ModelAdmin):
    list_display = ['title', 'screenshot_type', 'created_at']
    list_filter = ['screenshot_type']
    readonly_fields = ['created_at']
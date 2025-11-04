from django.shortcuts import render
from .models import LearningJourney, AboutMe, AdminScreenshot

def index(request):
    """View for the learning journey page"""
    learning_items = LearningJourney.objects.all().order_by('-date_learned')
    journey_screenshots = AdminScreenshot.objects.filter(
        screenshot_type='learning_journey'
    ).order_by('-created_at')
    
    context = {
        'learning_items': learning_items,
        'journey_screenshots': journey_screenshots
    }
    return render(request, 'index.html', context)

def about_me(request):
    """View for the about me page"""
    about_info = AboutMe.objects.first()
    about_screenshots = AdminScreenshot.objects.filter(
        screenshot_type='about_me'
    ).order_by('-created_at')
    
    context = {
        'about_info': about_info,
        'about_screenshots': about_screenshots
    }
    return render(request, 'aboutMe.html', context)
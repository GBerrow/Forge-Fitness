from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from users.models import UserSettings, PracticeNote
from django.db.models import Count
from datetime import datetime, timedelta

@login_required
def dashboard(request):
    user = request.user
    
    # Get user's practice notes statistics
    recent_notes = PracticeNote.objects.filter(user=user).order_by('-created_at')[:5]
    total_notes = PracticeNote.objects.filter(user=user).count()
    
    # Notes by page type
    notes_by_page = PracticeNote.objects.filter(user=user).values('page').annotate(count=Count('page'))
    
    # Recent activity (last 7 days)
    week_ago = datetime.now() - timedelta(days=7)
    recent_activity = PracticeNote.objects.filter(user=user, created_at__gte=week_ago).count()
    
    # Quick stats
    stats = {
        'total_notes': total_notes,
        'recent_activity': recent_activity,
        'training_notes': PracticeNote.objects.filter(user=user, page='training').count(),
        'activity_notes': PracticeNote.objects.filter(user=user, page='activity').count(),
        'progression_notes': PracticeNote.objects.filter(user=user, page='progression').count(),
    }
    
    context = {
        'user': user,
        'recent_notes': recent_notes,
        'stats': stats,
        'notes_by_page': notes_by_page,
    }
    
    return render(request, 'dashboard.html', context)

@login_required
def settings(request):
    user = request.user
    
    # Get or create user settings
    user_settings, created = UserSettings.objects.get_or_create(user=user)
    
    if request.method == 'POST':
        if 'update_profile' in request.POST:
            try:
                # Handle profile updates with validation
                if 'profile_picture' in request.FILES:
                    picture = request.FILES['profile_picture']
                    
                    # Validate file size (5MB max)
                    if picture.size > 5 * 1024 * 1024:
                        messages.error(request, 'Image file too large (max 5MB)')
                        return redirect('settings')
                    
                    # Validate file type
                    if not picture.content_type.startswith('image/'):
                        messages.error(request, 'File must be an image')
                        return redirect('settings')
                    
                    user.profile_picture = picture
                
                bio = request.POST.get('bio', '').strip()
                if len(bio) > 500:
                    messages.error(request, 'Bio must be less than 500 characters')
                    return redirect('settings')
                    
                user.bio = bio
                user.save()
                messages.success(request, 'Profile updated successfully!')
                
            except Exception as e:
                messages.error(request, 'Error updating profile. Please try again.')
                
            return redirect('settings')
    
    return render(request, 'settings.html', {
        'user': user,
        'user_settings': user_settings
    })

def training(request):
    return render(request, 'training.html')

def activity(request):
    notes = PracticeNote.objects.filter(user=request.user, page='activity').order_by('-created_at')
    return render(request, 'activity.html', {'notes': notes})

def progression(request):
    return render(request, 'progression.html')

def profile(request):
    return render(request, 'profile.html')

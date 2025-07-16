from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib import messages
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .forms import SignupForm, PracticeNoteForm, TrainingNoteForm, UserProfileForm, UserSettingsForm, AccountDeleteForm
from .models import UserProfile, PracticeNote, UserSettings
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_protect
from django.views import View
from django.http import HttpResponse
from django.views.decorators.cache import never_cache
from django.contrib.auth.views import LoginView
from django.utils.decorators import method_decorator
from django.http import Http404
from django.shortcuts import render


@method_decorator(never_cache, name='dispatch')
class CustomLoginView(LoginView):
    template_name = 'login.html'
    
    def dispatch(self, request, *args, **kwargs):
        # If user is already logged in, redirect to dashboard
        if request.user.is_authenticated:
            return redirect('dashboard')
        return super().dispatch(request, *args, **kwargs)
    
    def get_success_url(self):
        return self.get_redirect_url() or '/dashboard/'

@never_cache
@csrf_protect
@require_http_methods(["GET", "POST"])
def custom_logout(request):
    """Custom logout view that completely clears session and prevents caching"""
    if request.user.is_authenticated:
        messages.success(request, 'You have been logged out successfully.')
        
        # Clear session data before logout
        request.session.flush()
        
        # Logout user
        logout(request)
        
        # Clear any remaining session data
        request.session.clear()
        request.session.cycle_key()
    
    # Create response with strong cache prevention
    response = redirect('login')
    
    # Prevent ALL caching
    response['Cache-Control'] = 'no-cache, no-store, must-revalidate, max-age=0, private'
    response['Pragma'] = 'no-cache'
    response['Expires'] = '0'
    response['Last-Modified'] = '0'
    
    return response

class SignupView(View):
    def get(self, request):
        form = SignupForm()
        return render(request, 'signup.html', {'form': form})

    def post(self, request):
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Create UserSettings for the new user
            UserSettings.objects.create(user=user)
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            messages.success(request, 'Welcome! Your account has been created.')
            return redirect('dashboard')
        return render(request, 'signup.html', {'form': form})

# Practice Notes CRUD
@login_required
def create_note(request, page):
    """Create a new practice note for a specific page"""
    if page not in ['training', 'activity', 'progression']:
        return redirect('dashboard')
    
    # Use specialized form for training page
    FormClass = TrainingNoteForm if page == 'training' else PracticeNoteForm
    
    if request.method == 'POST':
        form = FormClass(request.POST, page=page)
        if form.is_valid():
            note = form.save(commit=False)
            note.user = request.user
            note.page = page
            note.save()
            messages.success(request, 'Note added successfully!')
            return redirect(page)
    else:
        form = FormClass(page=page)
    
    return render(request, 'create_note.html', {
        'form': form,
        'page': page,
        'page_context': PracticeNote.get_page_context(page)
    })

@login_required
def edit_note(request, note_id):
    """Edit an existing practice note"""
    note = get_object_or_404(PracticeNote, id=note_id, user=request.user)
    
    # Use specialized form for training page
    FormClass = TrainingNoteForm if note.page == 'training' else PracticeNoteForm
    
    if request.method == 'POST':
        form = FormClass(request.POST, instance=note, page=note.page)
        if form.is_valid():
            form.save()
            messages.success(request, 'Note updated successfully!')
            return redirect(note.page)
    else:
        form = FormClass(instance=note, page=note.page)
    
    return render(request, 'edit_note.html', {
        'form': form,
        'note': note,
        'page_context': PracticeNote.get_page_context(note.page)
    })

@login_required
def delete_note(request, note_id):
    """Delete a practice note"""
    note = get_object_or_404(PracticeNote, id=note_id, user=request.user)
    
    if request.method == 'POST':
        page = note.page
        note.delete()
        messages.success(request, 'Note deleted successfully!')
        return redirect(page)
    
    return render(request, 'delete_note.html', {'note': note})

# Profile Management
@method_decorator(never_cache, name='dispatch')
class ProfileView(LoginRequiredMixin, DetailView):
    model = UserProfile
    template_name = 'profile.html'
    context_object_name = 'profile'

    def get_object(self):
        return self.request.user
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add user stats
        context['total_notes'] = PracticeNote.objects.filter(user=self.request.user).count()
        context['recent_notes'] = PracticeNote.objects.filter(user=self.request.user)[:5]
        context['training_notes'] = PracticeNote.objects.filter(user=self.request.user, page='training').count()
        context['activity_notes'] = PracticeNote.objects.filter(user=self.request.user, page='activity').count()
        context['progression_notes'] = PracticeNote.objects.filter(user=self.request.user, page='progression').count()
        return context

class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = UserProfile
    form_class = UserProfileForm
    template_name = 'profile_edit.html'
    success_url = reverse_lazy('profile')  

    def get_object(self):
        return self.request.user
    
    def form_valid(self, form):
        messages.success(self.request, 'Profile updated successfully!')
        return super().form_valid(form)

# Settings Management
@method_decorator(never_cache, name='dispatch')
class SettingsView(LoginRequiredMixin, View):
    def get(self, request):
        # Get or create user settings
        user_settings, created = UserSettings.objects.get_or_create(user=request.user)
        settings_form = UserSettingsForm(instance=user_settings)
        delete_form = AccountDeleteForm()
        
        return render(request, 'settings.html', {
            'settings_form': settings_form,
            'delete_form': delete_form,
            'user_settings': user_settings,
        })
    
    def post(self, request):
        user_settings, created = UserSettings.objects.get_or_create(user=request.user)
        
        if 'update_settings' in request.POST:
            settings_form = UserSettingsForm(request.POST, instance=user_settings)
            if settings_form.is_valid():
                settings_form.save()
                messages.success(request, 'Settings updated successfully!')
                return redirect('settings')
        
        elif 'delete_account' in request.POST:
            delete_form = AccountDeleteForm(request.POST)
            if delete_form.is_valid():
                # Log out the user first
                logout(request)
                # Delete the user account
                request.user.delete()
                messages.success(request, 'Account deleted successfully.')
                return redirect('signup')
            else:
                messages.error(request, 'Please type "DELETE" to confirm account deletion.')
        
        return redirect('settings')

# Keep the old AccountDeleteView for backward compatibility
class AccountDeleteView(LoginRequiredMixin, DeleteView):
    model = UserProfile
    template_name = 'settings.html'
    success_url = reverse_lazy('signup')

    def get_object(self):
        return self.request.user

def test_404_error(request):
    """Test view to simulate 404 error"""
    return render(request, '404.html', status=404)

def test_500_error(request):
    """Test view to simulate 500 error"""
    return render(request, '500.html', status=500)

def custom_404_view(request, exception=None):
    """Custom 404 handler that works in both DEBUG and production"""
    return render(request, '404.html', status=404)

def custom_500_view(request):
    """Custom 500 handler that works in both DEBUG and production"""
    return render(request, '500.html', status=500)
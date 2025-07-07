from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import View, DetailView, UpdateView, DeleteView
from django.contrib import messages
from .forms import SignupForm, LoginForm, PracticeNoteForm, UserProfileForm
from .models import UserProfile, PracticeNote

class SignupView(View):
    def get(self, request):
        form = SignupForm()
        return render(request, 'signup.html', {'form': form})

    def post(self, request):
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
        return render(request, 'signup.html', {'form': form})

@login_required
def create_note(request, page):
    """Create a new practice note for a specific page"""
    if page not in ['training', 'activity', 'progression']:
        return redirect('dashboard')
    
    if request.method == 'POST':
        form = PracticeNoteForm(request.POST, page=page)
        if form.is_valid():
            note = form.save(commit=False)
            note.user = request.user
            note.page = page
            note.save()
            messages.success(request, 'Note added successfully!')
            return redirect(page)  # Redirect back to the page
    else:
        form = PracticeNoteForm(page=page)
    
    return render(request, 'create_note.html', {
        'form': form,
        'page': page,
        'page_context': PracticeNote.get_page_context(page)
    })

@login_required
def edit_note(request, note_id):
    """Edit an existing practice note"""
    note = get_object_or_404(PracticeNote, id=note_id, user=request.user)
    
    if request.method == 'POST':
        form = PracticeNoteForm(request.POST, instance=note, page=note.page)
        if form.is_valid():
            form.save()
            messages.success(request, 'Note updated successfully!')
            return redirect(note.page)
    else:
        form = PracticeNoteForm(instance=note, page=note.page)
    
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

class ProfileView(LoginRequiredMixin, DetailView):
    model = UserProfile
    template_name = 'profile.html'
    context_object_name = 'profile'

    def get_object(self):
        return self.request.user

class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = UserProfile
    form_class = UserProfileForm
    template_name = 'profile.html'
    success_url = reverse_lazy('profile')

    def get_object(self):
        return self.request.user

class SettingsView(LoginRequiredMixin, UpdateView):
    model = UserProfile
    template_name = 'settings.html'
    fields = ['profile_picture', 'bio']
    success_url = reverse_lazy('profile')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['account_settings'] = self.request.user
        return context

class AccountDeleteView(LoginRequiredMixin, DeleteView):
    model = UserProfile
    template_name = 'settings.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user

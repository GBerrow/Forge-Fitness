from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def preferences(request):
    return render(request, 'settings/preferences.html')

@login_required
def notifications(request):
    return render(request, 'settings/notifications.html')

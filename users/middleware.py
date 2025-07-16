from django.contrib.auth import logout
from django.shortcuts import redirect
from django.urls import reverse

class SessionSecurityMiddleware:
    """Middleware to ensure session security and prevent back button access"""
    
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Check if user is accessing protected pages
        protected_paths = ['/dashboard/', '/profile/', '/settings/', '/activity/', '/training/', '/progression/']
        
        if any(request.path.startswith(path) for path in protected_paths):
            if not request.user.is_authenticated:
                return redirect('login')
        
        response = self.get_response(request)
        
        # Add cache control headers to all protected responses
        if hasattr(request, 'user') and request.user.is_authenticated:
            if any(request.path.startswith(path) for path in protected_paths):
                response['Cache-Control'] = 'no-cache, no-store, must-revalidate, max-age=0, private'
                response['Pragma'] = 'no-cache'
                response['Expires'] = '0'
        
        return response

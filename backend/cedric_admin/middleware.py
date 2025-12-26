"""
Middleware to restrict admin panel access to staff and superuser accounts only
"""
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth.models import AnonymousUser


class AdminAccessMiddleware:
    """
    Middleware that enforces admin panel access restrictions.
    Only staff and superuser accounts can access the admin panel.
    """

    def __init__(self, get_response):
        self.get_response = get_response
        self.admin_paths = ['admin']

    def __call__(self, request):
        # Check if the request is for admin path
        if any(request.path.startswith('/' + path) for path in self.admin_paths):
            # Allow access to login page
            if request.path.endswith('/login/') or request.path == '/admin/':
                if request.user.is_authenticated:
                    # If user is not staff/superuser, deny access
                    if not (request.user.is_staff or request.user.is_superuser):
                        return redirect('admin:index')
        
        response = self.get_response(request)
        return response

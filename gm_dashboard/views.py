"""
Views für das Dashboard Plugin
"""

from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse


class DashboardView(LoginRequiredMixin, View):
    """
    Dashboard View - Zeigt konfigurierte Links an
    """
    
    def get(self, request, *args, **kwargs):
        """Return simple HTML to test if URL routing works"""
        html = """
        <!DOCTYPE html>
        <html>
        <head>
            <title>Dashboard Plugin Test</title>
            <style>
                body { font-family: Arial, sans-serif; margin: 40px; background: #f5f5f5; }
                .container { background: white; padding: 40px; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1); }
                h1 { color: #1e3a8a; }
                .success { color: green; font-weight: bold; }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>Dashboard Plugin</h1>
                <p class="success">✓ URL-Routing funktioniert!</p>
                <p>Wenn du diese Seite siehst, funktioniert die URL-Registrierung korrekt.</p>
                <p>Plugin-Version: 0.0.14</p>
            </div>
        </body>
        </html>
        """
        return HttpResponse(html, content_type='text/html')

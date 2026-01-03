"""
Views für das Dashboard Plugin
"""

from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from plugin.registry import registry


class DashboardView(LoginRequiredMixin, TemplateView):
    """
    Dashboard View - Zeigt konfigurierte Links an
    """
    template_name = 'dashboard/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Plugin-Instanz holen
        try:
            plugin = registry.get_plugin('gm-dashboard')
        except Exception:
            plugin = None
            
        if not plugin:
            context['links'] = []
            context['dashboard_title'] = 'Dashboard'
            context['plugin_version'] = '0.0.7'
            return context

        # Dashboard-Titel aus Settings
        dashboard_title = plugin.get_setting('DASHBOARD_TITLE', 'Dashboard')
        context['dashboard_title'] = dashboard_title

        # Links aus Settings sammeln
        links = []
        try:
            for i in range(1, 13):
                title = plugin.get_setting(f'LINK_{i}_TITLE', '').strip()
                url = plugin.get_setting(f'LINK_{i}_URL', '').strip()
                icon = plugin.get_setting(f'LINK_{i}_ICON', '').strip()
                new_tab = plugin.get_setting(f'LINK_{i}_NEW_TAB', False)

                # Nur Links hinzufügen, wenn Titel und URL vorhanden sind
                if title and url:
                    # Sicherstellen, dass URL absolut ist (mit http:// oder https://)
                    if not url.startswith(('http://', 'https://', '//')):
                        url = 'https://' + url
                    
                    links.append({
                        'title': title,
                        'url': url,
                        'icon': icon,
                        'new_tab': new_tab,
                    })
        except Exception:
            links = []

        context['links'] = links
        context['plugin_version'] = plugin.VERSION if plugin else '0.0.7'

        return context


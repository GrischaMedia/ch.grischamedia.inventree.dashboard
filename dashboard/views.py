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
        plugin = registry.get_plugin('dashboard')
        if not plugin:
            context['links'] = []
            context['dashboard_title'] = 'Dashboard'
            return context

        # Dashboard-Titel aus Settings
        dashboard_title = plugin.get_setting('DASHBOARD_TITLE', 'Dashboard')
        context['dashboard_title'] = dashboard_title

        # Links aus Settings sammeln
        links = []
        for i in range(1, 13):
            title = plugin.get_setting(f'LINK_{i}_TITLE', '').strip()
            url = plugin.get_setting(f'LINK_{i}_URL', '').strip()
            icon = plugin.get_setting(f'LINK_{i}_ICON', '').strip()
            new_tab = plugin.get_setting(f'LINK_{i}_NEW_TAB', False)

            # Nur Links hinzufügen, wenn Titel und URL vorhanden sind
            if title and url:
                links.append({
                    'title': title,
                    'url': url,
                    'icon': icon,
                    'new_tab': new_tab,
                })

        context['links'] = links
        context['plugin_version'] = plugin.VERSION

        return context


"""
Dashboard Plugin für InvenTree
"""

from django.urls import path, include
from plugin import InvenTreePlugin
from plugin.mixins import SettingsMixin, UrlsMixin


class DashboardPlugin(SettingsMixin, UrlsMixin, InvenTreePlugin):
    """
    Dashboard Plugin - Zeigt benutzerdefinierte Links als Boxen an
    """

    NAME = "Dashboard"
    SLUG = "dashboard"
    TITLE = "Dashboard"
    DESCRIPTION = "Dashboard Plugin für InvenTree mit benutzerdefinierten Links"
    VERSION = "0.0.1"
    AUTHOR = "GrischaMedia"
    PUBLISH_DATE = "2025-01-01"
    LICENSE = "GPL-3.0"

    def setup_urls(self):
        """
        URL-Routing registrieren
        """
        return [
            path('dashboard/', include('dashboard.urls')),
        ]

    def get_settings(self):
        """
        Plugin Settings definieren
        """
        settings = {
            'DASHBOARD_TITLE': {
                'name': 'Dashboard Titel',
                'description': 'Titel des Dashboards (Standard: Dashboard)',
                'default': 'Dashboard',
            },
        }

        # Settings für bis zu 12 Links
        for i in range(1, 13):
            settings[f'LINK_{i}_TITLE'] = {
                'name': f'Link {i} - Titel',
                'description': f'Titel für Link {i}',
                'default': '',
            }
            settings[f'LINK_{i}_URL'] = {
                'name': f'Link {i} - URL',
                'description': f'URL für Link {i}',
                'default': '',
            }
            settings[f'LINK_{i}_ICON'] = {
                'name': f'Link {i} - Icon',
                'description': f'Optionales Icon für Link {i} (z.B. Font Awesome Klasse)',
                'default': '',
            }
            settings[f'LINK_{i}_NEW_TAB'] = {
                'name': f'Link {i} - In neuem Tab öffnen',
                'description': f'Soll Link {i} in einem neuen Tab geöffnet werden?',
                'default': False,
                'validator': bool,
            }

        # Standard-Link für GrischaMedia
        settings['LINK_1_TITLE']['default'] = 'GrischaMedia'
        settings['LINK_1_URL']['default'] = 'https://grischamedia.ch'

        return settings


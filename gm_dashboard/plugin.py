"""
Dashboard Plugin für InvenTree
"""

import logging
from plugin import InvenTreePlugin
from plugin.mixins import SettingsMixin, UrlsMixin

logger = logging.getLogger('inventree')


class DashboardPlugin(SettingsMixin, UrlsMixin, InvenTreePlugin):
    """
    Dashboard Plugin - Zeigt benutzerdefinierte Links als Boxen an
    """

    NAME = "Dashboard"
    SLUG = "gm-dashboard"
    TITLE = "Dashboard"
    DESCRIPTION = "Dashboard Plugin für InvenTree mit benutzerdefinierten Links"
    VERSION = "1.0.0"
    AUTHOR = "GrischaMedia"
    PUBLISH_DATE = "2025-01-01"
    LICENSE = "GPL-3.0"
    
    def __init__(self, *args, **kwargs):
        """Initialize plugin with logging"""
        logger.info(f"DashboardPlugin.__init__ called for {self.NAME} (SLUG: {self.SLUG})")
        super().__init__(*args, **kwargs)
        logger.info(f"DashboardPlugin.__init__ completed for {self.NAME}")

    def setup_urls(self):
        """
        URL-Routing registrieren
        """
        logger.info(f"=== DashboardPlugin.setup_urls START ===")
        logger.info(f"DashboardPlugin.setup_urls called for plugin: {self.NAME} (SLUG: {self.SLUG})")
        try:
            from . import urls
            logger.info(f"URLs imported successfully: {urls}")
            logger.info(f"URL patterns: {urls.urlpatterns}")
            logger.info(f"=== DashboardPlugin.setup_urls END ===")
            return urls.urlpatterns
        except Exception as e:
            logger.error(f"Error in setup_urls: {str(e)}", exc_info=True)
            raise

    SETTINGS = {
        'DASHBOARD_TITLE': {
            'name': 'Dashboard Titel',
            'description': 'Titel des Dashboards (Standard: Dashboard)',
            'default': 'Dashboard',
        },
        'LINK_1_TITLE': {
            'name': 'Link 1 - Titel',
            'description': 'Titel für Link 1',
            'default': 'GrischaMedia',
        },
        'LINK_1_URL': {
            'name': 'Link 1 - URL',
            'description': 'URL für Link 1',
            'default': 'https://grischamedia.ch',
        },
        'LINK_1_ICON': {
            'name': 'Link 1 - Icon',
            'description': 'Optionales Icon für Link 1 (z.B. Font Awesome Klasse)',
            'default': '',
        },
        'LINK_1_NEW_TAB': {
            'name': 'Link 1 - In neuem Tab öffnen',
            'description': 'Soll Link 1 in einem neuen Tab geöffnet werden?',
            'default': False,
            'validator': bool,
        },
        'LINK_2_TITLE': {
            'name': 'Link 2 - Titel',
            'description': 'Titel für Link 2',
            'default': '',
        },
        'LINK_2_URL': {
            'name': 'Link 2 - URL',
            'description': 'URL für Link 2',
            'default': '',
        },
        'LINK_2_ICON': {
            'name': 'Link 2 - Icon',
            'description': 'Optionales Icon für Link 2 (z.B. Font Awesome Klasse)',
            'default': '',
        },
        'LINK_2_NEW_TAB': {
            'name': 'Link 2 - In neuem Tab öffnen',
            'description': 'Soll Link 2 in einem neuen Tab geöffnet werden?',
            'default': False,
            'validator': bool,
        },
        'LINK_3_TITLE': {
            'name': 'Link 3 - Titel',
            'description': 'Titel für Link 3',
            'default': '',
        },
        'LINK_3_URL': {
            'name': 'Link 3 - URL',
            'description': 'URL für Link 3',
            'default': '',
        },
        'LINK_3_ICON': {
            'name': 'Link 3 - Icon',
            'description': 'Optionales Icon für Link 3 (z.B. Font Awesome Klasse)',
            'default': '',
        },
        'LINK_3_NEW_TAB': {
            'name': 'Link 3 - In neuem Tab öffnen',
            'description': 'Soll Link 3 in einem neuen Tab geöffnet werden?',
            'default': False,
            'validator': bool,
        },
        'LINK_4_TITLE': {
            'name': 'Link 4 - Titel',
            'description': 'Titel für Link 4',
            'default': '',
        },
        'LINK_4_URL': {
            'name': 'Link 4 - URL',
            'description': 'URL für Link 4',
            'default': '',
        },
        'LINK_4_ICON': {
            'name': 'Link 4 - Icon',
            'description': 'Optionales Icon für Link 4 (z.B. Font Awesome Klasse)',
            'default': '',
        },
        'LINK_4_NEW_TAB': {
            'name': 'Link 4 - In neuem Tab öffnen',
            'description': 'Soll Link 4 in einem neuen Tab geöffnet werden?',
            'default': False,
            'validator': bool,
        },
        'LINK_5_TITLE': {
            'name': 'Link 5 - Titel',
            'description': 'Titel für Link 5',
            'default': '',
        },
        'LINK_5_URL': {
            'name': 'Link 5 - URL',
            'description': 'URL für Link 5',
            'default': '',
        },
        'LINK_5_ICON': {
            'name': 'Link 5 - Icon',
            'description': 'Optionales Icon für Link 5 (z.B. Font Awesome Klasse)',
            'default': '',
        },
        'LINK_5_NEW_TAB': {
            'name': 'Link 5 - In neuem Tab öffnen',
            'description': 'Soll Link 5 in einem neuen Tab geöffnet werden?',
            'default': False,
            'validator': bool,
        },
        'LINK_6_TITLE': {
            'name': 'Link 6 - Titel',
            'description': 'Titel für Link 6',
            'default': '',
        },
        'LINK_6_URL': {
            'name': 'Link 6 - URL',
            'description': 'URL für Link 6',
            'default': '',
        },
        'LINK_6_ICON': {
            'name': 'Link 6 - Icon',
            'description': 'Optionales Icon für Link 6 (z.B. Font Awesome Klasse)',
            'default': '',
        },
        'LINK_6_NEW_TAB': {
            'name': 'Link 6 - In neuem Tab öffnen',
            'description': 'Soll Link 6 in einem neuen Tab geöffnet werden?',
            'default': False,
            'validator': bool,
        },
        'LINK_7_TITLE': {
            'name': 'Link 7 - Titel',
            'description': 'Titel für Link 7',
            'default': '',
        },
        'LINK_7_URL': {
            'name': 'Link 7 - URL',
            'description': 'URL für Link 7',
            'default': '',
        },
        'LINK_7_ICON': {
            'name': 'Link 7 - Icon',
            'description': 'Optionales Icon für Link 7 (z.B. Font Awesome Klasse)',
            'default': '',
        },
        'LINK_7_NEW_TAB': {
            'name': 'Link 7 - In neuem Tab öffnen',
            'description': 'Soll Link 7 in einem neuen Tab geöffnet werden?',
            'default': False,
            'validator': bool,
        },
        'LINK_8_TITLE': {
            'name': 'Link 8 - Titel',
            'description': 'Titel für Link 8',
            'default': '',
        },
        'LINK_8_URL': {
            'name': 'Link 8 - URL',
            'description': 'URL für Link 8',
            'default': '',
        },
        'LINK_8_ICON': {
            'name': 'Link 8 - Icon',
            'description': 'Optionales Icon für Link 8 (z.B. Font Awesome Klasse)',
            'default': '',
        },
        'LINK_8_NEW_TAB': {
            'name': 'Link 8 - In neuem Tab öffnen',
            'description': 'Soll Link 8 in einem neuen Tab geöffnet werden?',
            'default': False,
            'validator': bool,
        },
        'LINK_9_TITLE': {
            'name': 'Link 9 - Titel',
            'description': 'Titel für Link 9',
            'default': '',
        },
        'LINK_9_URL': {
            'name': 'Link 9 - URL',
            'description': 'URL für Link 9',
            'default': '',
        },
        'LINK_9_ICON': {
            'name': 'Link 9 - Icon',
            'description': 'Optionales Icon für Link 9 (z.B. Font Awesome Klasse)',
            'default': '',
        },
        'LINK_9_NEW_TAB': {
            'name': 'Link 9 - In neuem Tab öffnen',
            'description': 'Soll Link 9 in einem neuen Tab geöffnet werden?',
            'default': False,
            'validator': bool,
        },
        'LINK_10_TITLE': {
            'name': 'Link 10 - Titel',
            'description': 'Titel für Link 10',
            'default': '',
        },
        'LINK_10_URL': {
            'name': 'Link 10 - URL',
            'description': 'URL für Link 10',
            'default': '',
        },
        'LINK_10_ICON': {
            'name': 'Link 10 - Icon',
            'description': 'Optionales Icon für Link 10 (z.B. Font Awesome Klasse)',
            'default': '',
        },
        'LINK_10_NEW_TAB': {
            'name': 'Link 10 - In neuem Tab öffnen',
            'description': 'Soll Link 10 in einem neuen Tab geöffnet werden?',
            'default': False,
            'validator': bool,
        },
        'LINK_11_TITLE': {
            'name': 'Link 11 - Titel',
            'description': 'Titel für Link 11',
            'default': '',
        },
        'LINK_11_URL': {
            'name': 'Link 11 - URL',
            'description': 'URL für Link 11',
            'default': '',
        },
        'LINK_11_ICON': {
            'name': 'Link 11 - Icon',
            'description': 'Optionales Icon für Link 11 (z.B. Font Awesome Klasse)',
            'default': '',
        },
        'LINK_11_NEW_TAB': {
            'name': 'Link 11 - In neuem Tab öffnen',
            'description': 'Soll Link 11 in einem neuen Tab geöffnet werden?',
            'default': False,
            'validator': bool,
        },
        'LINK_12_TITLE': {
            'name': 'Link 12 - Titel',
            'description': 'Titel für Link 12',
            'default': '',
        },
        'LINK_12_URL': {
            'name': 'Link 12 - URL',
            'description': 'URL für Link 12',
            'default': '',
        },
        'LINK_12_ICON': {
            'name': 'Link 12 - Icon',
            'description': 'Optionales Icon für Link 12 (z.B. Font Awesome Klasse)',
            'default': '',
        },
        'LINK_12_NEW_TAB': {
            'name': 'Link 12 - In neuem Tab öffnen',
            'description': 'Soll Link 12 in einem neuen Tab geöffnet werden?',
            'default': False,
            'validator': bool,
        },
    }


"""
Views für das Dashboard Plugin
"""

import logging
from django.views.generic import View
from django.http import HttpResponse
from django.template.loader import render_to_string
from plugin.registry import registry

logger = logging.getLogger('inventree')


class DashboardView(View):
    """
    Dashboard View - Zeigt konfigurierte Links an
    """
    
    def dispatch(self, request, *args, **kwargs):
        """Override dispatch to add logging and check authentication"""
        logger.info(f"=== DashboardView.dispatch START ===")
        logger.info(f"Request path: {request.path}")
        logger.info(f"Request method: {request.method}")
        logger.info(f"User: {request.user}")
        logger.info(f"User authenticated: {request.user.is_authenticated}")
        
        # Check authentication
        if not request.user.is_authenticated:
            logger.warning("User not authenticated, redirecting to /web/")
            from django.http import HttpResponseRedirect
            return HttpResponseRedirect('/web/')
        
        logger.info("User is authenticated, proceeding with request")
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        """Handle GET request"""
        logger.info("=== DashboardView.get START ===")
        
        # Plugin-Instanz holen
        plugin = None
        try:
            plugin = registry.get_plugin('gm-dashboard')
            logger.info(f"Plugin found: {plugin is not None}")
            if plugin:
                logger.info(f"Plugin name: {plugin.NAME}, slug: {plugin.SLUG}, version: {plugin.VERSION}")
        except Exception as e:
            logger.error(f"Error getting plugin: {str(e)}", exc_info=True)
            
        # Standard-Werte setzen
        links = []
        dashboard_title = 'Dashboard'
        plugin_version = '0.0.22'
            
        if plugin:
            # Dashboard-Titel aus Settings
            try:
                dashboard_title = plugin.get_setting('DASHBOARD_TITLE', 'Dashboard')
                logger.info(f"Dashboard title: {dashboard_title}")
            except Exception as e:
                logger.error(f"Error getting dashboard title: {str(e)}")

            # Links aus Settings sammeln
            try:
                for i in range(1, 13):
                    try:
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
                    except Exception as e:
                        logger.error(f"Error processing link {i}: {str(e)}")
                        continue
                logger.info(f"Found {len(links)} links")
            except Exception as e:
                logger.error(f"Error getting links: {str(e)}", exc_info=True)

            try:
                plugin_version = plugin.VERSION
            except Exception:
                pass

        # Context für Template
        context = {
            'links': links,
            'dashboard_title': dashboard_title,
            'plugin_version': plugin_version,
        }
        
        logger.info(f"Context prepared with {len(links)} links")
        
        # Template rendern
        try:
            html = render_to_string('dashboard/dashboard.html', context, request=request)
            logger.info("Template rendered successfully")
            logger.info(f"=== DashboardView.get END ===")
            return HttpResponse(html, content_type='text/html')
        except Exception as e:
            logger.error(f"Error rendering template: {str(e)}", exc_info=True)
            return HttpResponse(f"Error rendering template: {str(e)}", status=500)

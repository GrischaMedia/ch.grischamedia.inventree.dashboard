"""
Views für das Dashboard Plugin
"""

import logging
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from plugin.registry import registry

logger = logging.getLogger('inventree')


@method_decorator(login_required, name='dispatch')
class DashboardView(TemplateView):
    """
    Dashboard View - Zeigt konfigurierte Links an
    """
    template_name = 'dashboard/dashboard.html'
    
    def dispatch(self, request, *args, **kwargs):
        """Override dispatch to add logging"""
        logger.info(f"=== DashboardView.dispatch START ===")
        logger.info(f"Request path: {request.path}")
        logger.info(f"Request method: {request.method}")
        logger.info(f"User: {request.user}")
        logger.info(f"User authenticated: {request.user.is_authenticated}")
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        """Get context data for template"""
        logger.info("=== DashboardView.get_context_data START ===")
        
        context = super().get_context_data(**kwargs)
        
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
        plugin_version = '1.0.0'
            
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

        # Context setzen
        context['links'] = links
        context['dashboard_title'] = dashboard_title
        context['plugin_version'] = plugin_version
        
        logger.info(f"Context prepared with {len(links)} links")
        logger.info(f"=== DashboardView.get_context_data END ===")
        
        return context

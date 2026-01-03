"""
Views für das Dashboard Plugin
"""

import logging
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from plugin.registry import registry

logger = logging.getLogger('inventree')


class DashboardView(LoginRequiredMixin, TemplateView):
    """
    Dashboard View - Zeigt konfigurierte Links an
    """
    template_name = 'dashboard/dashboard.html'
    login_url = '/web/'

    def dispatch(self, request, *args, **kwargs):
        """Override dispatch to add logging"""
        logger.info(f"DashboardView.dispatch called for user: {request.user}, authenticated: {request.user.is_authenticated}")
        logger.info(f"Request path: {request.path}")
        logger.info(f"Request method: {request.method}")
        
        try:
            result = super().dispatch(request, *args, **kwargs)
            logger.info(f"DashboardView.dispatch returning: {type(result)}")
            return result
        except Exception as e:
            logger.error(f"DashboardView.dispatch ERROR: {str(e)}", exc_info=True)
            return HttpResponse(f"Error in DashboardView.dispatch: {str(e)}", status=500)

    def get_context_data(self, **kwargs):
        logger.info("DashboardView.get_context_data called")
        context = super().get_context_data(**kwargs)

        # Plugin-Instanz holen
        plugin = None
        try:
            plugin = registry.get_plugin('gm-dashboard')
            logger.info(f"Plugin found: {plugin is not None}")
            if plugin:
                logger.info(f"Plugin name: {plugin.NAME}, slug: {plugin.SLUG}")
        except Exception as e:
            logger.error(f"Error getting plugin: {str(e)}", exc_info=True)
            
        # Standard-Werte setzen
        context['links'] = []
        context['dashboard_title'] = 'Dashboard'
        context['plugin_version'] = '0.0.21'
            
        if plugin:
            # Dashboard-Titel aus Settings
            try:
                dashboard_title = plugin.get_setting('DASHBOARD_TITLE', 'Dashboard')
                context['dashboard_title'] = dashboard_title
                logger.info(f"Dashboard title: {dashboard_title}")
            except Exception as e:
                logger.error(f"Error getting dashboard title: {str(e)}")

            # Links aus Settings sammeln
            links = []
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

            context['links'] = links
            try:
                context['plugin_version'] = plugin.VERSION
            except Exception:
                pass

        logger.info(f"Context prepared with {len(context.get('links', []))} links")
        return context

    def render_to_response(self, context, **response_kwargs):
        """Override to add logging"""
        logger.info("DashboardView.render_to_response called")
        try:
            result = super().render_to_response(context, **response_kwargs)
            logger.info(f"Template rendered successfully, status: {result.status_code}")
            return result
        except Exception as e:
            logger.error(f"Error rendering template: {str(e)}", exc_info=True)
            return HttpResponse(f"Error rendering template: {str(e)}", status=500)

"""
Views für das Dashboard Plugin
"""

from django.views.generic import View
from django.http import HttpResponse
from plugin.registry import registry


class DashboardView(View):
    """
    Dashboard View - Zeigt konfigurierte Links an
    """
    
    def dispatch(self, request, *args, **kwargs):
        """Override dispatch to check authentication without redirect"""
        if not request.user.is_authenticated:
            return HttpResponse("Not authenticated", status=401)
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request, *args, **kwargs):
        """Return simple HTML to test if URL routing works"""
        # Plugin-Instanz holen
        plugin = None
        try:
            plugin = registry.get_plugin('gm-dashboard')
        except Exception:
            pass
        
        # Standard-Werte
        dashboard_title = 'Dashboard'
        plugin_version = '0.0.17'
        links = []
        
        if plugin:
            try:
                dashboard_title = plugin.get_setting('DASHBOARD_TITLE', 'Dashboard')
                plugin_version = plugin.VERSION
            except Exception:
                pass
            
            # Links aus Settings sammeln
            try:
                for i in range(1, 13):
                    try:
                        title = plugin.get_setting(f'LINK_{i}_TITLE', '').strip()
                        url = plugin.get_setting(f'LINK_{i}_URL', '').strip()
                        icon = plugin.get_setting(f'LINK_{i}_ICON', '').strip()
                        new_tab = plugin.get_setting(f'LINK_{i}_NEW_TAB', False)

                        if title and url:
                            if not url.startswith(('http://', 'https://', '//')):
                                url = 'https://' + url
                            
                            links.append({
                                'title': title,
                                'url': url,
                                'icon': icon,
                                'new_tab': new_tab,
                            })
                    except Exception:
                        continue
            except Exception:
                pass
        
        # Generate HTML
        html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>{dashboard_title}</title>
            <style>
                body {{ font-family: Arial, sans-serif; margin: 40px; background: #f5f5f5; }}
                .container {{ background: white; padding: 40px; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1); }}
                .header {{ background: #1e3a8a; color: white; padding: 20px; border-radius: 8px; margin-bottom: 20px; }}
                .version {{ background: rgba(255,255,255,0.2); padding: 4px 12px; border-radius: 12px; display: inline-block; }}
                .links {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 20px; margin-top: 20px; }}
                .link-box {{ background: #f8f9fa; border: 2px solid #e9ecef; border-radius: 8px; padding: 24px; text-align: center; text-decoration: none; color: inherit; display: block; }}
                .link-box:hover {{ transform: translateY(-4px); box-shadow: 0 4px 12px rgba(0,0,0,0.15); border-color: #3b82f6; }}
                h1 {{ margin: 0; }}
                .success {{ color: green; font-weight: bold; }}
            </style>
        </head>
        <body>
            <div class="container">
                <div class="header">
                    <h1>{dashboard_title} <span class="version">V{plugin_version}</span></h1>
                </div>
        """
        
        if links:
            html += '<div class="links">'
            for link in links:
                target = 'target="_blank" rel="noopener noreferrer"' if link['new_tab'] else ''
                icon_html = f'<div style="font-size: 48px; margin-bottom: 16px;">{link["icon"] if link["icon"] else "🔗"}</div>' if link.get('icon') else '<div style="font-size: 48px; margin-bottom: 16px;">🔗</div>'
                html += f'''
                <a href="{link['url']}" class="link-box" {target}>
                    {icon_html}
                    <h3>{link['title']}</h3>
                </a>
                '''
            html += '</div>'
        else:
            html += '<p>Keine Links konfiguriert. Bitte konfigurieren Sie Links in den Plugin-Einstellungen.</p>'
        
        html += """
                <div style="text-align: center; margin-top: 40px; color: #6c757d;">
                    <p>© 2025 GrischaMedia</p>
                </div>
            </div>
        </body>
        </html>
        """
        
        return HttpResponse(html, content_type='text/html')

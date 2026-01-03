# Debugging-Befehle für Portainer

## 1. Plugin-Status prüfen
```bash
# In den inventree-server Container gehen
docker exec -it <container-name> python manage.py shell

# Dann in der Python-Shell:
from plugin.registry import registry
plugins = registry.plugins
for slug, plugin in plugins.items():
    print(f"Plugin: {slug} - {plugin.NAME} - Active: {plugin.active}")

# Speziell unser Plugin prüfen:
plugin = registry.get_plugin('gm-dashboard')
if plugin:
    print(f"Plugin gefunden: {plugin.NAME}")
    print(f"Active: {plugin.active}")
    print(f"URLs: {plugin.setup_urls()}")
else:
    print("Plugin nicht gefunden!")
```

## 2. URL-Registrierung prüfen
```bash
# In den inventree-server Container gehen
docker exec -it <container-name> python manage.py shell

# Dann in der Python-Shell:
from django.urls import get_resolver
resolver = get_resolver()
url_patterns = resolver.url_patterns

# Plugin-URLs finden
for pattern in url_patterns:
    if hasattr(pattern, 'url_patterns'):
        for p in pattern.url_patterns:
            if 'gm-dashboard' in str(p.pattern):
                print(f"URL gefunden: {p.pattern} -> {p.callback}")
```

## 3. Plugin-Import testen
```bash
# In den inventree-server Container gehen
docker exec -it <container-name> python manage.py shell

# Dann in der Python-Shell:
try:
    from gm_dashboard import DashboardPlugin
    print("✓ Plugin import erfolgreich")
    print(f"SLUG: {DashboardPlugin.SLUG}")
    print(f"NAME: {DashboardPlugin.NAME}")
    
    # URLs testen
    plugin = DashboardPlugin()
    urls = plugin.setup_urls()
    print(f"URLs: {urls}")
except Exception as e:
    print(f"✗ Fehler: {e}")
    import traceback
    traceback.print_exc()
```

## 4. View direkt testen
```bash
# In den inventree-server Container gehen
docker exec -it <container-name> python manage.py shell

# Dann in der Python-Shell:
from gm_dashboard.views import DashboardView
from django.test import RequestFactory
from django.contrib.auth.models import User

# Test-Request erstellen
factory = RequestFactory()
request = factory.get('/plugin/gm-dashboard/')
request.user = User.objects.first()  # Ersten User nehmen

# View testen
view = DashboardView()
try:
    response = view.get(request)
    print(f"Response Status: {response.status_code}")
    print(f"Response Content: {response.content[:200]}")
except Exception as e:
    print(f"✗ Fehler: {e}")
    import traceback
    traceback.print_exc()
```

## 5. Alle registrierten URLs anzeigen
```bash
# In den inventree-server Container gehen
docker exec -it <container-name> python manage.py show_urls | grep -i dashboard
```

## 6. Plugin-Logs prüfen
```bash
# In den inventree-server Container gehen
docker exec -it <container-name> tail -f /path/to/inventree/logs/*.log
```

## 7. Plugin-Installation prüfen
```bash
# In den inventree-server Container gehen
docker exec -it <container-name> pip show ch.grischamedia.inventree.dashboard
```

## 8. Plugin neu laden
```bash
# In den inventree-server Container gehen
docker exec -it <container-name> python manage.py reload_plugins
```


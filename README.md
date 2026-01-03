# ch.grischamedia.inventree.dashboard

InvenTree Plugin für ein **benutzerdefiniertes Dashboard** mit konfigurierbaren Links.

## Funktion

Das Plugin stellt eine Dashboard-Seite bereit unter: **`/plugin/gm-dashboard/`** (Trailing Slash wichtig)

Auf dieser Seite werden konfigurierte Links als moderne Boxen in einem Grid-Layout angezeigt.

### Features

* Konfigurierbarer Dashboard-Titel (Standard: "Dashboard")
* Bis zu 12 benutzerdefinierte Links
* Jeder Link kann einen Titel, URL, optionales Icon und Option für neues Tab haben
* Moderne Grid-Ansicht für die Links
* Nur ausgefüllte Links werden angezeigt
* Integration in InvenTree Benutzerrechte

## Plugin Settings

* **DASHBOARD_TITLE**: Titel des Dashboards (Standard: "Dashboard")
* **LINK_X_TITLE**: Titel für Link X (1-12)
* **LINK_X_URL**: URL für Link X (1-12)
* **LINK_X_ICON**: Optionales Icon für Link X (1-12)
* **LINK_X_NEW_TAB**: Link in neuem Tab öffnen (1-12)

## Installation (Development)

Im gleichen Python-Environment wie dein InvenTree-Server:

```bash
pip install -e .
```

Danach InvenTree neu starten und im Admin unter **Plugin Settings** aktivieren.

## Installation (Production / Docker / Portainer)

Voraussetzung:

* In InvenTree ist **Plugin Support** aktiv
* In der Server-Konfiguration ist **ENABLE_PLUGINS_URL** aktiv, damit `/plugin/...` erreichbar ist

### Variante A: Installation über InvenTree UI

* In InvenTree als Admin: **Settings → Plugin Settings**
* Plugin installieren (z.B. via Git URL oder Paketname)
* **Server & Worker neu starten**

### Variante B: Installation per `plugins.txt`

InvenTree kann Plugins beim Start automatisch installieren, wenn **Check Plugins on Startup** aktiv ist.

1. In deinem InvenTree Config-Verzeichnis eine `plugins.txt` anlegen/erweitern
2. Eintrag hinzufügen:  
   `git+https://github.com/GrischaMedia/ch.grischamedia.inventree.dashboard.git@master`
3. Container neu starten

## Nutzung

Öffne die Seite:

* `https://<dein-host>/plugin/gm-dashboard/`

Konfiguriere Links in den Plugin-Einstellungen:

* **Settings → Plugin Settings → Dashboard**
* Links 1-12 konfigurieren
* Nur ausgefüllte Links werden auf dem Dashboard angezeigt

## Autor

GrischaMedia.ch

## Lizenz

GPL-3.0


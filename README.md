***

Den API-Key erzeugst du hier
https://github.com/settings/personal-access-tokens

# remFork (fork repository entferner)

Ein einfaches Python-Skript zum schnellen Auffinden und Löschen aller geforkten Repositories in deinem GitHub-Account.

## Achtung

**Dieses Skript löscht Repositories unwiderruflich!** Eine Wiederherstellung ist nicht möglich. Nutze es mit Bedacht und überprüfe die Liste der zu löschenden Forks sorgfältig, bevor du den Vorgang bestätigst.

## Voraussetzungen

Bevor du das Skript ausführen kannst, stelle sicher, dass die folgenden Punkte erfüllt sind:

1. **Python 3** ist auf deinem System installiert.
2. sofern du **`PyGithub`** nicht hast, installiere dies mit 

```bash
pip install PyGithub
```

3. Ein **GitHub Personal Access Token (Classic)** ist erforderlich.
    * Erstelle einen neuen Token unter **[GitHub Developer Settings](https://github.com/settings/tokens)**.
    * Vergib einen aussagekräftigen Namen für den Token (z.B. "fork-deleter-script").
    * Wähle die Berechtigungen (**Scopes**) aus. Du benötigst zwingend:
        * `repo` (um auf deine Repositories zugreifen zu können, auch private)
        * `delete_repo` (um Repositories löschen zu dürfen)
    * Kopiere den Token und bewahre ihn sicher auf. Er wird nur einmal angezeigt.

## Anwendung

1. **speichern**: Speichere das Script `main.py`.
2. **ausführen**: das Skript mit folgendem Befehl:

```bash
python main.py
```

4. **Anweisungen folgen**:
    * Du wirst aufgefordert, deinen **Personal Access Token** einzufügen.
    * Das Skript meldet sich an und listet alle Repositories auf, die es als Forks identifiziert hat.
    * Anschließend musst du den Löschvorgang durch die Eingabe von `ja` explizit bestätigen. Gibst du etwas anderes ein, wird das Skript sicherheitshalber abgebrochen.

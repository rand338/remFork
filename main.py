import sys
from github import Github, GithubException

def main():
    # 1. Token abfragen
    token = input("Bitte gib deinen GitHub Personal Access Token ein: ").strip()
    if not token:
        print("Kein Token eingegeben. Abbruch.")
        sys.exit(1)

    try:
        # 2. Anmeldung bei GitHub
        g = Github(token)
        user = g.get_user()
        username = user.login
        print(f"\nAngemeldet als: {username}")
        print("Lade Repository-Liste... (das kann einen Moment dauern)")

        # 3. Alle Forks finden
        # get_repos() holt alle Repositories des authentifizierten Users
        # 'affiliation="owner"' stellt sicher, dass wir nur eigene Repos bearbeiten
        repos = user.get_repos(affiliation="owner")
        
        forks_to_delete = []
        
        for repo in repos:
            if repo.fork:
                forks_to_delete.append(repo)
                print(f"  [Gefunden] {repo.full_name}")

        count = len(forks_to_delete)

        if count == 0:
            print("\nKeine Forks gefunden. Skript beendet.")
            sys.exit(0)

        # 4. Sicherheitsabfrage
        print(f"\nACHTUNG: Es wurden {count} Forks gefunden.")
        print("Diese Repositories werden UNWIDERRUFLICH gelöscht!")
        print("-" * 40)
        for repo in forks_to_delete:
            print(f"- {repo.full_name}")
        print("-" * 40)
        
        confirm = input(f"Bist du sicher, dass du diese {count} Repositories löschen willst? (ja/nein): ")

        if confirm.lower() != "ja":
            print("Abbruch. Nichts wurde gelöscht.")
            sys.exit(0)

        # 5. Löschvorgang
        print("\nStarte Löschvorgang...")
        for repo in forks_to_delete:
            try:
                print(f"Lösche {repo.full_name} ... ", end="")
                repo.delete()
                print("ERLEDIGT")
            except GithubException as e:
                print(f"FEHLER ({e.status}: {e.data.get('message', 'Unbekannter Fehler')})")

        print("\nFertig.")

    except GithubException as e:
        print(f"\nGitHub API Fehler: {e.status}")
        print(f"Nachricht: {e.data.get('message', '')}")
        print("Überprüfe deinen Token und ob er die Berechtigung 'delete_repo' hat.")
    except Exception as e:
        print(f"\nEin unerwarteter Fehler ist aufgetreten: {e}")

if __name__ == "__main__":
    main()
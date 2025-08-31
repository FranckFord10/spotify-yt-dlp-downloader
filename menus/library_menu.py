import questionary
from library.browser import browse_tracks, browse_playlists
from library.player import play_track, play_playlist
from utils.system import safe_execute
from utils.logger import log_info

def library_menu(config):
    """
    Displays the Library menu and handles user interactions.
    """
    while True:
        choice = questionary.select(
            "🎵 Library Menu — What would you like to do?",
            choices=[
                "Browse Tracks",
                "Browse Playlists",
                "Back"
            ]
        ).ask()

        if choice == "Browse Tracks":
            safe_execute(browse_tracks, config)

        elif choice == "Browse Playlists":
            safe_execute(browse_playlists, config)

        elif choice == "Back":
            log_info("Returning to main menu...")
            break

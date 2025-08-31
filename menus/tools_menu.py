import questionary
from utils.logger import log_info
from utils.system import system_check

# Import tools
from tools.library_cleanup import library_cleanup
from tools.playlist_to_tracklist import playlist_to_tracklist
from tools.dependency_check import dependency_check
from tools.library_export_json import library_export_json
from tools.compress_music import compress_music
from tools.choose_audio_format import choose_audio_format
from tools.open_log import open_log

def tools_menu(config):
    """
    Displays the Tools Menu for extra utilities.
    The menu only handles user choice and delegates logic to tools.
    """
    while True:
        choice = questionary.select(
            "🛠 Tools Menu — Select a tool:",
            choices=[
                "System check",
                "Library cleanup from broken files",
                "Playlist to track list",
                "Dependency check",
                "Library export as JSON",
                "Compress music",
                "Choose audio format",
                "Open log",
                "Help",
                "Back"
            ]
        ).ask()

        if not choice or choice == "Back":
            break

        try:
            if choice == "System check":
                system_check()

            elif choice == "Library cleanup from broken files":
                library_cleanup(config)

            elif choice == "Playlist to track list":
                playlist_to_tracklist(config)

            elif choice == "Dependency check":
                dependency_check()

            elif choice == "Library export as JSON":
                library_export_json(config)

            elif choice == "Compress music":
                compress_music(config)

            elif choice == "Choose audio format":
                choose_audio_format(config)
            
            elif choice == "Open log":
                open_log()

            elif choice == "Help":
                log_info("Help: Use yt-dlp for YouTube downloads. Modify config.json to change settings.")
                log_info("If you get many failed downloads, upgrade YT-DLP using: pip install --upgrade yt-dlp")

        except Exception as e:
            log_info(f"Error running tool '{choice}': {e}")

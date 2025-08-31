## Changelog

All notable changes to this project will be documented in this file.

Here’s what you asked for, following your style and structure:

---

### 0.4.1 - 2025-AUG-21

### Changed

- Better Logging for failed downloads
- Upgrade guide for YT-DLP in case of failed downloads

---

### 0.4.0 - 2025-AUG-21

### Added

- Ability to download playlists directly from Exportify CSV files placed in data/exportify/.
    - CSVs are auto-scanned, playlists confirmed with the user, and batch downloaded.

### Changed
- removed shutil and added python version (from merge request, thank you Artisan Memory)
- added tqdm to requirements.txt

---

### 0.3.0 - 2025-AUG-13

### Added

- Download from youtube using links (playlist or video) as audio format

---

### 0.2.0 - 2025-AUG-11

### Added

- Centralized all constants (audio formats, bitrates, dependencies, file paths) into a single `constants.py` file.
- Added system dependency checks for required binaries like `yt-dlp` and `ffmpeg`.
- Improved missing dependency detection to distinguish between Python packages and system binaries.
- Added descriptive bitrate choices with explanations to inform users of quality/size tradeoffs.
- Added function to open the app’s log file (`app.log`) directly in Notepad for easy debugging.

### Changed

- Updated dependency checker to avoid false positives for standard libraries (e.g., `shutil`).
- Enhanced “choose audio format” menu to always highlight the currently active format.
- Refactored code to use constants from the centralized constants file instead of hardcoded values.

### Fixed

- Fixed incorrect missing dependency for system binaries and stdlib modules.
- Improved error messages and logging for missing dependencies.

---

### 0.1.0 - 2025-AUG-09

### Added
- Support for importing playlists from Spotify’s playlist files.
- Option to download entire playlists in bulk or pick individual playlists.
- New interactive menu system replacing numbered menus.

### Changed
- Menus are now organized into their own sub-directory (`menus/`) for better project structure.
- Playlist import removed as it wasn't working, switched with new playlist file usage directly

### Fixed
- Bug fix: program no longer crashes when `failed_downloads.json` is empty.
- Bug fix: Weird behavior when no song or artist name are given when searching for a track
- Bug fix: "Unknown Artist" used when no artist name is given
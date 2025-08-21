import os
import csv
from utils.logger import log_info, log_warning, log_error

def load_tracks(tracks_file):
    import json
    try:
        with open(tracks_file, "r", encoding="utf-8") as f:
            return json.load(f)["tracks"]
    except Exception as e:
        log_error(f"Error loading tracks file: {e}")
        return []


def load_playlists(playlists_file):
    import json
    try:
        with open(playlists_file, "r", encoding="utf-8") as f:
            return json.load(f)["playlists"]
    except Exception as e:
        log_error(f"Error loading playlists file: {e}")
        return []


def load_exportify_playlists(exportify_dir="data/exportify"):
    """
    Scans the exportify folder for CSV files and parses them into playlist dicts.
    Each playlist dict matches your normal playlist structure:
    {
        "name": "Playlist Name",
        "tracks": [
            {"artist": "Artist Name", "track": "Track Name"},
            ...
        ]
    }
    """
    playlists = []
    if not os.path.exists(exportify_dir):
        return playlists

    for file in os.listdir(exportify_dir):
        if not file.lower().endswith(".csv"):
            continue

        playlist_name = os.path.splitext(file)[0]
        playlist_path = os.path.join(exportify_dir, file)

        tracks = []
        with open(playlist_path, newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                artist = row.get("Artist Name(s)", "").strip()
                track = row.get("Track Name", "").strip()
                if artist and track:
                    tracks.append({"artist": artist, "track": track})

        if tracks:
            playlists.append({
                "name": playlist_name,
                "tracks": tracks
            })

    return playlists

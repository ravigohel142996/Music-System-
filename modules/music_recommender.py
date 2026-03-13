"""
music_recommender.py
Recommends songs based on detected mood using the local songs.csv dataset.
Optionally integrates with Spotify for richer metadata and previews.
"""

import json
import os
import random
from typing import Dict, List, Optional

import pandas as pd

# Path to data files relative to project root
_DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "data")
_SONGS_CSV = os.path.join(_DATA_DIR, "songs.csv")
_PLAYLISTS_JSON = os.path.join(_DATA_DIR, "mood_playlists.json")


def load_songs() -> pd.DataFrame:
    """Load the songs dataset from CSV."""
    df = pd.read_csv(_SONGS_CSV)
    df.columns = [c.strip() for c in df.columns]
    return df


def load_playlist_config() -> Dict:
    """Load mood-to-playlist configuration from JSON."""
    with open(_PLAYLISTS_JSON, "r", encoding="utf-8") as f:
        return json.load(f)


def get_recommendations(
    mood: str,
    top_n: int = 6,
    shuffle: bool = True,
) -> List[Dict]:
    """
    Return recommended songs for a given mood.

    Args:
        mood: Detected emotion label (e.g. 'Happy', 'Sad').
        top_n: Maximum number of songs to return.
        shuffle: If True, shuffle results for variety.

    Returns:
        List of song dictionaries.
    """
    df = load_songs()
    mood_songs = df[df["mood"].str.lower() == mood.lower()]

    if mood_songs.empty:
        # Fallback to neutral if no songs found for mood
        mood_songs = df[df["mood"].str.lower() == "neutral"]

    if shuffle:
        mood_songs = mood_songs.sample(frac=1, random_state=random.randint(0, 999))

    subset = mood_songs.head(top_n)
    return subset.to_dict(orient="records")


def get_playlist_info(mood: str) -> Dict:
    """
    Return the playlist configuration metadata for a mood.

    Args:
        mood: Emotion label.

    Returns:
        Dictionary with mood metadata (genres, description, vibe_message, etc.).
    """
    config = load_playlist_config()
    # Case-insensitive lookup with neutral fallback
    for key, value in config.items():
        if key.lower() == mood.lower():
            return value
    return config.get("Neutral", {})


def get_all_moods() -> List[str]:
    """Return the list of all moods available in the dataset."""
    df = load_songs()
    return sorted(df["mood"].unique().tolist())


def get_mood_distribution() -> Dict[str, int]:
    """Return a count of songs per mood for analytics."""
    df = load_songs()
    return df["mood"].value_counts().to_dict()


def search_songs(query: str, mood: Optional[str] = None) -> List[Dict]:
    """
    Search songs by title or artist, optionally filtered by mood.

    Args:
        query: Search string.
        mood: Optional mood filter.

    Returns:
        List of matching song dictionaries.
    """
    df = load_songs()
    mask = (
        df["title"].str.contains(query, case=False, na=False)
        | df["artist"].str.contains(query, case=False, na=False)
    )
    if mood:
        mask &= df["mood"].str.lower() == mood.lower()
    return df[mask].to_dict(orient="records")

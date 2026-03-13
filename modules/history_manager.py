"""
history_manager.py
Manages session history of mood detections and music recommendations.
Uses Streamlit session_state as the backing store.
"""

from datetime import datetime
from typing import Dict, List, Optional

import streamlit as st


def _ensure_history() -> None:
    """Initialise the history list in session_state if not already present."""
    if "detection_history" not in st.session_state:
        st.session_state["detection_history"] = []


def add_entry(
    emotion: str,
    confidence: float,
    songs: List[Dict],
    method: str = "AI",
    image_label: Optional[str] = None,
) -> None:
    """
    Append a new detection result to the session history.

    Args:
        emotion: Detected emotion label.
        confidence: Confidence score (0-100).
        songs: List of recommended song dicts.
        method: Detection backend used.
        image_label: Optional short label for the input image.
    """
    _ensure_history()
    entry = {
        "timestamp": datetime.now().strftime("%H:%M:%S"),
        "emotion": emotion,
        "confidence": confidence,
        "songs": songs,
        "method": method,
        "image_label": image_label or "Uploaded Image",
    }
    st.session_state["detection_history"].insert(0, entry)


def get_history() -> List[Dict]:
    """
    Retrieve the full session history (most recent first).

    Returns:
        List of history entry dictionaries.
    """
    _ensure_history()
    return st.session_state["detection_history"]


def clear_history() -> None:
    """Clear all session history entries."""
    st.session_state["detection_history"] = []


def get_history_summary() -> Dict[str, int]:
    """
    Summarise how many times each emotion was detected in this session.

    Returns:
        Dictionary mapping emotion label → count.
    """
    history = get_history()
    summary: Dict[str, int] = {}
    for entry in history:
        emotion = entry.get("emotion", "Unknown")
        summary[emotion] = summary.get(emotion, 0) + 1
    return summary


def get_average_confidence() -> Optional[float]:
    """
    Calculate the average confidence across all session detections.

    Returns:
        Average confidence as a float, or None if history is empty.
    """
    history = get_history()
    if not history:
        return None
    total = sum(e.get("confidence", 0) for e in history)
    return round(total / len(history), 1)

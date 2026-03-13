"""
insights.py
Generates human-readable explanations and smart insights about mood detection.
"""

from typing import Dict

# Map of emotion → explanation template
EMOTION_EXPLANATIONS = {
    "Happy": (
        "Detected uplifted cheeks, a genuine smile, and bright eye crinkles — "
        "classic markers of authentic happiness. Upbeat, energetic music will amplify your mood!"
    ),
    "Sad": (
        "Detected drooping corners of the mouth and softened brow muscles — "
        "subtle indicators of sadness. Soothing, healing music can provide comfort and emotional release."
    ),
    "Angry": (
        "Detected furrowed brows, tightened jaw muscles, and compressed lips — "
        "strong indicators of frustration or anger. Powerful music can help you channel and release this energy."
    ),
    "Neutral": (
        "Detected a relaxed, symmetric facial expression with no dominant emotional signals. "
        "A balanced, eclectic playlist will keep you engaged and entertained."
    ),
    "Surprise": (
        "Detected raised eyebrows, widened eyes, and a slightly open mouth — "
        "classic signs of surprise or excitement. Dynamic, genre-hopping music matches your unpredictable energy."
    ),
    "Relaxed": (
        "Detected soft, relaxed facial muscles with minimal tension — "
        "a hallmark of deep calm. Ambient, peaceful music will deepen your sense of tranquility."
    ),
}

# Tips per mood
MOOD_TIPS = {
    "Happy": [
        "Share your positive energy — call a friend or dance with someone!",
        "This is a great time for creative work or social activities.",
        "Capture the moment — write in a gratitude journal.",
    ],
    "Sad": [
        "It's okay to feel sad — allow yourself to process these emotions.",
        "Consider a gentle walk in nature to lift your spirits.",
        "Reach out to a trusted friend or family member for support.",
    ],
    "Angry": [
        "Try deep breathing: inhale for 4 counts, hold for 4, exhale for 4.",
        "Physical exercise is a great way to release pent-up energy.",
        "Write down what's bothering you to gain clarity.",
    ],
    "Neutral": [
        "A great time to tackle that task you've been putting off.",
        "Try something new today — learn a skill or explore a hobby.",
        "Mindful meditation can deepen your sense of balance.",
    ],
    "Surprise": [
        "Embrace the unexpected — spontaneity often leads to amazing experiences.",
        "Document your reaction — it could make for a great story!",
        "Channel your heightened awareness into something creative.",
    ],
    "Relaxed": [
        "Perfect time for mindfulness, meditation, or gentle yoga.",
        "Read a book or explore a topic you're curious about.",
        "Savour this calm state — a relaxed mind is a creative mind.",
    ],
}

# Energy mapping for the UI badge
ENERGY_LEVEL_MAP = {
    "Happy": {"level": "High Energy", "icon": "⚡", "color": "#FFD700"},
    "Sad": {"level": "Low Energy", "icon": "💧", "color": "#4A90D9"},
    "Angry": {"level": "Intense Energy", "icon": "🔥", "color": "#FF4444"},
    "Neutral": {"level": "Balanced Energy", "icon": "⚖️", "color": "#9B9B9B"},
    "Surprise": {"level": "Dynamic Energy", "icon": "✨", "color": "#FF8C00"},
    "Relaxed": {"level": "Calm Energy", "icon": "🌊", "color": "#7ED8A3"},
}


def get_explanation(emotion: str, confidence: float) -> str:
    """
    Return a human-readable explanation for why a mood was detected.

    Args:
        emotion: Detected emotion label.
        confidence: Confidence score (0-100).

    Returns:
        Explanation string.
    """
    base = EMOTION_EXPLANATIONS.get(emotion, "Facial analysis detected this emotional state.")
    conf_str = (
        "with high certainty"
        if confidence >= 70
        else "with moderate certainty"
        if confidence >= 45
        else "with some uncertainty"
    )
    return f"{base} (Detected {conf_str} — {confidence:.0f}% confidence)"


def get_mood_tip(emotion: str) -> str:
    """
    Return a contextual wellness tip for the detected mood.

    Args:
        emotion: Detected emotion label.

    Returns:
        A single tip string.
    """
    import random  # noqa: PLC0415

    tips = MOOD_TIPS.get(emotion, ["Take a moment to breathe and check in with yourself."])
    return random.choice(tips)


def get_energy_info(emotion: str) -> Dict:
    """
    Return energy level metadata for the given emotion.

    Args:
        emotion: Detected emotion label.

    Returns:
        Dictionary with 'level', 'icon', and 'color' keys.
    """
    return ENERGY_LEVEL_MAP.get(
        emotion,
        {"level": "Balanced Energy", "icon": "⚖️", "color": "#9B9B9B"},
    )


def build_recommendation_summary(
    emotion: str,
    confidence: float,
    songs: list,
    method: str = "AI",
) -> str:
    """
    Build a downloadable plain-text summary of the session recommendation.

    Args:
        emotion: Detected emotion.
        confidence: Confidence score.
        songs: List of recommended song dicts.
        method: Detection method used.

    Returns:
        Formatted string ready to download as .txt.
    """
    lines = [
        "=" * 50,
        "  MUSIC SELECTION SYSTEM — RECOMMENDATION SUMMARY",
        "=" * 50,
        f"  Detected Mood   : {emotion}",
        f"  Confidence      : {confidence:.1f}%",
        f"  Detection Method: {method}",
        "",
        "  RECOMMENDED SONGS",
        "-" * 50,
    ]
    for i, song in enumerate(songs, 1):
        lines.append(f"  {i}. {song.get('title', 'Unknown')} — {song.get('artist', 'Unknown')}")
        lines.append(f"     Genre: {song.get('genre', 'N/A')} | Energy: {song.get('energy_level', 'N/A')}")
        url = song.get("preview_url", "")
        if url:
            lines.append(f"     Listen: {url}")
        lines.append("")

    lines += [
        "-" * 50,
        "  Built with AI + Computer Vision",
        "  Music Selection System — GitHub.com/ravigohel142996/Music-System-",
        "=" * 50,
    ]
    return "\n".join(lines)

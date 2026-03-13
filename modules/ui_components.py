"""
ui_components.py
Reusable Streamlit UI helpers for the Music Selection System.
"""

from typing import Dict, List, Optional

import plotly.graph_objects as go
import streamlit as st


# ---------------------------------------------------------------------------
# Hero Section
# ---------------------------------------------------------------------------

def render_hero() -> None:
    """Render the app hero / landing section."""
    st.markdown(
        """
        <div class="hero-container">
            <div class="hero-emoji">🎵</div>
            <h1 class="hero-title">Music Selection System</h1>
            <p class="hero-subtitle">Powered by Facial Recognition & AI</p>
            <p class="hero-tagline">
                Let your face choose the music. Our AI reads your emotion and curates<br>
                the perfect playlist in seconds — no manual searching required.
            </p>
            <div class="hero-badges">
                <span class="tech-badge">🤖 DeepFace AI</span>
                <span class="tech-badge">🎭 Emotion Detection</span>
                <span class="tech-badge">🎶 Smart Recommendations</span>
                <span class="tech-badge">📊 Real-time Analytics</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


# ---------------------------------------------------------------------------
# Mood Badge
# ---------------------------------------------------------------------------

def render_mood_badge(emotion: str, confidence: float, playlist_info: Dict) -> None:
    """
    Render a large gradient mood badge with confidence score.

    Args:
        emotion: Detected emotion label.
        confidence: Confidence score 0-100.
        playlist_info: Playlist config dict with color and emoji.
    """
    color = playlist_info.get("color", "#6C63FF")
    emoji = playlist_info.get("emoji", "🎵")
    energy = playlist_info.get("description", "")

    st.markdown(
        f"""
        <div class="mood-badge-container">
            <div class="mood-badge" style="background: linear-gradient(135deg, {color}33, {color}66); border: 2px solid {color};">
                <span class="mood-emoji">{emoji}</span>
                <span class="mood-label" style="color: {color};">{emotion}</span>
                <span class="mood-confidence">{confidence:.0f}% Confidence</span>
                <span class="mood-energy">{energy}</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


# ---------------------------------------------------------------------------
# Song Cards
# ---------------------------------------------------------------------------

def render_song_card(song: Dict, index: int) -> None:
    """
    Render a single song recommendation card.

    Args:
        song: Song dictionary with title, artist, mood, genre, etc.
        index: Card index for staggered animation.
    """
    title = song.get("title", "Unknown")
    artist = song.get("artist", "Unknown")
    mood = song.get("mood", "")
    genre = song.get("genre", "")
    energy = song.get("energy_level", "N/A")
    description = song.get("description", "")
    preview_url = song.get("preview_url", "")

    play_btn = ""
    if preview_url and str(preview_url).startswith("http"):
        play_btn = f'<a href="{preview_url}" target="_blank" class="play-btn">▶ Listen</a>'

    energy_dots = "●" * min(int(energy) if str(energy).isdigit() else 5, 10)
    energy_empty = "○" * (10 - len(energy_dots))

    st.markdown(
        f"""
        <div class="song-card" style="animation-delay: {index * 0.08}s;">
            <div class="song-number">#{index + 1}</div>
            <div class="song-title">{title}</div>
            <div class="song-artist">🎤 {artist}</div>
            <div class="song-meta">
                <span class="song-tag">{mood}</span>
                <span class="song-genre">{genre}</span>
            </div>
            <div class="song-energy">
                <span class="energy-label">Energy </span>
                <span class="energy-dots" style="color:#6C63FF;">{energy_dots}</span>
                <span class="energy-dots" style="opacity:0.3;">{energy_empty}</span>
            </div>
            <div class="song-desc">{description}</div>
            {play_btn}
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_song_cards(songs: List[Dict]) -> None:
    """
    Render a grid of song recommendation cards.

    Args:
        songs: List of song dictionaries.
    """
    st.markdown('<div class="songs-grid">', unsafe_allow_html=True)
    cols = st.columns(min(3, len(songs)))
    for i, song in enumerate(songs):
        with cols[i % len(cols)]:
            render_song_card(song, i)
    st.markdown("</div>", unsafe_allow_html=True)


# ---------------------------------------------------------------------------
# Confidence Chart
# ---------------------------------------------------------------------------

def render_confidence_gauge(confidence: float, emotion: str, color: str = "#6C63FF") -> None:
    """
    Render a Plotly gauge chart showing model confidence.

    Args:
        confidence: Confidence score 0-100.
        emotion: Detected emotion label.
        color: Gauge colour (hex string).
    """
    fig = go.Figure(
        go.Indicator(
            mode="gauge+number+delta",
            value=confidence,
            title={"text": f"Confidence — {emotion}", "font": {"color": "#EAEAEA", "size": 16}},
            number={"suffix": "%", "font": {"color": "#EAEAEA", "size": 28}},
            gauge={
                "axis": {"range": [0, 100], "tickcolor": "#EAEAEA"},
                "bar": {"color": color},
                "bgcolor": "#1A1A2E",
                "borderwidth": 1,
                "bordercolor": "#333",
                "steps": [
                    {"range": [0, 33], "color": "#2a2a3e"},
                    {"range": [33, 66], "color": "#1e1e30"},
                    {"range": [66, 100], "color": "#16163a"},
                ],
                "threshold": {
                    "line": {"color": "#FFFFFF", "width": 2},
                    "thickness": 0.75,
                    "value": confidence,
                },
            },
        )
    )
    fig.update_layout(
        height=260,
        margin=dict(t=40, b=10, l=10, r=10),
        paper_bgcolor="#0E0E1A",
        font={"color": "#EAEAEA"},
    )
    st.plotly_chart(fig, use_container_width=True)


def render_emotion_bar_chart(all_scores: Dict[str, float]) -> None:
    """
    Render a horizontal bar chart for all emotion probabilities.

    Args:
        all_scores: Dict mapping emotion label → score.
    """
    labels = list(all_scores.keys())
    values = [round(v, 1) for v in all_scores.values()]

    colours = {
        "Happy": "#FFD700",
        "Sad": "#4A90D9",
        "Angry": "#FF4444",
        "Neutral": "#9B9B9B",
        "Surprise": "#FF8C00",
        "Relaxed": "#7ED8A3",
    }
    bar_colors = [colours.get(l, "#6C63FF") for l in labels]

    fig = go.Figure(
        go.Bar(
            x=values,
            y=labels,
            orientation="h",
            marker_color=bar_colors,
            text=[f"{v:.1f}%" for v in values],
            textposition="outside",
            textfont={"color": "#EAEAEA"},
        )
    )
    fig.update_layout(
        title={"text": "Emotion Probability Distribution", "font": {"color": "#EAEAEA", "size": 14}},
        paper_bgcolor="#0E0E1A",
        plot_bgcolor="#1A1A2E",
        height=300,
        margin=dict(t=40, b=20, l=10, r=60),
        xaxis={
            "range": [0, max(values) * 1.2 if values else 100],
            "tickcolor": "#EAEAEA",
            "color": "#EAEAEA",
            "gridcolor": "#2a2a3e",
        },
        yaxis={"tickcolor": "#EAEAEA", "color": "#EAEAEA"},
        font={"color": "#EAEAEA"},
    )
    st.plotly_chart(fig, use_container_width=True)


# ---------------------------------------------------------------------------
# Session History
# ---------------------------------------------------------------------------

def render_history_table(history: List[Dict]) -> None:
    """
    Render the session history as a styled table.

    Args:
        history: List of history entry dicts (most recent first).
    """
    if not history:
        st.markdown(
            '<div class="empty-state">No history yet — analyse a face to get started!</div>',
            unsafe_allow_html=True,
        )
        return

    rows = []
    for entry in history:
        songs = entry.get("songs", [])
        song_titles = ", ".join(s.get("title", "") for s in songs[:3])
        if len(songs) > 3:
            song_titles += "..."
        rows.append(
            {
                "Time": entry.get("timestamp", ""),
                "Emotion": entry.get("emotion", ""),
                "Confidence": f"{entry.get('confidence', 0):.0f}%",
                "Method": entry.get("method", ""),
                "Top Recommendations": song_titles,
            }
        )

    import pandas as pd  # noqa: PLC0415

    df = pd.DataFrame(rows)
    st.dataframe(df, use_container_width=True, hide_index=True)


def render_history_mood_chart(history: List[Dict]) -> None:
    """
    Render a pie chart of mood distribution from session history.

    Args:
        history: List of history entry dicts.
    """
    if not history:
        return

    counts: Dict[str, int] = {}
    for entry in history:
        mood = entry.get("emotion", "Unknown")
        counts[mood] = counts.get(mood, 0) + 1

    colours = {
        "Happy": "#FFD700",
        "Sad": "#4A90D9",
        "Angry": "#FF4444",
        "Neutral": "#9B9B9B",
        "Surprise": "#FF8C00",
        "Relaxed": "#7ED8A3",
        "Unknown": "#6C63FF",
    }

    fig = go.Figure(
        go.Pie(
            labels=list(counts.keys()),
            values=list(counts.values()),
            marker_colors=[colours.get(k, "#6C63FF") for k in counts],
            hole=0.4,
            textinfo="label+percent",
            textfont={"color": "#EAEAEA"},
        )
    )
    fig.update_layout(
        title={"text": "Session Mood Distribution", "font": {"color": "#EAEAEA", "size": 14}},
        paper_bgcolor="#0E0E1A",
        height=320,
        margin=dict(t=40, b=20, l=10, r=10),
        font={"color": "#EAEAEA"},
        legend={"font": {"color": "#EAEAEA"}},
    )
    st.plotly_chart(fig, use_container_width=True)


# ---------------------------------------------------------------------------
# Footer
# ---------------------------------------------------------------------------

def render_footer() -> None:
    """Render the app footer."""
    st.markdown(
        """
        <div class="footer">
            <div class="footer-content">
                <p class="footer-title">🎵 Music Selection System</p>
                <p class="footer-sub">Built with AI + Computer Vision + ❤️</p>
                <div class="footer-badges">
                    <span class="footer-badge">Python</span>
                    <span class="footer-badge">Streamlit</span>
                    <span class="footer-badge">OpenCV</span>
                    <span class="footer-badge">DeepFace</span>
                    <span class="footer-badge">Plotly</span>
                </div>
                <p class="footer-credit">
                    © 2024 Music Selection System · Facial Recognition Music Recommender
                </p>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

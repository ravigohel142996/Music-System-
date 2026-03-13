"""
app.py
Main entry point for the Music Selection System based on Facial Recognition.
Run with: streamlit run app.py
"""

import io
import os
import sys

import numpy as np
import streamlit as st
from PIL import Image

# ---------------------------------------------------------------------------
# Ensure project root is on the Python path
# ---------------------------------------------------------------------------
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from modules.emotion_analyzer import analyze_emotion, pil_image_to_bgr
from modules.face_detector import detect_faces, draw_face_box
from modules.history_manager import add_entry, clear_history, get_history
from modules.insights import (
    build_recommendation_summary,
    get_energy_info,
    get_explanation,
    get_mood_tip,
)
from modules.music_recommender import get_playlist_info, get_recommendations
from modules.ui_components import (
    render_confidence_gauge,
    render_emotion_bar_chart,
    render_footer,
    render_hero,
    render_history_mood_chart,
    render_history_table,
    render_mood_badge,
    render_song_cards,
)
from utils.helpers import ensure_rgb, get_image_size_label, resize_image, validate_image
from utils.style import CUSTOM_CSS

# ---------------------------------------------------------------------------
# Streamlit page config (must be first Streamlit call)
# ---------------------------------------------------------------------------
st.set_page_config(
    page_title="Music Selection System — Facial Recognition",
    page_icon="🎵",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Inject premium CSS
st.markdown(CUSTOM_CSS, unsafe_allow_html=True)


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _process_image(image: Image.Image) -> None:
    """
    Run the full analysis pipeline on a PIL Image and display results.

    1. Validate image
    2. Detect face
    3. Analyse emotion
    4. Recommend music
    5. Display all sections
    """
    # Validate
    valid, err_msg = validate_image(image)
    if not valid:
        st.error(f"⚠️ {err_msg}")
        return

    image = ensure_rgb(image)
    image = resize_image(image, 640, 480)

    # Convert to BGR for OpenCV/ML processing
    bgr_image = pil_image_to_bgr(image)

    # ------------------------------------------------------------------ #
    # Face Detection
    # ------------------------------------------------------------------ #
    with st.spinner("🔍 Detecting face…"):
        faces = detect_faces(bgr_image)

    if not faces:
        st.warning(
            "😕 No face detected in the image. "
            "Please upload a clear, well-lit photo with your face visible."
        )
        st.image(image, caption="Uploaded Image (No face found)", use_column_width=True)
        return

    # Draw bounding box on a copy for display
    import cv2  # noqa: PLC0415
    import numpy as _np  # noqa: PLC0415

    rgb_arr = _np.array(image)
    bgr_for_draw = cv2.cvtColor(rgb_arr, cv2.COLOR_RGB2BGR)
    annotated_bgr = draw_face_box(bgr_for_draw, faces)
    annotated_rgb = cv2.cvtColor(annotated_bgr, cv2.COLOR_BGR2RGB)
    annotated_pil = Image.fromarray(annotated_rgb)

    # ------------------------------------------------------------------ #
    # Emotion Analysis
    # ------------------------------------------------------------------ #
    with st.spinner("🤖 Analysing facial expression…"):
        result = analyze_emotion(bgr_image)

    emotion: str = result["emotion"]
    confidence: float = result["confidence"]
    all_scores: dict = result["all_scores"]
    method: str = result["method"]

    # ------------------------------------------------------------------ #
    # Music Recommendation
    # ------------------------------------------------------------------ #
    songs = get_recommendations(emotion, top_n=6)
    playlist_info = get_playlist_info(emotion)
    explanation = get_explanation(emotion, confidence)
    tip = get_mood_tip(emotion)
    energy_info = get_energy_info(emotion)

    # Save to history
    add_entry(
        emotion=emotion,
        confidence=confidence,
        songs=songs,
        method=method,
        image_label=f"Image ({get_image_size_label(image)})",
    )

    # ================================================================== #
    # DISPLAY RESULTS
    # ================================================================== #

    st.markdown("---")

    # -------------------------------------------------- Detection Result --
    st.markdown('<p class="section-header">🎭 Detection Result</p>', unsafe_allow_html=True)

    col_img, col_badge = st.columns([1, 1])

    with col_img:
        st.image(
            annotated_pil,
            caption=f"Detected {len(faces)} face(s) · {get_image_size_label(image)}",
            use_column_width=True,
        )

    with col_badge:
        render_mood_badge(emotion, confidence, playlist_info)

        # Detection method & face count metrics
        m1, m2, m3 = st.columns(3)
        m1.metric("Faces Detected", len(faces))
        m2.metric("Confidence", f"{confidence:.0f}%")
        m3.metric("Method", method)

        # Vibe message
        vibe = playlist_info.get("vibe_message", "Here's music picked just for you.")
        st.markdown(f'<div class="vibe-message">💬 {vibe}</div>', unsafe_allow_html=True)

    # -------------------------------------------------- Insight Panel ----
    st.markdown(
        f"""
        <div class="insight-panel">
            <div class="insight-title">🧠 AI Explanation</div>
            <div class="insight-text">{explanation}</div>
        </div>
        <div class="tip-panel">💡 Wellness Tip: {tip}</div>
        """,
        unsafe_allow_html=True,
    )

    # -------------------------------------------------- Analytics --------
    st.markdown('<p class="section-header">📊 Confidence Analytics</p>', unsafe_allow_html=True)

    col_gauge, col_bar = st.columns([1, 1])
    with col_gauge:
        render_confidence_gauge(confidence, emotion, playlist_info.get("color", "#6C63FF"))
    with col_bar:
        render_emotion_bar_chart(all_scores)

    # -------------------------------------------------- Music Cards ------
    st.markdown('<p class="section-header">🎵 Your Personalised Playlist</p>', unsafe_allow_html=True)

    char_tags = " · ".join(playlist_info.get("characteristics", []))
    genres_str = ", ".join(playlist_info.get("genres", []))
    st.markdown(
        f"""
        <div class="insight-panel">
            <div class="insight-title">🎶 Playlist Strategy</div>
            <div class="insight-text">
                <strong>Genres:</strong> {genres_str}<br>
                <strong>Vibes:</strong> {char_tags}
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    render_song_cards(songs)

    # -------------------------------------------------- Download --------
    summary_text = build_recommendation_summary(emotion, confidence, songs, method)
    st.download_button(
        label="⬇️  Download Recommendation Summary",
        data=summary_text.encode("utf-8"),
        file_name=f"music_recommendation_{emotion.lower()}.txt",
        mime="text/plain",
    )


# ---------------------------------------------------------------------------
# Main App Layout
# ---------------------------------------------------------------------------

def main() -> None:
    """Render the complete app layout."""

    # Hero
    render_hero()

    # ====================================================================
    # INPUT SECTION
    # ====================================================================
    st.markdown('<p class="section-header">📸 Input — Detect Your Mood</p>', unsafe_allow_html=True)

    tab_webcam, tab_upload, tab_sample = st.tabs(
        ["📷 Webcam Capture", "🖼️ Upload Image", "🎭 Sample Images"]
    )

    # -------------------------------------------------------- Webcam ----
    with tab_webcam:
        st.markdown(
            """
            <div class="insight-panel">
                <div class="insight-title">📷 Webcam Instructions</div>
                <div class="insight-text">
                    Click <strong>Take Photo</strong> below to capture your face from your webcam.
                    Make sure you are in a well-lit environment for the best results.
                    Your photo is processed locally and never stored permanently.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        webcam_image = st.camera_input("Take a photo to detect your mood")

        if webcam_image is not None:
            image = Image.open(webcam_image)
            _process_image(image)

    # ------------------------------------------------------ Upload ------
    with tab_upload:
        st.markdown(
            """
            <div class="insight-panel">
                <div class="insight-title">🖼️ Upload Instructions</div>
                <div class="insight-text">
                    Upload a clear face photo (JPG, PNG, or WEBP).
                    For best results: good lighting, face fully visible, and minimal background clutter.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        uploaded_file = st.file_uploader(
            "Choose an image file",
            type=["jpg", "jpeg", "png", "webp"],
            label_visibility="collapsed",
        )

        if uploaded_file is not None:
            image = Image.open(uploaded_file)
            _process_image(image)

    # ------------------------------------------------------ Samples ----
    with tab_sample:
        st.markdown(
            """
            <div class="insight-panel">
                <div class="insight-title">🎭 Try with Sample Images</div>
                <div class="insight-text">
                    No webcam or photo handy? Select one of our sample mood images to see the system in action.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        sample_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "sample_images")
        sample_files = [
            f for f in os.listdir(sample_dir)
            if f.lower().endswith((".jpg", ".jpeg", ".png"))
        ] if os.path.isdir(sample_dir) else []

        if sample_files:
            selected_sample = st.selectbox(
                "Select a sample image",
                options=sample_files,
                format_func=lambda x: x.replace("_", " ").replace(".jpg", "").replace(".jpeg", "").title(),
            )
            if st.button("🚀 Analyse Sample Image", use_container_width=True):
                sample_path = os.path.join(sample_dir, selected_sample)
                try:
                    sample_image = Image.open(sample_path)
                    _process_image(sample_image)
                except Exception as e:
                    st.error(f"Could not load sample image: {e}")
        else:
            st.info(
                "Sample images not found. "
                "Please use the Webcam or Upload tab to analyse your own photo."
            )

    # ====================================================================
    # SESSION HISTORY SECTION
    # ====================================================================
    history = get_history()
    if history:
        st.markdown('<p class="section-header">📋 Session History</p>', unsafe_allow_html=True)

        col_hist, col_pie = st.columns([3, 2])

        with col_hist:
            render_history_table(history)

        with col_pie:
            render_history_mood_chart(history)

        if st.button("🗑️ Clear History", use_container_width=False):
            clear_history()
            st.rerun()

    # ====================================================================
    # FOOTER
    # ====================================================================
    render_footer()


if __name__ == "__main__":
    main()

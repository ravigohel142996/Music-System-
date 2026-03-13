# 🎵 Music Selection System Based on Facial Recognition

> *Let your face choose the music. Our AI reads your emotion and curates the perfect playlist in seconds.*

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue?logo=python)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28%2B-red?logo=streamlit)](https://streamlit.io)
[![OpenCV](https://img.shields.io/badge/OpenCV-4.8%2B-green?logo=opencv)](https://opencv.org)
[![License](https://img.shields.io/badge/License-MIT-yellow)](LICENSE)

---

## 📖 Overview

The **Music Selection System Based on Facial Recognition** is a modern AI-powered web application that:

1. **Captures** the user's face via webcam or uploaded image
2. **Detects** facial expression and mood using computer vision
3. **Recommends** a personalised music playlist based on the detected emotion
4. **Explains** why those songs were chosen using an AI insight panel
5. **Tracks** session history and mood analytics in a premium dashboard

---

## ✨ Features

| Feature | Description |
|--------|-------------|
| 🎭 Real-Time Mood Detection | Detects emotion from webcam or uploaded photo |
| 🎵 Smart Music Recommendation | Curated playlists for 6 different moods |
| 📊 Confidence Analytics | Plotly gauge and bar charts for prediction confidence |
| 🧠 Explainable AI Panel | Human-readable explanation for every detection |
| 📋 Session History | Track all detections in the current session |
| ⬇️ Downloadable Summary | Export your playlist recommendation as a .txt file |
| 🌙 Premium Dark UI | Glassmorphism cards, gradients, smooth animations |
| 🔄 Graceful Fallbacks | Works even without GPU or heavy ML dependencies |

### Supported Moods
- 😄 **Happy** → Upbeat, energetic, feel-good music
- 😢 **Sad** → Soothing, healing, emotional ballads
- 😠 **Angry** → Powerful, intense, cathartic releases
- 😐 **Neutral** → Balanced, lo-fi, ambient tracks
- 😲 **Surprise** → Dynamic, exciting, genre-hopping music
- 😌 **Relaxed** → Soft, ambient, meditative soundscapes

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Frontend | Streamlit + Custom CSS |
| Face Detection | OpenCV Haar Cascades |
| Emotion Analysis | DeepFace (primary) → FER (fallback) → Heuristic |
| Data & Analytics | Pandas, NumPy, Plotly |
| Music Catalogue | Local CSV dataset (42+ songs) |
| Optional Integration | Spotipy (Spotify API) |

---

## 📁 Folder Structure

```
music-selection-system/
├── app.py                     # Main Streamlit application
├── requirements.txt           # Python dependencies
├── README.md                  # This file
├── .streamlit/
│   └── config.toml            # Streamlit theme configuration
├── assets/
│   ├── logo.png
│   └── banner.png
├── data/
│   ├── songs.csv              # 42+ songs across 6 moods
│   └── mood_playlists.json    # Mood metadata & strategy config
├── modules/
│   ├── face_detector.py       # OpenCV face detection
│   ├── emotion_analyzer.py    # DeepFace/FER emotion analysis
│   ├── music_recommender.py   # Song recommendation engine
│   ├── ui_components.py       # Reusable Streamlit UI components
│   ├── insights.py            # AI explanation & wellness tips
│   └── history_manager.py     # Session history management
├── utils/
│   ├── helpers.py             # Image utilities
│   └── style.py               # Custom CSS theme
└── sample_images/
    ├── happy.jpg
    ├── sad.jpg
    ├── neutral.jpg
    ├── angry.jpg
    ├── relaxed.jpg
    └── surprise.jpg
```

---

## 🚀 Installation & Local Setup

### Prerequisites
- Python 3.9 or higher
- pip package manager

### Steps

```bash
# 1. Clone the repository
git clone https://github.com/ravigohel142996/Music-System-.git
cd Music-System-

# 2. (Optional but recommended) Create a virtual environment
python -m venv venv
source venv/bin/activate        # macOS/Linux
# venv\Scripts\activate         # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the app
streamlit run app.py
```

The app will open at **http://localhost:8501**

---

## ☁️ Deploy to Streamlit Cloud

1. **Fork** this repository to your GitHub account
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Click **New app**
4. Select your forked repository, branch `main`, and set **Main file path** to `app.py`
5. Click **Deploy** — Streamlit Cloud will automatically install dependencies

> **Note:** The app works without any external API keys. DeepFace will download model weights on first run (~50 MB). If the ML model fails to load in the cloud environment, the app gracefully falls back to a heuristic-based emotion detector.

### Optional: Spotify Integration

To enable Spotify preview links:

1. Create a Spotify Developer app at [developer.spotify.com](https://developer.spotify.com)
2. Add your credentials as Streamlit secrets:

```toml
# .streamlit/secrets.toml  (do NOT commit this file)
SPOTIFY_CLIENT_ID = "your_client_id"
SPOTIFY_CLIENT_SECRET = "your_client_secret"
```

---

## 📸 Screenshots

| Hero Section | Detection Result |
|:---:|:---:|
| *(Premium dark landing page)* | *(Emotion badge + face image)* |

| Music Playlist | Analytics Dashboard |
|:---:|:---:|
| *(Glassmorphism song cards)* | *(Plotly confidence gauge)* |

---

## 🔮 Future Scope

- [ ] Real-time video stream emotion detection
- [ ] Spotify API integration for full playback
- [ ] User accounts and persistent history
- [ ] Multi-face detection and group mood averaging
- [ ] Voice mood detection (audio analysis)
- [ ] Mobile-responsive PWA wrapper
- [ ] Language localisation (multi-language support)

---

## 📄 License

This project is licensed under the **MIT License** — feel free to use, modify, and distribute.

---

## 👨‍💻 Built With

**AI + Computer Vision + ❤️**

> *Music Selection System — where technology meets emotion.*

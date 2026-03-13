"""
style.py
Custom CSS definitions for the Music Selection System premium UI theme.
"""

CUSTOM_CSS = """
<style>
/* ====================================================
   GLOBAL RESETS & BASE STYLES
   ==================================================== */

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background: linear-gradient(135deg, #0E0E1A 0%, #111127 50%, #0E0E1A 100%);
    min-height: 100vh;
}

/* Remove default Streamlit padding on main block */
.block-container {
    padding-top: 1rem !important;
    max-width: 1200px !important;
}

/* Hide Streamlit branding */
#MainMenu, footer, header { visibility: hidden; }

/* ====================================================
   HERO SECTION
   ==================================================== */

.hero-container {
    text-align: center;
    padding: 3rem 2rem 2rem;
    background: linear-gradient(180deg, rgba(108,99,255,0.12) 0%, transparent 100%);
    border-bottom: 1px solid rgba(108,99,255,0.15);
    margin-bottom: 2rem;
}

.hero-emoji {
    font-size: 4rem;
    margin-bottom: 0.5rem;
    filter: drop-shadow(0 0 20px rgba(108,99,255,0.6));
    animation: float 3s ease-in-out infinite;
}

@keyframes float {
    0%, 100% { transform: translateY(0); }
    50% { transform: translateY(-10px); }
}

.hero-title {
    font-size: 3.2rem;
    font-weight: 800;
    background: linear-gradient(135deg, #FFFFFF 0%, #6C63FF 50%, #A78BFA 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    margin: 0;
    letter-spacing: -0.5px;
}

.hero-subtitle {
    font-size: 1.2rem;
    color: #A78BFA;
    margin: 0.5rem 0 1rem;
    font-weight: 500;
    letter-spacing: 0.5px;
}

.hero-tagline {
    font-size: 1rem;
    color: #8888AA;
    max-width: 600px;
    margin: 0 auto 1.5rem;
    line-height: 1.7;
}

.hero-badges {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 0.5rem;
    margin-top: 1rem;
}

.tech-badge {
    background: rgba(108,99,255,0.15);
    border: 1px solid rgba(108,99,255,0.4);
    color: #A78BFA;
    padding: 0.3rem 0.9rem;
    border-radius: 50px;
    font-size: 0.8rem;
    font-weight: 500;
    transition: all 0.2s ease;
}

.tech-badge:hover {
    background: rgba(108,99,255,0.3);
    border-color: #6C63FF;
    color: #FFFFFF;
}

/* ====================================================
   SECTION HEADERS
   ==================================================== */

.section-header {
    font-size: 1.5rem;
    font-weight: 700;
    color: #EAEAEA;
    margin: 2rem 0 1rem;
    display: flex;
    align-items: center;
    gap: 0.5rem;
    border-bottom: 2px solid rgba(108,99,255,0.3);
    padding-bottom: 0.5rem;
}

/* ====================================================
   MOOD BADGE
   ==================================================== */

.mood-badge-container {
    display: flex;
    justify-content: center;
    padding: 1rem 0;
}

.mood-badge {
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 1.5rem 2.5rem;
    border-radius: 20px;
    backdrop-filter: blur(10px);
    -webkit-backdrop-filter: blur(10px);
    text-align: center;
    min-width: 240px;
    box-shadow: 0 8px 32px rgba(0,0,0,0.3);
    animation: slideUp 0.5s ease;
}

@keyframes slideUp {
    from { opacity: 0; transform: translateY(20px); }
    to { opacity: 1; transform: translateY(0); }
}

.mood-emoji {
    font-size: 3.5rem;
    margin-bottom: 0.4rem;
}

.mood-label {
    font-size: 2rem;
    font-weight: 800;
    letter-spacing: -0.5px;
}

.mood-confidence {
    font-size: 0.9rem;
    color: #AAAACC;
    margin-top: 0.2rem;
}

.mood-energy {
    font-size: 0.8rem;
    color: #7777AA;
    margin-top: 0.4rem;
    font-style: italic;
}

/* ====================================================
   SONG CARDS
   ==================================================== */

.songs-grid {
    display: flex;
    flex-wrap: wrap;
    gap: 1rem;
    margin: 1rem 0;
}

.song-card {
    background: rgba(255,255,255,0.04);
    border: 1px solid rgba(108,99,255,0.2);
    border-radius: 16px;
    padding: 1.2rem;
    transition: all 0.25s ease;
    animation: fadeIn 0.4s ease both;
    position: relative;
    overflow: hidden;
}

.song-card::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 3px;
    background: linear-gradient(90deg, #6C63FF, #A78BFA);
    transform: scaleX(0);
    transition: transform 0.3s ease;
    transform-origin: left;
}

.song-card:hover {
    border-color: rgba(108,99,255,0.6);
    background: rgba(108,99,255,0.08);
    transform: translateY(-3px);
    box-shadow: 0 8px 30px rgba(108,99,255,0.2);
}

.song-card:hover::before { transform: scaleX(1); }

@keyframes fadeIn {
    from { opacity: 0; transform: translateY(15px); }
    to { opacity: 1; transform: translateY(0); }
}

.song-number {
    font-size: 0.7rem;
    color: #6C63FF;
    font-weight: 700;
    letter-spacing: 1px;
    text-transform: uppercase;
    margin-bottom: 0.4rem;
}

.song-title {
    font-size: 1.05rem;
    font-weight: 700;
    color: #EAEAEA;
    margin-bottom: 0.2rem;
    line-height: 1.3;
}

.song-artist {
    font-size: 0.85rem;
    color: #9999BB;
    margin-bottom: 0.6rem;
}

.song-meta {
    display: flex;
    flex-wrap: wrap;
    gap: 0.3rem;
    margin-bottom: 0.6rem;
}

.song-tag {
    background: rgba(108,99,255,0.2);
    color: #A78BFA;
    padding: 0.15rem 0.6rem;
    border-radius: 50px;
    font-size: 0.72rem;
    font-weight: 600;
}

.song-genre {
    background: rgba(255,255,255,0.06);
    color: #8888AA;
    padding: 0.15rem 0.6rem;
    border-radius: 50px;
    font-size: 0.72rem;
}

.song-energy {
    font-size: 0.75rem;
    margin-bottom: 0.5rem;
    letter-spacing: 1px;
}

.energy-label { color: #7777AA; }

.song-desc {
    font-size: 0.78rem;
    color: #6666AA;
    line-height: 1.5;
    margin-bottom: 0.8rem;
    font-style: italic;
}

.play-btn {
    display: inline-block;
    background: linear-gradient(135deg, #6C63FF, #A78BFA);
    color: #FFFFFF !important;
    text-decoration: none !important;
    padding: 0.35rem 0.9rem;
    border-radius: 50px;
    font-size: 0.78rem;
    font-weight: 600;
    transition: all 0.2s ease;
    box-shadow: 0 3px 10px rgba(108,99,255,0.3);
}

.play-btn:hover {
    box-shadow: 0 5px 18px rgba(108,99,255,0.5);
    transform: scale(1.05);
}

/* ====================================================
   INSIGHT PANEL
   ==================================================== */

.insight-panel {
    background: rgba(108,99,255,0.08);
    border: 1px solid rgba(108,99,255,0.25);
    border-left: 4px solid #6C63FF;
    border-radius: 12px;
    padding: 1.2rem 1.4rem;
    margin: 1rem 0;
    animation: slideUp 0.4s ease;
}

.insight-title {
    font-size: 0.8rem;
    font-weight: 700;
    color: #A78BFA;
    letter-spacing: 1px;
    text-transform: uppercase;
    margin-bottom: 0.5rem;
}

.insight-text {
    font-size: 0.9rem;
    color: #CCCCDD;
    line-height: 1.6;
}

.tip-panel {
    background: rgba(126,216,163,0.07);
    border: 1px solid rgba(126,216,163,0.2);
    border-left: 4px solid #7ED8A3;
    border-radius: 12px;
    padding: 0.8rem 1.2rem;
    margin-top: 0.8rem;
    font-size: 0.85rem;
    color: #9EE6BA;
    line-height: 1.5;
}

/* ====================================================
   VIBE MESSAGE
   ==================================================== */

.vibe-message {
    text-align: center;
    font-size: 1.05rem;
    color: #AAAACC;
    font-style: italic;
    padding: 1rem;
    background: rgba(255,255,255,0.02);
    border-radius: 12px;
    border: 1px solid rgba(255,255,255,0.06);
    margin: 1rem 0;
    line-height: 1.6;
}

/* ====================================================
   EMPTY STATE
   ==================================================== */

.empty-state {
    text-align: center;
    color: #4444AA;
    padding: 2rem;
    font-size: 0.95rem;
    font-style: italic;
    background: rgba(255,255,255,0.02);
    border-radius: 12px;
    border: 1px dashed rgba(108,99,255,0.2);
}

/* ====================================================
   FOOTER
   ==================================================== */

.footer {
    margin-top: 4rem;
    border-top: 1px solid rgba(108,99,255,0.15);
    padding: 2rem 1rem;
    text-align: center;
}

.footer-title {
    font-size: 1.2rem;
    font-weight: 700;
    background: linear-gradient(135deg, #6C63FF, #A78BFA);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    margin-bottom: 0.3rem;
}

.footer-sub {
    color: #7777AA;
    font-size: 0.85rem;
    margin-bottom: 0.8rem;
}

.footer-badges {
    display: flex;
    justify-content: center;
    flex-wrap: wrap;
    gap: 0.4rem;
    margin-bottom: 0.8rem;
}

.footer-badge {
    background: rgba(108,99,255,0.1);
    border: 1px solid rgba(108,99,255,0.2);
    color: #7777CC;
    padding: 0.2rem 0.7rem;
    border-radius: 50px;
    font-size: 0.72rem;
}

.footer-credit {
    color: #444466;
    font-size: 0.75rem;
}

/* ====================================================
   STREAMLIT OVERRIDES
   ==================================================== */

div[data-testid="stTabs"] button {
    color: #AAAACC;
    font-weight: 600;
    font-size: 0.9rem;
}

div[data-testid="stTabs"] button[aria-selected="true"] {
    color: #6C63FF;
    border-bottom-color: #6C63FF !important;
}

div[data-testid="stExpander"] {
    border: 1px solid rgba(108,99,255,0.2) !important;
    border-radius: 12px !important;
    background: rgba(255,255,255,0.02) !important;
}

.stButton > button {
    background: linear-gradient(135deg, #6C63FF, #7C73FF);
    color: white;
    border: none;
    border-radius: 10px;
    padding: 0.5rem 1.5rem;
    font-weight: 600;
    font-size: 0.9rem;
    transition: all 0.2s ease;
    box-shadow: 0 4px 15px rgba(108,99,255,0.25);
}

.stButton > button:hover {
    background: linear-gradient(135deg, #5a52ee, #6C63FF);
    box-shadow: 0 6px 22px rgba(108,99,255,0.4);
    transform: translateY(-1px);
}

.stDownloadButton > button {
    background: rgba(108,99,255,0.15);
    border: 1px solid rgba(108,99,255,0.4);
    color: #A78BFA;
    border-radius: 10px;
}

div[data-testid="stMetric"] {
    background: rgba(255,255,255,0.03);
    border: 1px solid rgba(108,99,255,0.15);
    border-radius: 12px;
    padding: 1rem;
}

div[data-testid="stMetric"] > label {
    color: #7777AA !important;
    font-size: 0.8rem !important;
}

div[data-testid="stMetric"] > div {
    color: #EAEAEA !important;
    font-weight: 700 !important;
}
</style>
"""

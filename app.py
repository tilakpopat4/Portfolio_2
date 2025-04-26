import streamlit as st
from PIL import Image
import os

# Set page config
st.set_page_config(
    page_title="Upcoming Shortfilms - Tilak Popat Films",
    page_icon="🎬",
    layout="centered"
)

# Custom CSS for white text on dark background
st.markdown("""
    <style>
    body {
        background-color: #121212;
        color: white;
    }
    .main {
        background-color: #121212;
    }
    .title {
        font-size: 36px;
        font-weight: bold;
        text-align: center;
        margin-top: 10px;
        color: white;
    }
    .description {
        font-size: 18px;
        text-align: center;
        padding: 10px 30px;
        color: white;
    }
    .release {
        font-size: 16px;
        text-align: center;
        margin-top: 10px;
        font-style: italic;
        color: white;
    }
    .presented {
        font-size: 16px;
        text-align: center;
        margin-top: 20px;
        letter-spacing: 2px;
        color: white;
    }
    .divider {
        margin: 40px 0;
        border-top: 1px solid #444;
    }
    .youtube-link {
        text-align: center;
        margin-top: 15px;
    }
    </style>
""", unsafe_allow_html=True)

# Function to safely show a shortfilm block
def show_shortfilm(image_path, title, description, release_date, youtube_url):
    try:
        if os.path.exists(image_path):
            image = Image.open(image_path)
            st.image(image)
        else:
            st.warning(f"Image not found: {image_path}")
            st.image("https://via.placeholder.com/800x400.png?text=Poster+Coming+Soon", use_column_width=True)

        st.markdown(f'<div class="title">{title}</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="description">{description}</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="release">Estimated Release Time: {release_date}</div>', unsafe_allow_html=True)
        st.markdown('<div class="presented">PRESENTED BY TILAK POPAT FILMS</div>', unsafe_allow_html=True)
        
        # YouTube Link with icon
        st.markdown(f'''
            <div class="youtube-link">
                <a href="{youtube_url}" target="_blank">
                    <img src="https://upload.wikimedia.org/wikipedia/commons/0/09/YouTube_full-color_icon_(2017).svg" width="40" height="28">
                </a>
            </div>
        ''', unsafe_allow_html=True)

        st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

    except Exception as e:
        st.error(f"An error occurred: {e}")

# =================== Shortfilm 1 ===================
show_shortfilm(
    "Add a heading.png",
    "PARIKSHA - [A Shortfilm]",
    "A mobile shortfilm based on <strong>Engineering Life Hurdles</strong> with <strong>4 Chapters</strong>. Each chapter delivers a helpful lesson for students.",
    "Aug – 2025",
    "https://youtu.be/P86C62-LAao"  # <-- Replace with actual YouTube link
)

# =================== Shortfilm 2 ===================
show_shortfilm(
    "2.png",
    "COVID - 2019 - [A Family Film]",
    "Explores the inner conflicts of a young adult dealing with identity, anxiety, and societal pressure. A gripping introspective tale.",
    "Oct – 2025",
    "https://youtu.be/qMsSFRMz5p8"  # <-- Replace with actual YouTube link
)

# =================== Shortfilm 3 ===================
show_shortfilm(
    "55.png",
    "KILLER - [An Action Film]",
    "An emotional visual journey without words. 'Dastaan' highlights family bonds, sacrifice, and the power of expression through silence.",
    "Dec – 2025",
    "https://youtu.be/gv7sD67KME0"  # <-- Replace with actual YouTube link
)

# Back to Home
st.markdown("### 🔗 [Back to the Home Page](https://tilakpopatportfolio.streamlit.app/)")

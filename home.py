import streamlit as st

# Page setup
st.set_page_config(page_title="Tilak Popat's Portfolio", layout="wide")
st.title("🏠 Tilak Popat's Portfolio")

# --- Custom CSS Styling ---
st.markdown("""
    <style>
    body {
        background-color: #0f2027;
    }
    .main {
        background: linear-gradient(to right, #0f2027, #203a43, #2c5364);
        color: white;
    }
    .hero-title {
        font-size: 60px;
        font-weight: bold;
        color: #FEC260;
        margin-bottom: 0;
    }
    .hero-subtitle {
        font-size: 28px;
        color: #FFFFFF;
        margin-top: 0;
    }
    .social-icon img {
        width: 48px;
        height: 48px;
        transition: transform 0.5s ease;
    }
    .social-icon img:hover {
        transform: scale(1.2);
    }
    </style>
""", unsafe_allow_html=True)

# --- Layout ---
col1, col2 = st.columns(2)

with col1:
    st.markdown('<h1 class="hero-title">Hi, I\'m Tilak Popat</h1>', unsafe_allow_html=True)
    st.markdown('<p class="hero-subtitle">Cybersecurity Student | Cinematography Enthusiast 🎬</p>', unsafe_allow_html=True)

    # Typing animation (JS won't run in Streamlit, but left for structure)
    st.markdown("""
    <div style="color: white; font-size: 22px; font-weight: bold;">
        <span>Exploring the world of Cybersecurity 🔐</span><br>
        <span>Storytelling through Cinematography 🎥</span><br>
        <span>Building projects that inspire 🚀</span><br>
        <span>Welcome to my creative world 🌟</span>
    </div>
    """, unsafe_allow_html=True)

    # --- Quick Links with Icons ---
    st.markdown("### 📁 Quick Links")

    quick_links = {
        "🎥 View My Cinematography Work": ("https://example.com/cinematography", "https://img.icons8.com/color/48/video-editing.png"),
        "🔐 Explore My Cybersecurity Projects": ("https://example.com/cybersecurity", "https://img.icons8.com/color/48/lock--v1.png"),
        "📧 Contact Me": ("https://example.com/contact", "https://img.icons8.com/color/48/secured-letter.png"),
    }

    for text, (link, icon) in quick_links.items():
        st.markdown(f"""
            <div style="margin-bottom: 10px;">
                <a href="{link}" target="_blank" style="text-decoration: none;">
                    <img src="{icon}" style="vertical-align: middle; width:32px; height:32px; margin-right:10px;" />
                    <span style="font-size: 20px; color: white;">{text}</span>
                </a>
            </div>
        """, unsafe_allow_html=True)

    st.markdown(" ")

    # --- Resume Download ---
    try:
        with open("Tilak_Resume.pdf", "rb") as file:
            st.download_button(
                label="📄 Download My Resume",
                data=file,
                file_name="Tilak_Resume.pdf",
                mime="application/pdf",
                key="resume_download"
            )
    except FileNotFoundError:
        st.warning("Resume file not found. Please add 'Tilak_Resume.pdf' to your app folder.")

with col2:
    try:
        st.image("your_profile_image.png", width=350, caption="👋 Hello from Tilak!")
    except:
        st.info("📷 Profile image not found. Upload your image in the folder!")

# --- Social Icons ---
st.markdown("---")
st.markdown("### 🌐 Connect with me:")

cols = st.columns(4)

with cols[0]:
    st.markdown("""
    <a href="https://github.com/yourgithub" class="social-icon" target="_blank">
        <img src="https://img.icons8.com/color/48/github--v1.png" alt="GitHub"/>
    </a>
    """, unsafe_allow_html=True)

with cols[1]:
    st.markdown("""
    <a href="https://www.linkedin.com/in/tilak-popat-9438042b7?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app" class="social-icon" target="_blank">
        <img src="https://img.icons8.com/color/48/linkedin.png" alt="LinkedIn"/>
    </a>
    """, unsafe_allow_html=True)

with cols[2]:
    st.markdown("""
    <a href="https://www.instagram.com/tilak_popat_?igsh=Yzd2ZWQ3MDB1MXIz" class="social-icon" target="_blank">
        <img src="https://img.icons8.com/color/48/instagram-new--v1.png" alt="Instagram"/>
    </a>
    """, unsafe_allow_html=True)

with cols[3]:
    st.markdown("""
    <a href="mailto:tilakpopat2007@gmail.com" class="social-icon" target="_blank">
        <img src="https://img.icons8.com/color/48/gmail-new.png" alt="Email"/>
    </a>
    """, unsafe_allow_html=True)


st.markdown("""
    <a href="./photo_library" target="_self">
        <button style='font-size:18px; padding:10px 20px;'>📸 Visit Tilak's Photo Library</button>
    </a>
""", unsafe_allow_html=True)
st.markdown("### 🔗 [Go to Tilak's Photo Library](https://portfolio2-7.streamlit.app/)")


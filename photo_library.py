import os
import streamlit as st
from PIL import Image

# Allow opening large images without DecompressionBombError
Image.MAX_IMAGE_PIXELS = None

st.set_page_config(page_title="Tilak's Photo Gallery", layout="wide")

# Main Title
st.title("📸 Tilak's Photography Gallary")

st.markdown("---")

# Small and thinner subtitles
st.markdown("<h4 style='font-weight: 400;'>HIGHLIGHT : Each & Every Photo of this Gallary is clicked by a Mobile Camera !</h4>", unsafe_allow_html=True)
st.markdown("<h4 style='font-weight: 400;'>Model - Redmi Note 13 Pro 5G</h4>", unsafe_allow_html=True)

st.markdown("---")

# Load image folder
image_folder = "images2"
image_files = [f for f in os.listdir(image_folder) if f.endswith((".png", ".jpg", ".jpeg"))]

# Sort to keep consistent order
image_files.sort()

# Create 4-column layout
cols = st.columns(4)

for index, image_file in enumerate(image_files):
    image_path = os.path.join(image_folder, image_file)
    img = Image.open(image_path)

    # Optional: Resize very large images to speed up loading
    max_width = 1200  # Adjust if needed
    if img.width > max_width:
        img = img.resize((max_width, int(img.height * max_width / img.width)))

    with cols[index % 4]:
        st.image(img, use_container_width=False, caption=os.path.splitext(image_file)[0])

st.markdown("---")
st.markdown("### 🔗 [Back To The Home Page](https://tilakpopatportfolio.streamlit.app/)")

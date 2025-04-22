import os
import streamlit as st
from PIL import Image

st.set_page_config(page_title="Tilak's Photo Gallery", layout="wide")

st.title("📸 Tilak's Photography Library")

st.markdown("---")
# Load image folder
image_folder = "images"
image_files = [f for f in os.listdir(image_folder) if f.endswith((".png", ".jpg", ".jpeg"))]

# Sort to keep consistent order
image_files.sort()

# Create 4-column layout
cols = st.columns(4)

for index, image_file in enumerate(image_files):
    image_path = os.path.join(image_folder, image_file)
    img = Image.open(image_path)
try:
    img = Image.open(image_path)
except (FileNotFoundError, Image.UnidentifiedImageError) as e:
    st.error(f"⚠️ Failed to load image: {e}")
    
    with cols[index % 4]:
        st.image(img, use_container_width=False, caption=os.path.splitext(image_file)[0])

st.markdown("---")
st.markdown("### 🔗 [Back To The Home Page](https://tilakpopatportfolio.streamlit.app/)")

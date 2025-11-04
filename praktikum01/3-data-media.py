# import library
import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

# Percobaan Mandiri
st.title("Praktikum 1 - Visualisasi Data")
st.caption("Bagian 3: Data and Media Elements")
st.subheader("praktikum 01 Nama Kelompok")
st.markdown("""
1. ARIA KRISTALLINACHT SUNDANIS - 0110222076
2. BAGUS ACHMAD HIDAYAT - 0110222002
3. AZRIL PUTRA SYAHRI - 0110222197
""")

# Images
import streamlit as st
st.write("Displaying an Images")

# Displaying Image by specifying path
st.image("assets/kucingpembuka.jpg")

# Image Courtesy by unsplash
st.write("Sumber: pinterest.com")


import streamlit as st
# Image Courtesy
st.write("Diplaying Multiple Images")

# Listing out animal images
animal_images = [
    'assets/kucing1.jpg',
    'assets/kucing2.jpg',
    'assets/kucing3.jpg',
    'assets/kucing4.jpg',
]

# Displaying Multiple images with width 150
st.image(animal_images, width=150)

# Image Courtesy
st.write("Sumber: pinterest.com")

#Background Image
import streamlit as st
import base64

# Function to set Image as Background
def add_local_background_image(image):
    with open(image, "rb") as image:
        encoded_string = base64.b64encode(image.read())
    
    # Menampilkan Atribusi Gambar
    st.write("sumber: pinterest.com") 

    # Menerapkan CSS untuk Background
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:files/{"jpg"};base64,{encoded_string.decode()});
        background-size: 50%;
    }}
    </style>
    """,
    unsafe_allow_html=True
    )

st.write("Background Image")

# Calling Image in function
add_local_background_image('assets/kucing6.jpg')

# Resizing an Image
import streamlit as st
from PIL import Image

original_image = Image.open("assets/kucing5.jpg")

# Display Original Image
st.title("Original Image")
st.image(original_image)

# Resizing Image to 600x400
resized_image = original_image.resize((600, 400))

# Displaying Resized Image
st.title("Resized Image")
st.image(resized_image)
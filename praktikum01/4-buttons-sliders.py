# import library
import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

# Percobaan Mandiri
st.title("Praktikum 1 - Visualisasi Data")
st.caption("Bagian 4: Buttons and Sliders")
st.subheader("praktikum 01 Nama Kelompok")
st.markdown("""
1. ARIA KRISTALLINACHT SUNDANIS - 0110222076
2. BAGUS ACHMAD HIDAYAT - 0110222002
3. AZRIL PUTRA SYAHRI - 0110222197
""")

# Buttons
st.title('Creating a Button')

# Defining a Button
button = st.button('Click Here')

if button:
    st.write('You have clicked the Button')
else:
    st.write('You have not clicked the Button')


# Radio Buttons
st.title('Creating Radio Buttons')

# Defining Radio Button
gender = st.radio(
    "Select your Gender",
    ('Male', 'Female', 'Others'))

if gender == 'Male':
    st.write('You have selected Male.')
elif gender == 'Female':
    st.write("You have selected Female.")
else:
    st.write("You have selected Others.")


# Check boxes
st.title('Creating Checkboxes')
st.write('Select your Hobies:')

# Defining Checkboxes
check_1 = st.checkbox('Books')
check_2 = st.checkbox('Movies')
check_3 = st.checkbox('Sports')


# Drop-Downs
st.title('Creating Dropdown')

# Creating Dropdown
hobby = st.selectbox('Choose your hobby: ',
    ('Books', 'Movies', 'Sports'))


# Multiselects
st.title('Multi-Select')

# Defining Multi_Select with Pre-Selection
hobbies = st.multiselect(
    'What are your Hobbies',
    ['Reading', 'Cooking', 'Watching Movies/TV Series', 'Playing', 'Drawing', 'Hiking'],
    ['Reading', 'Playing']
)


# Download Buttons
st.title("Download Button")

# Creating Download Button
down_btn = st.download_button(
    label="Download Image",
    data=open("assets/kucingpembuka.jpg", "rb"),
    file_name="kucingpembuka.jpg",
    mime="image/jpg"
)


# Progress Bars 
import time

st.title('Progress Bar')

# Defining Progress Bar
download = st.progress(0)

for percentage in range(100):
    time.sleep(0.1)
    download.progress(percentage+1)

st.write('Download Complete')


# Spinners
st.title('Spinner')

# Defining Spinner
with st.spinner('Loading...'):
    time.sleep(5)

st.write('Hello Data Scientists')
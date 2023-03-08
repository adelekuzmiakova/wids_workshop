import streamlit as st

def load_expander_crop_hints():
    expander = st.expander("**What is dominant colors?**")
    expander.write(" • **Dominant colors** identifies the colors that **are represented the most** in your photo.  \n • Use the slider below to select the number of dominant colors you want to pull out from your image    \n • The dominant colors with their proportions will be shown.  \n   \n**An example:**")
    expander.image("https://raw.githubusercontent.com/ifolor/ml-demo-app/dev/main/public_assets/cover_image_crop.png", width = 700) 

def write(text, variable):
    return text + variable
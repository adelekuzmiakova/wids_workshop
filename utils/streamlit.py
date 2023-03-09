import streamlit as st

def load_expander_color_hints():
    expander = st.expander("**What is dominant colors?**")
    expander.write(" • **Dominant colors** identifies the colors that **are represented the most** in your photo.  \n • Use the slider on your left to select the number of dominant colors you want to pull out from your image    \n • The dominant colors with their proportions will be shown.")

def load_expander_restoring_hints():
    expander = st.expander("**What is image enhacement?**")
    expander.write(" • **Image enhacement** feature can be used to adjust colour, contrast, brightness and sharpness.   \n • For more information please see the Pillow reference docs: https://pillow.readthedocs.io/en/stable/reference/ImageEnhance.html   \n • Use the slider on your left to adjust the contrast, brigthness, or sharpness.")

def write(text, variable):
    return text + variable
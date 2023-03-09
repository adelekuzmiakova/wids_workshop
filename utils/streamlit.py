import streamlit as st

def load_expander_color_hints():
    expander = st.expander("**What is dominant colors?**")
    expander.write(" • **Dominant colors** identifies the colors that **are represented the most** in your photo.  \n • Use the slider below to select the number of dominant colors you want to pull out from your image    \n • The dominant colors with their proportions will be shown.  \n   \n**An example:**")
    expander.image("https://raw.githubusercontent.com/adelekuzmiakova/wids_workshop/main/public_assets/image_2.png?token=GHSAT0AAAAAAB7YOPJYRCM2HTGFSEXGLYBYZAI7XDQ", width = 650) 

def load_expander_restoring_hints():
    expander = st.expander("**What is image enhacement?**")
    expander.write(" • **Image enhacement** identifies the colors that **are represented the most** in your photo.  \n • Use the slider below to select the number of dominant colors you want to pull out from your image    \n • The dominant colors with their proportions will be shown.  \n   \n**An example:**")
    expander.image("https://raw.githubusercontent.com/adelekuzmiakova/wids_workshop/main/public_assets/image_2.png?token=GHSAT0AAAAAAB7YOPJYJUTXCISXTCYZ3A2IZAI5E4Q", width = 650) 


def write(text, variable):
    return text + variable
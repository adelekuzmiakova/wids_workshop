import streamlit as st

def load_expander_crop_hints():
    expander = st.expander("**What is crop hints?**")
    expander.write(" • **Crop hints** identifies the **area of interest** in your photo and removes distracting elements.   \n • You can specify the **aspect (width:height) ratio**, such as 1:1 (square) or 16:9 (long panorama), of the final cropped image using the left sidebar).  \n • Then upload your image and you will be shown the **cropped version**.  \n   \n**An example:**")
    expander.image("https://raw.githubusercontent.com/ifolor/ml-demo-app/dev/main/public_assets/cover_image_crop.png", width = 700) 

def write(text, variable):
    return text + variable
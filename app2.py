import os
import sys
import pandas as pd
import numpy as np 
from io import BytesIO
from glob import glob
from PIL import Image, ImageEnhance
import streamlit as st

from utils.streamlit import *


st.image("logo.jpg")
st.subheader("Which feature do you want to test?")
tab_1, tab_2, tab_3 = st.tabs(["Dominant colors", "Image enhacement", "Object detection"])

with tab_1:
    load_expander_crop_hints() 

    uploaded_file = st.file_uploader("", type=['jpg','png','jpeg'])
    if uploaded_file is not None:
        with st.sidebar:
            # sidebar where user can select aspect ratio
            st.markdown('Please select the desired aspect ratio.')
            aspect_ratio_options = ["16:9", "4:3", "1:1", "4:5", "None"]
            aspect_ratio_input = st.radio("", aspect_ratio_options)
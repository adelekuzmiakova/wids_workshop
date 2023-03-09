import os
import sys
import pandas as pd
import numpy as np 
from io import BytesIO
from glob import glob
from PIL import Image, ImageEnhance
import streamlit as st
from sklearn.cluster import KMeans
import cv2

from utils.streamlit import *


st.image("logo.jpg", width = 600)
st.subheader("Which feature do you want to test?")
tab_1, tab_2, tab_3 = st.tabs(["Dominant colors", "Image enhancement", "Object detection"])

with tab_1:
    load_expander_color_hints() 
    with st.container(): 

        uploaded_file = st.file_uploader("", type=['jpg','png','jpeg'], key = "dominant_colors")
        if uploaded_file is not None:
            with st.sidebar:
                # sidebar where user can select the number of dominant colors
                st.markdown('Dominant colors')
                num_clusters = st.slider(label = "How many colors do you want to identify?", min_value = 1, max_value = 10, value = 5, step = 1)

            # function call
            col_1, col_2 = st.columns(np.ones(2)*0.5)
            with col_1:
                image = Image.open(uploaded_file)
                st.markdown('<p style="text-align: center;">Original image</p>',unsafe_allow_html=True)
                st.image(image, channels="BGR") 

            with col_2:
                image = np.asarray(image)
                img = image.reshape((image.shape[0] * image.shape[1],image.shape[2])) 


                clt = KMeans(n_clusters = num_clusters) # "pick out" the K-means tool from our collection of algorithms
                clt.fit(img) # apply the model to our data, the image

                print(clt.labels_)

                label_indx = np.arange(0,len(np.unique(clt.labels_)) + 1) 

                (hist, _) = np.histogram(clt.labels_, bins = label_indx) # count the number of pixels in each cluster
                hist = hist.astype("float") # convert to float
                hist /= hist.sum() # normalize the histogram

                hist_bar = np.zeros((50, 300, 3), dtype = "uint8")
                startX = 0
                for (percent, color) in zip(hist,  clt.cluster_centers_): 
                    endX = startX + (percent * 300) # to match grid
                    cv2.rectangle(hist_bar, (int(startX), 0), (int(endX), 50), color.astype("uint8").tolist(), -1)
                    startX = endX

                st.markdown('<p style="text-align: center;">Dominant colors</p>',unsafe_allow_html=True)
                st.image(hist_bar, channels="RBG") 


with tab_2:
    load_expander_restoring_hints() 
    with st.container():

        uploaded_file = st.file_uploader("", type=['jpg','png','jpeg'], key = "image_enhancement")
        if uploaded_file is not None:
            with st.sidebar:
                # sidebar where user can select the contrast factor
                st.markdown('Contrast')
                contrast = st.slider(label = "Use the slider to control the contrast of an image, similar to the contrast control on a TV set. An enhancement factor of 0.0 gives a solid grey image. A factor of 1.0 gives the original image.", min_value = 0.0, max_value = 4.0, value = 1.0, step = 0.1)

                # sidebar where user can select the brightness factor
                st.markdown('Brightness')
                brightness = st.slider(label = "Use the slider to control the control the brightness of an image. An enhancement factor of 0.0 gives a black image. A factor of 1.0 gives the original image.", min_value = 0.0, max_value = 4.0, value = 1.0, step = 0.1)



            col_1, col_2, col_3 = st.columns(3)
            with col_1:
                image = Image.open(uploaded_file)
                st.markdown('<p style="text-align: center;">Original image</p>',unsafe_allow_html=True)
                st.image(image, channels="BGR") 

            with col_2:
                contrast_enhancer = ImageEnhance.Contrast(image)
                contrasted_image = contrast_enhancer.enhance(contrast)

                st.markdown('<p style="text-align: center;">Contrasted image</p>',unsafe_allow_html=True)
                st.image(contrasted_image, channels="BGR")

            with col_3:
                brightness_enhancer = ImageEnhance.Brightness(image)
                brightened_image = brightness_enhancer.enhance(brightness)

                st.markdown('<p style="text-align: center;">Brightned image</p>',unsafe_allow_html=True)
                st.image(brightened_image, channels="BGR")

                
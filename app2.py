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


st.image("logo.jpg")
st.subheader("Which feature do you want to test?")
tab_1, tab_2, tab_3 = st.tabs(["Dominant colors    ", "Image enhancement    ", "Object detection    "])

with tab_1:
    load_expander_crop_hints() 

    uploaded_file = st.file_uploader("", type=['jpg','png','jpeg'])
    if uploaded_file is not None:
        with st.sidebar:
            # sidebar where user can select aspect ratio
            num_clusters = st.slider(label = "How many colors do you want to identify?", min_value = 1, max_value = 10, value = 5, step = 1)

        with st.container(): 
            # function call

            col_1, col_2 = st.columns(np.ones(2)*0.5)
            with col_1:
                image_bytes = uploaded_file.read()
                image = Image.open(uploaded_file)
                st.markdown('<p style="text-align: center;">Original image</p>',unsafe_allow_html=True)
                st.image(image, channels="BGR") 

            with col_2:
                image = np.asarray(image)
                img = image.reshape((image.shape[0] * image.shape[1],image.shape[2])) 
                print(img.shape)


                clt = KMeans(n_clusters = num_clusters) # "pick out" the K-means tool from our collection of algorithms
                clt.fit(img) # apply the model to our data, the image

                print(clt.labels_)

                label_indx = np.arange(0,len(np.unique(clt.labels_)) + 1) 

                (hist, _) = np.histogram(clt.labels_, bins = label_indx) # count the number of pixels in each cluster
                hist = hist.astype("float") # convert to float
                hist /= hist.sum() # normalize the histogram
                print(hist)

                hist_bar = np.zeros((50, 300, 3), dtype = "uint8")
                startX = 0
                for (percent, color) in zip(hist,  clt.cluster_centers_): 
                    endX = startX + (percent * 300) # to match grid
                    cv2.rectangle(hist_bar, (int(startX), 0), (int(endX), 50), color.astype("uint8").tolist(), -1)
                    startX = endX

                st.markdown('<p style="text-align: center;">Dominant colors</p>',unsafe_allow_html=True)
                st.image(hist_bar, channels="RBG") 
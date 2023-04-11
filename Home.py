import streamlit as st
from PIL import Image
from matplotlib import image
import os

#Title of the home page
st.header(":brown[Laptop Price Prediction:desktop_computer]")
#Using subheader
st.write('Created By: :green[Nettetla Hrushikesh]')

#Adding Image
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
dir_of_interest = os.path.join(FILE_DIR, "resourses")
IMAGE_PATH = os.path.join(dir_of_interest, "image")
IMAGE_PATH1 = os.path.join(IMAGE_PATH, "laptop img for project.jpg")

img = image.imread(IMAGE_PATH1)
st.image(img)

#Using markdown cell type
st.markdown(":blue[check out:]",)

#Creating column layout
col1,col2=st.columns(2, gap='small')
with col1:
    st.write("[LinkedIn](https://www.linkedin.com/in/hrushikeshnettetla425/)")
with col2:
    st.write("[GitHub](https://github.com/Hrushikeshnettetla)")
import streamlit as st
#import tensorflow as tf
import os
from AI import AI
from PIL import Image


#categories of food
catgories = ['chicken', 'rice', 'broccoli', 'ramen', 'kale']


def app():
    # Include the reference to your CSS file in the HTML header
    st.write("""
    <head>
    <link rel="stylesheet" type="text/css" href="/Users/crystalhuang/cruz_hacks/coding-connoisseurs-/style.css">
    </head>
    """, unsafe_allow_html=True)

    with open("howitworks.html", "r") as f:
        html_content = f.read()
    
    st.markdown(
        html_content,
        unsafe_allow_html=True,
)
    st.title("Food Recognition App")
    uploaded_file = st.file_uploader("Upload an image of food:", type=["jpg", "jpeg", "png",])
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image', use_column_width=True)
        im = image.resize((224, 224))
        im = list(im.getdata())
        a = AI(im)
        st.write("The food is the image of a(n) {}".format(a.classify()))

st.write("""
# Pictrition
# Weekly Diet Tracker
# """)


# Run the app
if __name__ == '__main__':
    app()

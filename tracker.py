import streamlit as st
import os
import utils as utl
#import tensorflow as tf
import os
from AI import AI
from PIL import Image



#categories of food
catgories = ['chicken', 'rice', 'broccoli', 'ramen', 'kale']


def app():
    st.title("Food Recognition App")
    st.write("""
    # Pictrition
    # Weekly Diet Tracker
    # """)
   #load the CSS
    # Reading the HTML file
    with open("howitworks.html", "r") as file:
        html_content = file.read()
    # Reading the CSS file
    with open("style.css", "r") as file:
        css_content = file.read()
    # Inlining the CSS styles in the HTML
    html_string = f"<style>{css_content}</style>{html_content}"

    # Adding the HTML string to Streamlit
    st.markdown(html_string, unsafe_allow_html=True)
    uploaded_file = st.file_uploader("Upload an image of food:", type=["jpg", "jpeg", "png",])
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image', use_column_width=True)
        im = image.resize((224, 224))
        im = list(im.getdata())
        a = AI(im)
        st.write("The food is the image of a(n) {}".format(a.classify()))



# Run the app
if __name__ == '__main__':
    app()

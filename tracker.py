import streamlit as st
import os
#import tensorflow as tf
import os
from AI import AI
from PIL import Image
#import matplotlib.pyplot as plt


#categories of food
catgories = ['chicken', 'rice', 'broccoli', 'ramen', 'kale']


def app():
    st.title("Pictrition")
    st.header("Your Weekly Diet Tracker")

   #load the CSS
    # Reading the HTML file
    # with open("homepage.html", "r") as file:
    #     html_content = file.read()
    # # Reading the CSS file
    # with open("style.css", "r") as file:
    #     css_content = file.read()
    # # Inlining the CSS styles in the HTML
    # html_string = f"<style>{css_content}</style>{html_content}"

    # Adding the HTML string to Streamlit
    # st.markdown(html_string, unsafe_allow_html=True)
    uploaded_file = st.file_uploader("Upload an image of food:", type=["jpg", "jpeg", "png",])
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image', use_column_width=True)
        im = image.resize((224, 224))
        im = list(im.getdata())
        a = AI(im)
        category, error = a.classify()
        st.write("The food is the image of a(n) {}".format(a.classify()))
    
    with open("weekly.txt", "a") as f:
        f.write(category)
        f.write("\n")

    def analyze_week():
        with open("weekly.txt", "r") as f:
            indexes = {'meat':0, 'vegetable':1, 'bread':2, 'fruit':3}
            counts = [0 for _ in range(len(indexes))]
            for line in f:
                counts[indexes[line[:-1]]] += 1
            #plt.pie(counts, labels=list(indexes.keys()))
            #plt.savefig("pie_chart.png")
    analyze_week()



# Run the app
if __name__ == '__main__':
    app()

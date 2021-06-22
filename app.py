import streamlit as st
from classify import teachable_machine_classification
from PIL import Image


st.title("Food Image Classifier")

st.write("chicken_curry, chicken_wings, fried rice, grilled salmon, hamburger, ice_cream, pizza, ramen, steak, sushi")

st.write("These food classes can be recognised by the model. Have Fun")

class_names = ['chicken_curry', 'chicken_wings', 'fried_rice', 'grilled_salmon',
       'hamburger', 'ice_cream', 'pizza', 'ramen', 'steak', 'sushi']
     



uploaded_file = st.file_uploader("Upload Your Image JPG FORMAT ONLY ", type="jpg")
if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption='Your image', use_column_width=True)
        st.write("")
        st.write("Classifying...")
        label = pred_plot(image,class_names)
        st.write(label)


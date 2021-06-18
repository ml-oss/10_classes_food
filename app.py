import streamlit as st
from classify import teachable_machine_classification
from PIL import Image





uploaded_file = st.file_uploader("img", type="jpg")
if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption='img', use_column_width=True)
        st.write("")
        st.write("Classifying...")
        label = teachable_machine_classification(image, 'model.sav')
        if label == 0:
            st.write("chicken_curry")  
        if label == 1:
            st.write("chicken_wings")
        if label == 2:
            st.write("fried_rice")
        if label == 3:
            st.write("grilled_salmon")
        if label == 4:
            st.write("hamburger")

        if label == 5:
            st.write("ice_cream")

        if label == 6:
            st.write("pizza")
        
        if label == 7:
            st.write("ramen")
        
        if label == 8:
            st.write("steak")

        if label == 9:
            st.write("sushi")

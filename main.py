# importing library
import streamlit as st
from PIL import Image
# level one h1
st.title(':green[welcome to streamlit]')
st.text('we are learning python')
st.markdown('### hello')

st.success("✔️we sucessfully done")
st.warning("Dont do this")
st.info("Dig deeper")
img=Image.open("Template.jpg")
st.img(img,width="500")
st.video("")
# st.slider()

# st.exception(exp)
# image=st.camera_input('enter you feed')
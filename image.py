import requests
import streamlit as st
import base64
import io
from PIL import Image

def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

img_base64 = get_img_as_base64("D:\Screenshots\pro.png")

page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("data:image/png;base64,{img_base64}");
background-size: cover;
}}
[data-testid="stHeader"]{{
background: rgba(0,0,0,0);
}}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0"
headers = {"Authorization": "Bearer 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"}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.content

# Streamlit UI
prompt = st.text_input('Enter a prompt:')
if st.button('Generate'):
    if prompt:
        image_bytes = query({"inputs": prompt})
        image = Image.open(io.BytesIO(image_bytes))  # Open the image from bytes
        st.image(image)
    else:
        st.write("Please enter a prompt.")

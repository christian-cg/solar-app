import streamlit as st
import pandas as pd
import requests
import ipdb

st.set_page_config(
    page_title='Solar project',
    layout='wide'
)

# header_html = """
# <div style="padding:0px; border:0px; border-radius:0px; background:url(https://images.unsplash.com/photo-1625301840055-7c1b7198cfc0?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=2942&q=80); height:200px;">
#     <h1 style="color:#333;text-align:center;"></h1>
# </div>
# """

# st.markdown(header_html, unsafe_allow_html=True)

#url = st.secrets['url']
#url = 'http://localhost:8000/predict'
url = 'https://solarpanelstatus-z7imutgpsq-ew.a.run.app/predict'

st.header("Solar panel condition classifier")
st.markdown("""
            Evaluate if a solar panel is **clean**, **damaged** or **dirty**
            """)

# Allow users to upload images for evaluation
uploaded_files = st.file_uploader("Upload images:",
                                 type=['jpeg', 'jpg', 'png'],
                                 accept_multiple_files=True)


if st.button("Evaluate images", type='primary'):
    # Check if any files where uploaded
    if uploaded_files:
        col_header_1, col_header_2 = st.columns(2)
        with col_header_1:
            st.markdown('**Image**')
        with col_header_2:
            st.markdown('**Class**')
        # Fetch the model's classification results
        for uploaded_file in uploaded_files:
            bytes_data = uploaded_file.getvalue()
            files = {"image": (bytes_data)}
            response = requests.post(url, files=files)
            if response.status_code == 200:
                result = response.json()['predition'] # Warning: this typo is in the API deployed to the cloud. But fixed and merged on GH repo.
                col1, col2 = st.columns(2)
                with col1:
                    st.image(bytes_data, caption=uploaded_file.name, width=200)
                with col2:
                    st.markdown(f"The image was classified as **{result}**.")
            else:
                st.error(f"Error uploading the image: {uploaded_file.name}")
    else:
        st.warning("You need to upload an image to be evaluated.")



### Single image upload ###

# response = requests.post(url, files={"image": ("image.jpg", bytes_data, "image/jpeg")})

# if uploaded_files is not None:
#     files = {uploaded_file.name: (bytes_data)}
#     st.image(bytes_data)
#     st.write(bytes_data)

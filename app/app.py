import streamlit as st
import pandas as pd
import requests
import time
import ipdb

# Page config
st.set_page_config(
    page_title='Solar project',
    layout='wide'
)

# Custom CSS
css = """
<style>
    .page-header {
        height:128px;
        margin: 0 0 0 0;
        padding: 0 0 0 0;
        border: 0;
        border-radius: 16px 16px 0 0;
        background-image: url(https://images.unsplash.com/photo-1625301840055-7c1b7198cfc0?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=2942&q=80);
        background-position: center;
    }
    .css-z5fcl4 {
        padding-top: 48px;
    }
</style>
"""

st.markdown(css, unsafe_allow_html=True)

# Custom HTML elements
header_html = """
<div class="page-header"></div>
"""

st.markdown(header_html, unsafe_allow_html=True)

# Streamlit app
url = st.secrets['url']

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
        col_header_1, col_header_2, col_header_3 = st.columns(3)
        with col_header_1:
            st.markdown('**Image**')
        with col_header_2:
            st.markdown('**Class**')

        # with st.spinner('Wait for it...'):
        #     time.sleep(8)
        # st.success('Done!')

        # Fetch the model's classification results
        for uploaded_file in uploaded_files:
            bytes_data = uploaded_file.getvalue()
            files = {"image": (bytes_data)}
            response = requests.post(url, files=files)
            if response.status_code == 200:
                result = response.json()['prediction']
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.image(bytes_data, caption=uploaded_file.name, width=256)
                with col2:
                    st.markdown(f"The image was classified as **{result}**.")
            else:
                st.error(f"Error uploading the image: {uploaded_file.name}")
    else:
        st.warning("You need to upload an image to be evaluated.")

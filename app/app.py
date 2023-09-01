import streamlit as st
import requests
import pdb

#url = st.secrets['url']
url = 'http://localhost:8501/predict'

st.header("Solar panel condition classifier")
st.text("""Upload an image to evaluate the condition of solar panels.""")

# Allow users to upload images
uploaded_files = st.file_uploader("Upload an image file:",
                                 type=['jpeg', 'jpg', 'png'],
                                 accept_multiple_files=True)

for uploaded_file in uploaded_files:
    bytes_data = uploaded_file.getvalue()

if uploaded_files is not None:
    files = {uploaded_file.name: (bytes_data)}

    st.image(bytes_data)
    st.write(uploaded_file.name)
    #st.write(bytes_data)

@breakpoint

# Evaluate images and retrieve the model's classification results
if st.button("Evaluate"):
    response = requests.post(url, files=files)

    result = response.json()

    st.write("Response status code: ", response.status_code)
    st.write("API response: ", result)

    # if response.status_code == 200:
    #     result = response.json()
    #     st.success("Images uploeaded succesfully!")
    #     st.write("API response: ", result)
    # else:
    #     st.error("Images upload failed.")

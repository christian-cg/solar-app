import streamlit as st
import requests
import ipdb

#url = st.secrets['url']
url = ''

st.header("Solar panel condition classifier")
st.text("""Upload an image to evaluate the condition of solar panels.""")

# Allow users to upload images
uploaded_files = st.file_uploader("Upload an image file:",
                                 type=['jpeg', 'jpg', 'png'],
                                 accept_multiple_files=True)

if st.button("Evaluate images"):
    # Check if any files where uploaded
    if uploaded_files:
        # Fetch the model's classification results
        for uploaded_file in uploaded_files:
            bytes_data = uploaded_file.getvalue()

            files = {uploaded_file.name: (bytes_data)}

            response = requests.post(url, files=files)

            st.write("API response status code: ", response.status_code)

            if response.status_code == 200:
                st.success("Image uploaded succesfully!")
                result = response.json()
                st.write(f"API response: {uploaded_file.name} is {result}")
                st.write("Image:")
                st.image(bytes_data)
            else:
                st.error(f"Error uploading the image: {uploaded_file.name}")
    else:
        st.warning("You need to upload an image to be evaluated.")

breakpoint()

response = requests.post(url, files={"image": ("image.jpg", bytes_data, "image/jpeg")})

if uploaded_files is not None:
    files = {uploaded_file.name: (bytes_data)}

    st.image(bytes_data)
    st.write(uploaded_file.name)
    #st.write(bytes_data)

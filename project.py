'''
Project:    CS50 Python Final
Author:     Regina Chua
Date:       DEC 2024

Instructions:
Your project must be implemented in Python.
Your project must have a main function and three or more additional functions. At least three of those additional functions must be accompanied by tests that can be executed with pytest.
Your main function must be in a file called project.py, which should be in the “root” (i.e., top-level folder) of your project.
Your 3 required custom functions other than main must also be in project.py and defined at the same indentation level as main (i.e., not nested under any classes or functions).
Your test functions must be in a file called test_project.py, which should also be in the “root” of your project. Be sure they have the same name as your custom functions, prepended with test_ (test_custom_function, for example, where custom_function is a function you’ve implemented in project.py).
You are welcome to implement additional classes and functions as you see fit beyond the minimum requirement.
Implementing your project should entail more time and effort than is required by each of the course’s problem sets.
Any pip-installable libraries that your project requires must be listed, one per line, in a file called requirements.txt in the root of your project.

References:
https://docs.streamlit.io/get-started/tutorials/create-an-app
https://docs.streamlit.io/develop/api-reference/caching-and-state/st.session_state
https://docs.streamlit.io/develop/api-reference/media/st.image
https://discuss.streamlit.io/t/how-do-i-use-a-background-image-on-streamlit/5067
https://github.com/deepankarvarma/Photo-Collage-Maker-Using-Python/blob/master/app.py

'''

# Import packages
import streamlit as st
from PIL import Image, ImageOps
import requests
from io import BytesIO

# Set streamlit page title
st.set_page_config(page_title="Mosaic Maker by Regina Chua", page_icon="🖼️")

# Adding a background
st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://4kwallpapers.com/images/wallpapers/macos-monterey-wwdc-21-stock-dark-mode-5k-4480x2520-5585.jpg");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

# 1st function - initialize session
def initialize_session_state():
    if 'images' not in st.session_state:
        st.session_state.images = []

# 2nd function - image uploading
def handle_file_upload(uploaded_files):
    if uploaded_files:
        for uploaded_file in uploaded_files:
            image = Image.open(uploaded_file)
            if image not in st.session_state.images:
                st.session_state.images.append(image)

# 3rd function - image linking
def handle_image_urls(image_urls):
    if image_urls:
        urls = image_urls.split('\n')
        for url in urls:
            try:
                response = requests.get(url)
                image = Image.open(BytesIO(response.content))
                if image not in st.session_state.images:
                    st.session_state.images.append(image)
            except Exception as e:
                st.error(f"Error loading image from URL: {url}. Error: {e}")

# 4th function - making the mosaic
def create_mosaic(images):
    max_width = max(img.width for img in images)
    max_height = max(img.height for img in images)
    num_columns = 3
    num_rows = (len(images) + num_columns - 1) // num_columns
    mosaic_width = num_columns * max_width
    mosaic_height = num_rows * max_height

    # Create a new blank image
    mosaic = Image.new('RGB', (mosaic_width, mosaic_height))

    # Paste images
    for index, img in enumerate(images):
        row = index // num_columns
        col = index % num_columns
        x = col * max_width
        y = row * max_height
        mosaic.paste(ImageOps.fit(img, (max_width, max_height)), (x, y))

    return mosaic

# Main function
def main():
    st.title("Mosaic Maker")
    st.subheader("App developed by Regina Chua")
    st.text("This app generates a 3-column grid-style mosaic where the images are cropped to fixed dimensions. Alternatively, you can screenshot the preview section if you prefer to retain the image's original dimensions.")

    # Initialize session state
    initialize_session_state()

    # Image upload
    st.header("Add your images")
    uploaded_files = st.file_uploader("Choose image/s...", type=["jpg", "jpeg", "png"], accept_multiple_files=True)
    handle_file_upload(uploaded_files)

    # Image URL
    image_urls = st.text_area("Or enter image URLS (one per line)")
    handle_image_urls(image_urls)

    # Refresh preview
    if st.button("Refresh Preview"):
        st.session_state.images = []
        handle_file_upload(uploaded_files)
        handle_image_urls(image_urls)

    # Display images in a grid preview
    if st.session_state.images:
        st.subheader("Images in Memory")
        cols = st.columns(3)
        for i, img in enumerate(st.session_state.images):
            col = cols[i % 3]
            col.image(img, use_container_width=True)

    # Title for mosaic
    st.header("Export as Mosaic")
    title = st.text_input("Name the mosaic with image filetype:", value="mosaic.png")

    # Make mosaic
    if st.button("Make Mosaic"):
        if st.session_state.images:
            collage = create_mosaic(st.session_state.images)
            st.image(collage, caption=title)

            st.text("Give the app a moment. A button will appear below to download the mosaic.")

            # Download button
            img_byte_arr = BytesIO()
            collage.save(img_byte_arr, format='PNG')
            img_byte_arr = img_byte_arr.getvalue()
            st.download_button(label="Download Mosaic", data=img_byte_arr, file_name=title, mime="image/png")
        else:
            st.error("Please upload at least one image.")

if __name__ == "__main__":
    main()

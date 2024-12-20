'''
Instructions:
Your project must be implemented in Python.
Your project must have a main function and three or more additional functions. At least three of those additional functions must be accompanied by tests that can be executed with pytest.
Your main function must be in a file called project.py, which should be in the “root” (i.e., top-level folder) of your project.
Your 3 required custom functions other than main must also be in project.py and defined at the same indentation level as main (i.e., not nested under any classes or functions).
Your test functions must be in a file called test_project.py, which should also be in the “root” of your project. Be sure they have the same name as your custom functions, prepended with test_ (test_custom_function, for example, where custom_function is a function you’ve implemented in project.py).
You are welcome to implement additional classes and functions as you see fit beyond the minimum requirement.
Implementing your project should entail more time and effort than is required by each of the course’s problem sets.
Any pip-installable libraries that your project requires must be listed, one per line, in a file called requirements.txt in the root of your project.

My notes:
This python project will be executed in streamlit.
The functions include:
* add_images() - add images (by file upload or by URL)
* add_title() - add title (for the filename) (optional, so the default is mosaic.png)
* collage_images() - collage images in a mosaic grid layout
* download_collage() - download collage as an image

tests:
* test_add_images()
* test_add_title()
* test_collage_images()

'''

import streamlit as st
from PIL import Image
import requests
from io import BytesIO

def main():
    st.title("Mosaic Maker - app developed by Regina Chua")

    uploaded_file = st.file_uploader("Choose an image...", type=["jpg","jpeg", "png"])
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_container_width=True)

    image_url = st.text_input("Or enter an image URL")
    if image_url:
        try:
            response = requests.get(image_url)
            image = Image.open(BytesIO(response.content))
            st.image(image, caption="Image from URL", use_container_width=True)
        except Exception as e:
            st.error("Error loading image from URL.")

if __name__ == "__main__":
    main()

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
'''

import pytest
from io import BytesIO
from PIL import Image
from unittest.mock import patch, MagicMock
import streamlit as st
from project import initialize_session_state, handle_file_upload, handle_image_urls, display_image_grid, create_mosaic

def test_initialize_session_state():
    with patch.dict(st.session_state, {}, clear=True):
        initialize_session_state()
        assert 'images' in st.session_state, "Session state should include 'images'."
        assert st.session_state['images'] == [], "Session state's 'images' should be an empty list."

def create_test_image(color, width, height):
    img = Image.new("RGB", (width, height), color)
    byte_arr = BytesIO()
    img.save(byte_arr, format='PNG')
    byte_arr.seek(0)
    return byte_arr

def test_handle_file_upload():
    test_image = create_test_image("blue", 100, 100)
    uploaded_files = [test_image]

    with patch.dict(st.session_state, {}, clear=True):
        initialize_session_state()
        handle_file_upload(uploaded_files)
        assert len(st.session_state.images) == 1, "One image should be added to session state."
        assert st.session_state.images[0].size == (100, 100), "The image should be 100x100 in size."

def test_handle_image_urls():
    test_url = "https://i.pinimg.com/736x/7b/1b/bb/7b1bbb5bc4947531f58ec6a3109ba18e.jpg" # my art as a placeholder test
    test_image = create_test_image("blue", 100, 100)
    
    with patch('requests.get') as mock_get:
        mock_response = MagicMock()
        mock_response.content = test_image.getvalue()
        mock_get.return_value = mock_response

        with patch.dict(st.session_state, {}, clear=True):
            initialize_session_state()
            handle_image_urls(test_url)
            assert len(st.session_state.images) == 1, "One image should be added to session state."
            assert st.session_state.images[0].size == (100, 100), "The image should be 100x100 in size."

def test_display_image_grid():
    test_image1 = create_test_image("red", 100, 100)
    test_image2 = create_test_image("green", 100, 100)
    test_image3 = create_test_image("blue", 100, 100)
    images = [Image.open(test_image1), Image.open(test_image2), Image.open(test_image3)]

    with patch.dict(st.session_state, {}, clear=True):
        initialize_session_state()
        st.session_state.images = images

        with patch('streamlit.columns') as mock_columns:
            mock_cols = [MagicMock() for _ in range(3)]
            mock_columns.return_value = mock_cols

            # Mock the image call on each column
            for col in mock_cols:
                col.image = MagicMock()

            display_image_grid(st.session_state.images)

            mock_columns.assert_called_once_with(3)
            for col in mock_cols:
                col.image.assert_called_once()

# I'm a bit color blind and the computer seems to be as well so...
def is_approximately_green(color):
    r, g, b = color
    return r == 0 and 120 <= g <= 255 and b == 0

def test_create_mosaic():
    images = [
        create_test_image("red", 100, 100),
        create_test_image("green", 100, 100),
        create_test_image("blue", 100, 100),
    ]

    # Convert BytesIO to PIL Images
    pil_images = [Image.open(img) for img in images]

    # Pass images to create_mosaic function
    mosaic = create_mosaic(pil_images)

    # Save the mosaic for manual inspection
    mosaic.save("./images/test_mosaic_debug.png")

    # Assert the size of the mosaic
    assert mosaic.size == (300, 100), f"Unexpected mosaic size: {mosaic.size}"

    # Adjust pixel sampling coordinates for expected placement
    left_color = mosaic.getpixel((50, 50))  # Should be red
    middle_color = mosaic.getpixel((150, 50))  # Should be green
    right_color = mosaic.getpixel((250, 50))  # Should be blue

    assert left_color == (255, 0, 0), f"Top left image should be red, got {left_color}"
    assert is_approximately_green(middle_color), f"Middle image should be green, got {middle_color}"
    assert right_color == (0, 0, 255), f"Top right image should be blue, got {right_color}"

# Run the tests
if __name__ == "__main__":
    pytest.main()

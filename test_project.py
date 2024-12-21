import pytest
from io import BytesIO
from PIL import Image
from project import create_mosaic

def create_test_image(color, width, height):
    """Creates a test image of a specified color and size."""
    return Image.new("RGB", (width, height), color)

def test_create_mosaic():
    """Tests the create_mosaic function for correct mosaic generation."""
    # Create three test images
    images = [
        create_test_image("red", 100, 100),
        create_test_image("green", 100, 100),
        create_test_image("blue", 100, 100),
    ]

    # Pass images to create_mosaic function
    mosaic = create_mosaic(images)

    # Assert the size of the mosaic
    assert mosaic.size == (300, 100), f"Unexpected mosaic size: {mosaic.size}"

    # Check pixel colors for expected arrangement
    assert mosaic.getpixel((50, 50)) == (255, 0, 0), "Top left image should be red"
    assert mosaic.getpixel((150, 50)) == (0, 255, 0), "Top middle image should be green"
    assert mosaic.getpixel((250, 50)) == (0, 0, 255), "Top right image should be blue"

def test_add_images():
    """Tests the function that adds images to the session state."""
    from project import add_images

    # Simulate session state and uploaded images
    session_state = {"images": []}
    test_images = [
        create_test_image("red", 100, 100),
        create_test_image("blue", 100, 100),
    ]

    # Add images and check session state
    add_images(session_state, test_images)
    assert len(session_state["images"]) == 2, "Expected 2 images in session state."
    assert session_state["images"][0].getpixel((50, 50)) == (255, 0, 0), "First image should be red."

def test_add_title():
    """Tests the function that adds a title to the mosaic."""
    from project import add_title

    # Mock title input
    title = "mosaic.png"
    result_title = add_title(title)

    # Assert the result
    assert result_title == "mosaic.png", f"Expected title to be 'mosaic.png', got {result_title}"

def test_download_collage():
    """Tests the download_collage function to verify download functionality."""
    from project import download_collage

    # Create a test image
    test_image = create_test_image("yellow", 300, 100)

    # Mock a download function and check the byte content
    download_bytes = download_collage(test_image, "test_collage.png")
    assert isinstance(download_bytes, BytesIO), "Expected a BytesIO object."
    assert len(download_bytes.getvalue()) > 0, "Download content should not be empty."

# Run the tests
if __name__ == "__main__":
    pytest.main()

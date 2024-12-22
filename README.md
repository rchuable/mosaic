# MOSAIC MAKER
#### Video Demo: https://youtu.be/COVwBVFQV_I
#### Description:

![Screenshot of Mosaic Maker UI](images/mosaic_maker_ui.jpg)

[![Open in Streamlit](https://img.shields.io/badge/Open%20in-Streamlit-brightgreen)](https://mosaicmaker.streamlit.app/)

Mosaic Maker is streamlit application I designed to quickly collage images in a 3-column grid to use as a reference. This can apply to vision boards, art reference sheets, palette combinations, mood boards, meme grids (e.g., favorite anime 3x3), and more.

In my case as a digital artist, I wanted a quick way to build **reference sheets**. Similar to a bibliography in research writing, reference sheets are an artist's visual bibliography; it sets the start for how we determine the composition, lighting, colors, and textures that go into a piece. Since I also make fanart, I need reference images to get specific elements, such as a character's hair or clothing, into the canvas.

Here is sample mosaic output for a Jinx & Isha reference:
![Mosaic output of Jinx from Arcane](images/jinx.png)

Then here is my art derived from this reference:
![Art by Courage artwork of Jinx from Arcane, titled Jinx Leading the People, depicted from Eugene Delacroix's Liberty Leading the People](https://i.pinimg.com/736x/7b/1b/bb/7b1bbb5bc4947531f58ec6a3109ba18e.jpg)

Let's get into it! Mosaic Maker features the following functions:
- Add images by local file upload and/or URL
- Customize filename (optional)
- Refresh preview of images
- Collage the images into a 3-column mosaic
- Download the mosaic as an image with the customized filename

Adding images by local file helps if I have the images stored there, where that my be screenshots from the show or a video. On the other hand, I like to conserve my PC storage space, so I also built a function to add images by URL. Image URLS can be found when right-clicking the image and copying the image link, where that may be directed to wherever it's hosted i.e., on Pinterest, Google, and other image-hosting websites.

I added a function for refreshing the preview of images stored in the session (or app's memory as it's called in the UI) if I wanted to add or remove more images. Frankly the preview is already great as-is for a screenshot, but it wouldn't be any different from building a Pinterest board and taking a screenshot of that. I much prefer it to be a quick and organized layout. Hence I built the collage or mosaic-making function and set that to a 3-column grid for simplicity. It crops the images to be in uniform dimensions.

Lastly, I added a function to download the mosaic with a custom filename. I figured a point-and-click function would be easier on users than if you let them right-click the mosaic output, write a filename, then save that. It is set to export to wherever your browser has its default folder for downloads -- typically the Downloads folder.

And that's the app! Give it a spin by visiting https://mosaicmaker.streamlit.app or by clicking this button:

[![Open in Streamlit](https://img.shields.io/badge/Open%20in-Streamlit-brightgreen)](https://mosaicmaker.streamlit.app/)

I want to give a shoutout to deepankarvarma who made an Image Collage app using Python. It was a great reference for me to build my app (and also a good source for the sick background image of the app!). Streamlit documentation was also extremely helpful in building this app, from how to initialize a session to uploading files and more. I also want to give credits to Copilot for helping me troubleshoot the test script.

This app was created to complete https://cs50.harvard.edu/python/2022/project/ but I hope that this is also useful for you and your grid-making needs. For instance, a resolution or vision board for the coming new year. Happy Mosaic-ing!
# docker-python-watermark
## Watermark images with Python via Docker

Text appears at a 45 degrees angle overlayed on an image

---

To use app:

1. Pull Docker image from [reverie89/python-watermark](https://hub.docker.com/r/reverie89/python-watermark) OR build from Dockerfile from this repo
2. Put image files (.png or .jpg) into `input` directory
3. Put font file (.ttf) into `input` directory
4. Edit .env as applicable for the text, font, color (R, G, B, Alpha), output extension
5. Run the following:
```
docker run
--rm
--env-file .env
-v ./input:/input
-v ./output:/output
reverie89/python-watermark
```
1. Find the watermarked images in `output` directory

---

Docker container was built with Python 3.11 and uses the Pillow ~=9.0 package
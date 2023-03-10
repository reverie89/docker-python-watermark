# docker-python-watermark
## Watermark images with Python via Docker

Text appears at a 45 degrees angle overlayed on an image

Edit .env as applicable for the text, font and color (R, G, B, A)

Insert .ttf font into same directory as .env file

---

To use app:

1. Pull Docker image from [reverie89/python-watermark](https://hub.docker.com/r/reverie89/python-watermark) OR build from Dockerfile from this repo,
2. Put image files (.png or .jpg) into `input` directory
3. Run the following:
```docker run --rm --env-file $(pwd)/app/.env -v $(pwd)/app:/app watermark```
4. Find the watermarked images in `output` directory

---

Docker container was built with Python 3.11 and uses the Pillow ~=9.0 package
# python modules
import os, datetime
from PIL import Image, ImageFont, ImageDraw

os.chdir("/app")

# variables
inputDir = os.getcwd() + "/input/"
outputDir = os.getcwd() + "/output/"

try:
	os.makedirs(outputDir)
	outputResult = open(outputDir + "/result.txt", "a")
except FileExistsError:
	pass

outputResult = open(outputDir + "/result.txt", "a")

watermark_text = os.getenv("WATERMARK_TEXT")
watermark_color = tuple(map(int, os.getenv("WATERMARK_COLOR").split(", ")))
fontfamily = os.getenv("FONT_FAMILY")


class Watermark:
	def __init__(self, inputFile, ext, inputDir, outputDir):
		self.inputFile = inputFile
		self.ext = ext
		self.inputDir = inputDir
		self.outputDir = outputDir

	def text(self, watermark_text, fontfamily):
		self.watermark_text = watermark_text
		self.fontfamily = fontfamily
		
		image = Image.open(self.inputDir + self.inputFile).convert("RGBA")
		image_w, image_h = image.size
		if image_w >= image_h:
			fontsize = int(image_w / 10)
		else:
			fontsize = int(image_h / 10)
		font = ImageFont.truetype(self.fontfamily, fontsize)
		# watermark text
		left, top, right, bottom = font.getbbox(watermark_text)
		width, height = right - left, (bottom - top)*2
		text_image = Image.new(mode="RGBA", size=(width, height), color=(255, 255, 255, 0))

		draw = ImageDraw.Draw(text_image)
		draw.text(xy=(0, 0), text=self.watermark_text, fill=watermark_color, font=font)
		rotate_watermark = text_image.rotate(45, expand=True, fillcolor=(0, 0, 0, 0))
		rotate_x = (image.size[0] - rotate_watermark.size[0])//2
		rotate_y = (image.size[1] - rotate_watermark.size[1])//2
		# watermark image onto original image
		watermark_image = Image.new(mode="RGBA", size=image.size, color=(255, 255, 255, 0))
		watermark_image.paste(rotate_watermark, (rotate_x, rotate_y))
		combined_image = Image.alpha_composite(image, watermark_image)
		try:
			combined_image.save(self.outputDir + self.inputFile, self.ext)
			return True
		except Exception as e:
			print(e)
			return False

for	filename in os.listdir(inputDir):
	match filename[-4:].lower():
		case ".png":
			process = Watermark(inputFile=filename, ext="PNG", inputDir=inputDir, outputDir=outputDir)
			if process.text(watermark_text=watermark_text, fontfamily=fontfamily):
				result = "%s %s %s %s" % (datetime.datetime.now(), "-", filename, "- OK\n")
			else:
				result = "%s %s %s %s" % (datetime.datetime.now(), "-", filename, "- NO\n")
			outputResult.write(result)
			print(result)
		case ".jpg":
			process = Watermark(inputFile=filename, ext="JPG", inputDir=inputDir, outputDir=outputDir)
			if process.text(watermark_text=watermark_text, fontfamily=fontfamily):
				result = "%s %s %s %s" % (datetime.datetime.now(), "-", filename, "- OK\n")
			else:
				result = "%s %s %s %s" % (datetime.datetime.now(), "-", filename, "- NO\n")
			outputResult.write(result)
			print(result)
	pass

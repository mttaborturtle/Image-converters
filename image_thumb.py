from PIL import Image
import glob
import os

# Set prefered output size
size = 64, 64

# Convert all files to desired size
for infile in glob.glob("*.jpg"):
    file, ext = os.path.splitext(infile)
    im = Image.open(infile)
    im.thumbnail(size)
    im.save(file + "-thumb.jpg", "JPEG")

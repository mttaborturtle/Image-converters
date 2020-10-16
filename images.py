from PIL import Image, ImageFilter

# Convert an image to B+W then show the new image
# To change options or add filters see PIL docs
img = Image.open('PATH/TO/IMAGE/FILE')

# Converts to B+W
filtered_img = img.convert('L')

# Outputs new file and opens the image to view
filtered_img.save('PATH/TO/DESIRED/OUTPUT/FILENAME.png', 'png')
filtered_img.show()

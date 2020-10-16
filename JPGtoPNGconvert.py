import sys
import os
from PIL import Image

# Take in the image folder/image and the dest folder
# from the command line
image_folder = sys.argv[1]
dest_folder = sys.argv[2]


# Check to see if the destination folder already
# exists and create it if it does not
try:
    if os.path.isdir(dest_folder) == False:
        os.mkdir(dest_folder)
        print('Sucessfully created folder ' + dest_folder)
    else:
        print('Your intended dir already exists')
except OSError:
    print("Creation of the directory %s failed" % dest_folder)


# Convert all images in folder from JPG to PNG
image_folder_dir = os.listdir(image_folder)
for filename in image_folder_dir:
    if filename.endswith('.jpg'):
        img = Image.open(f'{image_folder}{filename}')
        clean_name = os.path.splitext(filename)[0]
        img.save(f'{dest_folder}{clean_name}.png', 'png')
        print(f'converted {filename} and saved it to: {dest_folder}')
    else:
        continue
print('Image Conversion Complete!')

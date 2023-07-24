#image processing
#--------------------------------------------
# import cv2
from PIL import Image
#--------------------------------------------

#--------------------------------------------
#step 1 crop link
def CropImage(path,fileName):
    img = Image.open(path)
    width, height = img.size
    img_cropped = img.crop((0, 0, width, height-6))
    img_cropped.save(f'test/croped/{fileName}')
#--------------------------------------------



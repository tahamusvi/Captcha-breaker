#image processing
#--------------------------------------------
import cv2
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
#step 2 gray image
def GrayImage(path,fileName):
    img = cv2.imread(path)
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imwrite(f'test/grayed/{fileName}', gray_img)

#--------------------------------------------
def MedianImage(path,fileName):
    img = cv2.imread(path)
    median_img = cv2.medianBlur(img, 3)
    cv2.imwrite(f'test/median/{fileName}', median_img)
#--------------------------------------------
def GaussianBlur(path,fileName):
    img = cv2.imread(path)
    gaussian_img = cv2.GaussianBlur(img, (3, 3), 0)
    cv2.imwrite(f'test/gaussian/{fileName}', gaussian_img)
#--------------------------------------------
#step 3 dilate
def dilateImage(path,fileName):
    img = cv2.imread(path)
    max_img = cv2.dilate(img, None, iterations=1)
    cv2.imwrite(f'test/dilate/{fileName}', max_img)
#--------------------------------------------
def TImage(path, fileName):
    img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    color_mapped_img = cv2.applyColorMap(img, cv2.COLORMAP_HOT)
    cv2.imwrite(f'test/Tempature/{fileName}', color_mapped_img)
#--------------------------------------------
def BinaryImage(path, fileName):
    img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    ret, thresh_img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
    cv2.imwrite(f'test/final/{fileName}', thresh_img)
#--------------------------------------------
#image processing
#--------------------------------------------
import cv2
from PIL import Image
#--------------------------------------------

#--------------------------------------------
#step 1 crop link
def CropImage(path,fileName,final_path):
    img = Image.open(path)
    width, height = img.size
    img_cropped = img.crop((0, 0, width, height-6))
    img_cropped.save(f'{final_path}{fileName}')
#--------------------------------------------
#step 2 gray image
def GrayImage(path,fileName,final_path):
    img = cv2.imread(path)
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imwrite(f'{final_path}{fileName}', gray_img)

#--------------------------------------------
def MedianImage(path,fileName,final_path):
    img = cv2.imread(path)
    median_img = cv2.medianBlur(img, 3)
    median_img = cv2.medianBlur(median_img, 3)
    median_img = cv2.medianBlur(median_img, 3)
    cv2.imwrite(f'{final_path}{fileName}', median_img)
#--------------------------------------------
def GaussianBlur(path,fileName,final_path):
    img = cv2.imread(path)
    gaussian_img = cv2.GaussianBlur(img, (3, 3), 0)
    cv2.imwrite(f'{final_path}{fileName}', gaussian_img)
#--------------------------------------------
#step 3 dilate
def dilateImage(path,fileName,final_path):
    img = cv2.imread(path)
    max_img = cv2.dilate(img, None, iterations=1)
    cv2.imwrite(f'{final_path}{fileName}', max_img)
#--------------------------------------------
def TImage(path, fileName,final_path):
    img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    color_mapped_img = cv2.applyColorMap(img, cv2.COLORMAP_HOT)
    cv2.imwrite(f'{final_path}{fileName}', color_mapped_img)
#--------------------------------------------
def BinaryImage(path, fileName,final_path):
    img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    ret, thresh_img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
    cv2.imwrite(f'{final_path}{fileName}', thresh_img)
#--------------------------------------------
import numpy as np
def threshImage(path, fileName,final_path):
    img = cv2.imread(path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    kernel = np.ones((3, 3), np.uint8)
    opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=1)
    cv2.imwrite(f'{final_path}{fileName}', opening)
#--------------------------------------------
def InvertImage(path,fileName,final_path):
    img = cv2.imread(path)
    thresh = cv2.bitwise_not(img)
    cv2.imwrite(f'{final_path}{fileName}', thresh)
#--------------------------------------------
import cv2

def convert_to_binary(path,fileName,final_path):
    # Load the image in grayscale
    img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)

    # Apply binary thresholding to the image
    ret, thresh_img = cv2.threshold(img, 10, 200, cv2.THRESH_BINARY)

    # Save the binary image to the output path
    cv2.imwrite(f'{final_path}{fileName}', thresh_img)
#------------------------------------------
def cut_image(path,fileName,final_path):
    img = cv2.imread(path)
    height, width = img.shape[:2]

    # cut from the left and then right
    flag = False
    left_row = 0
    right_row = 0
    for i in range(2):
        for x in range(width):
            for y in range(height):
                if i == 0:
                    pxl = img[x,y]
                else:
                    pxl = img[-x-1, y]
                if all(pxl != [0,0,0]):
                    flag = True
                    break

            if flag:
                break

            else:
                if i == 0:
                    left_row = x
                else:
                    right_row = x

    img = Image.open(path)
    img_cropped = img.crop((left_row, 0, width - right_row, height))
    img_cropped.save(f'{final_path}{fileName}')
#------------------------------------------
def separate_image(path,fileName,final_path):
    img = cv2.imread(path)
    height, width = img.shape[:2]
    img_rows = []
    for x in range(width):
        c_row = 0
        for y in range(height):
            pxl = img[x, y]
            c_row += sum(pxl)
        img_rows.append(c_row)

    already_used = []
    for i, index in enumerate(img_rows):
        if i == min(img_rows)
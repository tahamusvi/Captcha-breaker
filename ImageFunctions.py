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
    # height, width = img.shape[:2]
    img2 = Image.open(path)
    width, height = img2.size

    # cut from the left and then right
    flag = False
    left_row = 0
    right_row = 0

    for x in range(width):
        for y in range(height):
            pxl = img[y,x]
            if all(pxl != [0,0,0]):
                flag = True
                break

        if flag:
            break

        else:
            left_row = x

    flag = False
    # print(width)
    for x in range(0,width):
        for y in range(height):
            pxl = img[y,-x-1]
            if all(pxl != [0,0,0]):
                flag = True
                break

        if flag:
            break

        else:
            right_row = x

    # img = Image.open(path)
    # print(right_row)
    # print(left_row)

    img_cropped = img2.crop((left_row, 0, width - right_row, height))
    img_cropped.save(f'{final_path}/{fileName}')

#------------------------------------------
def rotate_image(path,fileName,final_path,degree):
    # خواندن تصویر
    img2 = Image.open(path)
    
    if(degree):
        rotated_image = img2.transpose(Image.ROTATE_90).transpose(Image.FLIP_LEFT_RIGHT)
    else:
        rotated_image = img2.transpose(Image.ROTATE_270).transpose(Image.FLIP_LEFT_RIGHT)
    
    rotated_image.save(f'{final_path}/{fileName}')
#------------------------------------------
def separate_image(path,fileName,final_path,name=None):
    img = cv2.imread(path)
    img2 = Image.open(path)
    width, height = img2.size
    img_rows = []
    for x in range(width):
        c_row = 0
        for y in range(height):
            pxl = img[y, x]
            c_row += sum(pxl)
        img_rows.append(c_row)

    def sort_image():
        sorted_img_rows = sorted(img_rows)
        img_rows_reformatted = []
        for i, index in enumerate(img_rows):
            img_rows_reformatted.append([index, i])
        sorted_img_rows = sorted(img_rows_reformatted)
        return sorted_img_rows

    already_used = []
    target_row = []
    sorted_img_rows = sort_image()

    for i in sorted_img_rows[5:-5]:
        if i[1] not in already_used:
            target_row.append(i[1])
            for j in range(17):
                try:
                    already_used.append(i[1] + j - 8)
                except:
                    pass
        if len(target_row) == 4:
            break

    target_row = sorted(target_row)
    img_cropped = []
    img_cropped.append(img2.crop((0, 0, target_row[0], height)))
    for i in range(3):
        img_cropped.append(img2.crop((target_row[i], 0, target_row[i + 1], height)))
    img_cropped.append(img2.crop((target_row[3], 0, width, height)))
    if(name):
        

        for i in range(5):
            print(name[i])
            try:
                img_cropped[i].save(f'{final_path}{name[i]}.png')
            except:
                pass
    else:
        for i in range(5):
            try:
                img_cropped[i].save(f'{final_path}{i}{fileName}')
                cut_image(f'{final_path}{i}{fileName}',f"{i}{fileName}",f'{final_path}')
                rotate_image(f'{final_path}{i}{fileName}',f"{i}{fileName}",f'{final_path}',True)
                cut_image(f'{final_path}{i}{fileName}',f"{i}{fileName}",f'{final_path}')
                rotate_image(f'{final_path}{i}{fileName}',f"{i}{fileName}",f'{final_path}',True)
            except:
                pass



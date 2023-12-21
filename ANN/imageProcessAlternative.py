from ImageFunctions import *
import os
import os.path
import cv2
import glob
import imutils

# --------------------------------------------


def respy(file_path, file_name, path):
    output = f"{path}output/"
    img = cv2.imread(file_path)
    img2 = Image.open(file_path)

    # CropImage(file_path,file_name,output)
    img = GrayImage(img)

    file_path = f"{output}{file_name}"

    img = dilateImage(img)
    img = InvertImage(img)
    img = cut_image_R(img, img2)
    img = TImage(img)
    img = convert_to_binary(img)
    save_image_cv2(img, file_path)
    # cut_image(file_path,file_name,path)
    # separate_image(file_path,file_name,sep)

# --------------------------------------------


def respy2(file_path, file_name, path):

    img = cv2.imread(file_path)
    # img2 = Image.open(file_path)
    file_path = f"{path}output/{file_name}"

    gray_img = GrayImage(img)

    # blur_image = cv2.blur(gray_img, (4, 4))
    blur_image = simple_blur(gray_img)
    # cv2.GaussianBlur(blur_image, (0, 0), 6)
    gblur_img = GaussianBlur(blur_image)
    # cv2.addWeighted(gray_img, 1.80, gblur_img, -0.60, 0)
    sharp_img = sharping(gray_img, gblur_img)
    sharp_not_img = bitwise_not(sharp_img)  # cv2.bitwise_not(sharp_img)
    # cv2.threshold(sharp_not_img, 20, 255, cv2.THRESH_BINARY)
    img_zeroone = convert_to_binary2(sharp_not_img)

    cl_img = clear_img(img_zeroone)
    removed_white_pixel = remove_white_pixel(cl_img)

    save_image_cv2(removed_white_pixel, file_path)

    cut_image(file_path, file_name, f"{path}output/")
    separate_image_alternative(file_path, file_name, f"{path}outputc/")
    # add_black_border(file_path,file_name,f"{path}outputc/",5)


# --------------------------------------------
path = "test/ts2/"
sep = f"{path}sep/"

for i in range(1, 2):
    current_path = f"{path}{i}/"

    for file_name in os.listdir(current_path):
        if(file_name == "output" or file_name == "outputc" or file_name == "croped"):
            # print(file_name)
            continue
        file_path = os.path.join(current_path, file_name)
        CropImage(file_path, file_name, f"{current_path}croped/")

    for file_name in os.listdir(f"{current_path}croped/"):
        file_path = os.path.join(f"{current_path}croped/", file_name)
        respy2(file_path, file_name, current_path)

    for file_name in os.listdir(f"{current_path}outputc/"):
        file_path = os.path.join(f"{current_path}outputc/", file_name)
        add_black_border(file_path, file_name, f"{current_path}outputc", 5)

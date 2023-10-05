from ImageFunctions import *
import os
from matplotlib import pyplot as plt
#--------------------------------------------
# def count_files(folder_path):
#     file_count = 0

#     for filename in os.listdir(folder_path):
#         if os.path.isfile(os.path.join(folder_path, filename)):
#             file_count += 1

#     return file_count
#--------------------------------------------
# path = "test/"

# for file_name in os.listdir(path):

#     if(file_name == 'croped'):
#         continue

#     file_path = os.path.join(path, file_name)
#     # print(file_path)
#     CropImage(file_path,file_name)
#--------------------------------------------
# path = "test/croped/"

# for file_name in os.listdir(path):

#     if(file_name == 'grayed'):
#         continue

#     file_path = os.path.join(path, file_name)
#     GrayImage(file_path,file_name)
#--------------------------------------------
# path = "test/grayed/"

# for file_name in os.listdir(path):

#     file_path = os.path.join(path, file_name)
#     MedianImage(file_path,file_name)
#     GaussianBlur(file_path,file_name)
#     dilateImage(file_path,file_name)
#--------------------------------------------
# path = "test/dilate/"

# for file_name in os.listdir(path):

#     file_path = os.path.join(path, file_name)
#     TImage(file_path,file_name)
#--------------------------------------------
# path = "test/dilate3/"

# for file_name in os.listdir(path):

#     file_path = os.path.join(path, file_name)
#     convert_to_binary(file_path,file_name,"test/final/")

#--------------------------------------------
def respy(file_path,file_name,path):
    output = f"{path}output/"
    img = cv2.imread(file_path)
    img2 = Image.open(file_path)

    # CropImage(file_path,file_name,output)
    img = GrayImage(img)
    
    file_path = f"{output}{file_name}"

    img = dilateImage(img)
    img = InvertImage(img)
    img = cut_image_R(img,img2)
    img = TImage(img)
    img = convert_to_binary(img)
    save_image_cv2(img,file_path)
    # cut_image(file_path,file_name,path)
    # separate_image(file_path,file_name,sep)

#--------------------------------------------
def respy2(file_path,file_name,path):

    img = cv2.imread(file_path)
    # img2 = Image.open(file_path)
    file_path = f"{path}output/{file_name}"

    gray_img = GrayImage(img)  
    
    blur_image = simple_blur(gray_img) #blur_image = cv2.blur(gray_img, (4, 4))
    gblur_img = GaussianBlur(blur_image) #cv2.GaussianBlur(blur_image, (0, 0), 6)
    sharp_img = sharping(gray_img,gblur_img) #cv2.addWeighted(gray_img, 1.80, gblur_img, -0.60, 0)
    sharp_not_img = bitwise_not(sharp_img) #cv2.bitwise_not(sharp_img)
    img_zeroone = convert_to_binary2(sharp_not_img) #cv2.threshold(sharp_not_img, 20, 255, cv2.THRESH_BINARY)
    
    cl_img = clear_img(img_zeroone)
    removed_white_pixel = remove_white_pixel(cl_img)
    

    save_image_cv2(removed_white_pixel,file_path)

    cut_image(file_path,file_name,f"{path}output/")
    separate_image(file_path,file_name,f"{path}outputc/")
    # add_black_border(file_path,file_name,f"{path}outputc/",5)

#--------------------------------------------
path = "test/ts2/"
sep = f"{path}sep/"

for i in range(1,2):
    current_path = f"{path}{i}/"

    for file_name in os.listdir(current_path):
        if(file_name == "output" or file_name ==  "outputc" or file_name ==  "croped"):
            # print(file_name)
            continue
        file_path = os.path.join(current_path, file_name)
        CropImage(file_path,file_name,f"{current_path}croped/")

    for file_name in os.listdir(f"{current_path}croped/"):
        file_path = os.path.join(f"{current_path}croped/", file_name)
        respy2(file_path,file_name,current_path)
    
    for file_name in os.listdir(f"{current_path}outputc/"):
        file_path = os.path.join(f"{current_path}outputc/", file_name)
        add_black_border(file_path,file_name,f"{current_path}outputc",5)
        


    
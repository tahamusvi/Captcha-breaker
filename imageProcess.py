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

    # CropImage(file_path,file_name,output)
    GrayImage(file_path,file_name,output)
    
    file_path = f"{output}{file_name}"

    
    dilateImage(file_path,file_name,output)
    InvertImage(file_path,file_name,output)
    cut_image(file_path,file_name,output)
    TImage(file_path,file_name,output)
    convert_to_binary(file_path,file_name,output)
    # cut_image(file_path,file_name,path)
    # separate_image(file_path,file_name,sep)
#--------------------------------------------
def respy2(file_path,path):
    output = f"{path}output2/"
    im = cv2.imread(file_path)
    sim = sharp_img(im)
    cl_img = clear_img(sim)
    cv2.imwrite(f'{output}{file_name}', cl_img)

#--------------------------------------------
path = "test/ts2/"
sep = f"{path}sep/"

for i in range(1,2):
    current_path = f"{path}{i}/"

    for file_name in os.listdir(current_path):
        if(file_name == "output" or file_name ==  "output2" or file_name ==  "croped"):
            print(file_name)
            continue
        file_path = os.path.join(current_path, file_name)
        CropImage(file_path,file_name,f"{current_path}croped/")
    for file_name in os.listdir(f"{current_path}croped/"):
        file_path = os.path.join(f"{current_path}croped/", file_name)
        respy(file_path,file_name,current_path)
        respy2(file_path,current_path)




        


    
    # CropImage(file_path,file_name,path)


    
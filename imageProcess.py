from ImageFunctions import *
import os
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
path = "test/ts2/"
pathf = path + "s/"


for file_name in os.listdir(path):

    file_path = os.path.join(path, file_name)

    
    # CropImage(file_path,file_name,path)


    CropImage(file_path,file_name,pathf)
    GrayImage(file_path,file_name,pathf)
    dilateImage(file_path,file_name,pathf)
    InvertImage(file_path,file_name,pathf)
    cut_image(file_path,file_name,pathf)
    TImage(file_path,file_name,pathf)
    convert_to_binary(file_path,file_name,pathf)
    cut_image(file_path,file_name,pathf)
    separate_image(file_path,file_name,pathf)
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
def respy(file_path,file_name,path):
    sep = f"{path}sep/"
    # CropImage(file_path,file_name,path)
    # GrayImage(file_path,file_name,path)
    # dilateImage(file_path,file_name,path)
    # InvertImage(file_path,file_name,path)
    # cut_image(file_path,file_name,path)
    # TImage(file_path,file_name,path)
    # convert_to_binary(file_path,file_name,path)
    # cut_image(file_path,file_name,path)
    separate_image(file_path,file_name,sep)
    
#--------------------------------------------
path = "test/ts2/"
sep = f"{path}sep/"

for i in range(35,36):
    current_path = f"{path}{i}/"

    for file_name in os.listdir(current_path):
        if(file_name == "sep"):
            continue
        file_path = os.path.join(current_path, file_name)
        respy(file_path,file_name,current_path)

    


    
    # CropImage(file_path,file_name,path)


    
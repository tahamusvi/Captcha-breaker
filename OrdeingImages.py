from ImageFunctions import *
import os
#--------------------------------------------
def respy(file_path,file_name,path):
    CropImage(file_path,file_name,path)


    new_file_path = f"{path}{file_name}"

    GrayImage(new_file_path,file_name,path)
    dilateImage(new_file_path,file_name,path)
    InvertImage(new_file_path,file_name,path)
    cut_image(new_file_path,file_name,path)
    TImage(new_file_path,file_name,path)
    convert_to_binary(new_file_path,file_name,path)
    cut_image(new_file_path,file_name,path)
    separate_image(new_file_path,file_name,path)
#--------------------------------------------
def respy2(file_path,file_name,path):
    CropImage(file_path,file_name,path)

    # InvertImage(file_path,file_name,path)
    # cut_image(file_path,file_name,path)
    new_file_path = f"{path}{file_name}"
    MedianImage(new_file_path,file_name,path)
    MedianImage(new_file_path,file_name,path)

    dilateImage(new_file_path,file_name,path)
    # TImage(new_file_path,file_name,path)
    convert_to_binary(new_file_path,file_name,path)
    separate_image(new_file_path,file_name,path,f"1{file_name}")    
#--------------------------------------------
path = "dataset/"
sep = f"{path}sep/"

for i in range(35,36):
    current_path = f"{path}captcha/"

    for file_name in os.listdir(current_path):
        print(file_name)
        
        file_path = os.path.join(current_path, file_name)
        respy2(file_path,file_name,f"{path}after/")






    
    # CropImage(file_path,file_name,path)
#--------------------------------------------




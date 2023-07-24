from ImageFunctions import CropImage
import os
#--------------------------------------------
# def count_files(folder_path):
#     file_count = 0

#     for filename in os.listdir(folder_path):
#         if os.path.isfile(os.path.join(folder_path, filename)):
#             file_count += 1

#     return file_count
#--------------------------------------------
path = "test/"

for file_name in os.listdir(path):

    if(file_name == "croped"):
        continue

    file_path = os.path.join(path, file_name)
    # print(file_path)
    CropImage(file_path,file_name)

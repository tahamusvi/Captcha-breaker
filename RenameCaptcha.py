
import os
import random
import string
characters = string.ascii_letters + string.digits
#--------------------------------------------
def change_name(alphabet,path):
    count = 1
    path_complete = path + alphabet

    for file_name in os.listdir(path_complete):
        random_string = ''.join(random.choice(characters) for _ in range(4))
        file_path = os.path.join(path_complete, file_name)
        os.rename(file_path, f'{path_complete}/{random_string}.png')

    for file_name in os.listdir(path_complete):
        file_path = os.path.join(path_complete, file_name)
        os.rename(file_path, f'{path_complete}/{alphabet}-{count}.png')
        count += 1
#--------------------------------------------
# make folders
# a --> 97
# A --> 65
# 0 --> 48
#------------------------
# start = 97
# folder = "trainData/Low"
# # os.makedirs(folder)
# for i in range(26):
#     os.makedirs(f"{folder}/{chr(start+i)}")
# #------------------------
# start = 65
# folder = "trainData/Capital"
# # os.makedirs(folder)
# for i in range(26):
#     os.makedirs(f"{folder}/{chr(start+i)}")
# #------------------------
# start = 48
# folder = "trainData/Numbers"
# # os.makedirs(folder)
# for i in range(26):
#     os.makedirs(f"{folder}/{chr(start+i)}")
#--------------------------------------------
path = "trainData/low/"
start = 97
for i in range(26):
    change_name(f"{chr(i+start)}",path)

# start = 48 
# for i in range(10):
#     change_name(f"{chr(i+start)}",path)





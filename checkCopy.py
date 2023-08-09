from PIL import Image
import numpy as np
import os
#--------------------------------------------
def compare_images(image1_path, image2_path):
    image1 = Image.open(image1_path)
    image2 = Image.open(image2_path)

    if image1.size != image2.size:
        return False

    image1_array = np.array(image1)
    image2_array = np.array(image2)

    return np.array_equal(image1_array, image2_array)
#--------------------------------------------

#--------------------------------------------
path = "check/"

for file_name in os.listdir(path):

    file_path = os.path.join(path, file_name)
    for file_name2 in os.listdir(path):
        file_path2 = os.path.join(path, file_name2)
        if((file_path != file_path2) and (compare_images(file_path,file_path2))):
            os.remove(file_path)
        
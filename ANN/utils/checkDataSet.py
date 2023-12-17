import os

def UpdateDataset():
    dataset = {
    "not_find" : 0,
    "error" : 0,
    }

    folders = [f for f in os.listdir("dataset") if os.path.isdir(os.path.join("dataset", f))]

    for folder in folders:
        if(not folder in dataset):
            dataset[folder] = len(os.listdir(os.path.join("dataset", folder)))


    return dataset
#--------------------------------------------------------------------------------------
def delete_files_in_folders():
    folders = [f for f in os.listdir("dataset") if os.path.isdir(os.path.join("dataset", f))]

    for folder in folders:
        folder_path = os.path.join("dataset", folder)
        for file_name in os.listdir(folder_path):
            file_path = os.path.join(folder_path, file_name)
            if os.path.isfile(file_path):
                os.remove(file_path)

    print("all files deleted!")
#--------------------------------------------------------------------------------------
def printDataSet():
    dataset = UpdateDataset()
    for key in dataset:
        print(f"{key}: {dataset[key]}")
#--------------------------------------------------------------------------------------
delete_files_in_folders()
printDataSet()
# print(UpdateDataset())
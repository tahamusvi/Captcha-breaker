import requests # request img from web
import shutil # save img locally
import time
import os
#--------------------------------------------
url = 'https://golestan.iust.ac.ir/Forms/AuthenticateUser/captcha.aspx'

#--------------------------------------------
for j in range(5,20):

    folder_name = f"captcha/captcha({j})"
    if not os.path.exists(folder_name):
        os.mkdir(folder_name)

    for i in range(0,100):

        
    
        file_name = f"captcha/captcha({j})/{i}.png"
        res = requests.get(url, stream = True)
        if res.status_code == 200:
            with open(file_name,'wb') as f:
                shutil.copyfileobj(res.raw, f) 
            print('Image sucessfully Downloaded: ',file_name)
        else:
            print('Image Couldn\'t be retrieved')
        time.sleep(3) 
#--------------------------------------------












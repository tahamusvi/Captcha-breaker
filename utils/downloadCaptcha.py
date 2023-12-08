import requests # request img from web
import shutil # save img locally
"""
We use this code to download Golestan Captchas from various university websites.
 The reason for the large number of universities is to avoid being blocked by their servers.
"""
#--------------------------------------------
links = {
    "sutech" : "https://golestan.sutech.ac.ir/",
    "iust" : "https://golestan.iust.ac.ir/",
    "yazd" : "https://golestan.yazd.ac.ir/",
    "qom" : "https://edu.qom.ac.ir/",
    # "ui" : "https://golestan.ui.ac.ir/",
    "znu" : "https://golestan.znu.ac.ir/",
    "sbu" : "https://golestan.sbu.ac.ir/",
    "modares" : "https://golestan.modares.ac.ir/",
    "usc" : "https://edu.usc.ac.ir/",
    "iut" : "https://golestan.iut.ac.ir/",
    "umz" : "https://golestan.umz.ac.ir/",
    "uok" : "https://golestan.uok.ac.ir/",
    "lu" : "https://golestan.lu.ac.ir/",
    "nit" : "https://golestan.nit.ac.ir/",
    "uma" : "https://golestan.uma.ac.ir/",
    "atu" : "https://ems.atu.ac.ir/",
} 

slice = f"Forms/AuthenticateUser/captcha.aspx"

#--------------------------------------------
number = int(input("how many captcha needed ? "))
for i in range(0,number):
    nameUni = list(links.keys())[i%len(links)]

    file_name = f"captcha/{i}-{nameUni}.png"

    url = f"{links[nameUni]}{slice}"

    res = requests.get(url, stream = True)
    if res.status_code == 200:
        with open(file_name,'wb') as f:
            shutil.copyfileobj(res.raw, f) 
        # print('Image sucessfully Downloaded: ',file_name)
#--------------------------------------------













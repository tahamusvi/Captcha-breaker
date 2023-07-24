import requests # request img from web
import shutil # save img locally
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
for i in range(0,2000):
    nameUni = list(links.keys())[i%15]

    file_name = f"captcha/test3/{i}-{nameUni}.png"

    url = f"{links[nameUni]}{slice}"

    res = requests.get(url, stream = True)
    if res.status_code == 200:
        with open(file_name,'wb') as f:
            shutil.copyfileobj(res.raw, f) 
        # print('Image sucessfully Downloaded: ',file_name)
#--------------------------------------------













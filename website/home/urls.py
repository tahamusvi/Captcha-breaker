from .views import *
from django.urls import path



app_name = 'captcha'

urlpatterns = [
    path('', home,name="home"),
    path('answering/', answering,name="answering"),
    path('upload/',process_captchas,name="upload"),
    path('download/',download_captchas,name="download"),
]

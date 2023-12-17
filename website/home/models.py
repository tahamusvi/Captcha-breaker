from distutils.command.upload import upload
from django.db import models



class captcha(models.Model):
    answer = models.CharField(max_length=5,null=True,blank=True)
    answered = models.BooleanField(default=False)
    image = models.ImageField(upload_to='data/captchas/')



    def __str__(self):
        return f"{self.id}-{self.answer}"

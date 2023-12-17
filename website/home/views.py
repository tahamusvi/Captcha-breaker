from django.shortcuts import render,redirect
from .models import captcha
import random
from .forms import CaptchaForm

def home(request):
    caps = captcha.objects.filter(answered = False)
    ans = captcha.objects.filter(answered = True).count()
    all = caps.count() + ans



    

    return render(request,'home/home.html',{'all':all,'ans':ans})




def answering(request):
    if(request.method == 'POST'):
        id = request.POST.get('id')
        answer = request.POST.get('answer')

        print(request.POST)
        cap = captcha.objects.get(id = id)
        cap.answer = answer
        cap.answered = True
        cap.save()

        return redirect("captcha:home")

    else:
        caps = captcha.objects.filter(answered = False)
        random_caps = random.choice(caps) 
        return render(request,'home/answering.html',{"captcha":random_caps,"form":CaptchaForm()}) 



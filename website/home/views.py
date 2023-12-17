from django.shortcuts import render,redirect
from .models import captcha
import random
from .forms import CaptchaForm
import zipfile
from django.core.files import File
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import zipfile
from django.http import HttpResponse
import os 
#-----------------------------------------------
def home(request):
    caps = captcha.objects.filter(answered = False)
    ans = captcha.objects.filter(answered = True).count()
    all = caps.count() + ans

    return render(request,'home/home.html',{'all':all,'ans':ans})
#-----------------------------------------------
def answering(request):
    if(request.method == 'POST'):
        id = request.POST.get('id')
        answer = request.POST.get('answer')

        cap = captcha.objects.get(id = id)
        cap.answer = answer
        cap.answered = True
        cap.save()

        return redirect("captcha:home")

    else:
        caps = captcha.objects.filter(answered = False)
        random_caps = random.choice(caps) 
        return render(request,'home/answering.html',{"captcha":random_caps,"form":CaptchaForm()}) 
#-----------------------------------------------
from io import BytesIO

@csrf_exempt
def process_captchas(request):
    if request.method == 'POST':
        # Assuming the zip file is sent as a file in the request
        zip_file = request.FILES.get('captchas_zip')

        if zip_file:
            try:
                # Try opening the zip file directly
                with zipfile.ZipFile(zip_file, 'r') as z:
                    process_zip_files(z)
            except AttributeError:
                # Handle if zip_file is of type 'bytes'
                zip_io = BytesIO(zip_file)
                with zipfile.ZipFile(zip_io, 'r') as z:
                    process_zip_files(z)

            return JsonResponse({'message': 'Captchas processed successfully'})
        else:
            return JsonResponse({'error': 'No zip file provided'}, status=400)

    else:
        return render(request, 'home/upload.html')
#-----------------------------------------------
def process_zip_files(zip_file):
    for file_name in zip_file.namelist():
        file_content = zip_file.read(file_name)

        new_captcha = captcha()
        new_captcha.image.save(file_name, File(BytesIO(file_content)))
        new_captcha.save()
#-----------------------------------------------


def download_captchas(request):
    # Get the captchas that have been answered
    answered_captchas = captcha.objects.filter(answered=True)

    if answered_captchas:
        # Create an in-memory ZIP file
        in_memory_zip = BytesIO()

        # Create a ZIP file object
        with zipfile.ZipFile(in_memory_zip, 'w') as zf:
            # Add each answered captcha to the ZIP file
            for captcha_obj in answered_captchas:
                # Get the image file path
                image_path = captcha_obj.image.path

                # Add the image file to the ZIP file
                zf.write(image_path, f"{captcha_obj.answer}.png")

        # Set the appropriate content type for ZIP file
        response = HttpResponse(content_type='application/zip')

        # Set the content-disposition to trigger a download
        response['Content-Disposition'] = 'attachment; filename="answered_captchas.zip"'

        # Write the ZIP file to the response
        response.write(in_memory_zip.getvalue())

        # Return the response
        return response

    else:
        return JsonResponse({'error': 'No answered captchas found'}, status=400)
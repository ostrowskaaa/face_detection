import os
from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from .forms import ImageUploadForm
#from .forms import GalleryForm
from .dface import dface
#from .dface import gallery
from cv2 import cv2

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def detection(request):
    form = ImageUploadForm(request.POST, request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            post = form.save(commit=False)
            post.save()

            imageURL = settings.MEDIA_URL + form.instance.document.name
            dface(settings.MEDIA_ROOT_URL + imageURL)

            return render(request, 'detection.html', {'form':form, 'post':post})
    else:
        form = ImageUploadForm()
    return render(request, 'detection.html',{'form':form})

def gallery(request):
    imageURL = settings.MEDIA_ROOT_URL + settings.MEDIA_URL + 'documents/'
    img_list = os.listdir(imageURL)
    for file in img_list:

        img = cv2.imread(imageURL+file, 1)
       # cv2.imwrite(imageURL+file, img)
    return render(request, "gallery.html", {'documents': img_list})
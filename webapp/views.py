from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from .forms import UploadImageForm
from .forms import ImageUploadForm
from .dface import dface

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def upload(request):
    form = UploadImageForm(request.POST, request.FILES)
    if form.is_valid():
        myfile = request.FILES['image']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'upload.html', {'form': form, 'uploaded_file_url': uploaded_file_url})
    else:
        form = UploadImageForm()
        return render(request, 'upload.html', {'form': form})

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
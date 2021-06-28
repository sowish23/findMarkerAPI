# import the necessary packages
# from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.http import HttpResponse
from .forms import ImageUploadForm
from django.conf import settings
from django.shortcuts import render
from .findmk import findmk
import urllib
import json

def postImg(request):
    if request.method =='POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()

            imageURL = settings.MEDIA_URL + form.instance.document.name
            findmk(settings.MEDIA_ROOT_URL + imageURL)

            return render(request, 'index.html',{'form':form,'post':post})
    else:
        form = ImageUploadForm()
    return render(request, 'index.html',{'form':form})


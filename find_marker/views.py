# import the necessary packages
# from django.shortcuts import render
# from django.views.decorators.csrf import csrf_exempt
# from django.http import JsonResponse
# from django.http import HttpResponse
# from .forms import ImageUploadForm
# from django.conf import settings
# from django.shortcuts import render
# from .findmk import findmk
# import urllib
# import json

import json
from django.views import View
from django.http import JsonResponse
from .models import ImageUploadModel


class postImg(View):
    def post(self, request):
        print(request.body)
        data = json.loads(request.body)
        ImageUploadModel(
            document=data['document'],
        ).save()

        # 제대로 응답처리 했다면 200 status와 함께 성공 메세지 전달
        return JsonResponse({'message': 'SUCCESS'}, status=200)

    def get(self, request):
        data = ImageUploadModel.objects.values() # ORM 메소드를 통해 DB에서 데이터를 가져옴
        return JsonResponse({'images':list(data)}, status=200)

# def postImg(request):
#     if request.method =='POST':
#         form = ImageUploadForm(request.POST, request.FILES)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.save()

#             imageURL = settings.MEDIA_URL + form.instance.document.name
#             findmk(settings.MEDIA_ROOT_URL + imageURL)

#             return render(request, 'index.html',{'form':form,'post':post})
#     else:
#         form = ImageUploadForm()
#     return render(request, 'index.html',{'form':form})


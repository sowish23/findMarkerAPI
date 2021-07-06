import json
from django.views import View
from django.http import JsonResponse
from .models import ImageUploadModel
from .models import Address
from .findmk import findmk
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser


class postImg(View):
    parser_classes = (MultiPartParser,)
    def post(self, request, format=None):
        ImageUploadModel(
            document=request.FILES['image'],
        ).save()

        return JsonResponse({'message': 'SUCCESS'}, status=200)

    def get(self, request):
        data = ImageUploadModel.objects.values() 
        data_list = list(data)
        return JsonResponse({'images':data_list[len(data_list)-1]}, status=200)


class getAddress(View):
    parser_classes = (MultiPartParser,)
    def post(self, request, format=None):
        data = json.loads(request.body)
        print('path', data['path'])
        address = findmk(data['path'])

        Address(
            document=data['path'],
            address=address
        ).save()

        return JsonResponse({'message': 'SUCCESS'}, status=200)

    def get(self, request):
        data = Address.objects.values() 
        data_list = list(data)
        return JsonResponse({'address' : data_list[len(data_list)-1]}, status=200)

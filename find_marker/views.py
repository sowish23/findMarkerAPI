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
        print(request.FILES['image'])

        ImageUploadModel(
            document=request.FILES['image'],
        ).save()

        # address = findmk(request.FILES['image'])

        # Address(
        #     document=data['document'],
        #     address=address
        # ).save()

        return JsonResponse({'message': 'SUCCESS'}, status=200)

    def get(self, request):
        data = ImageUploadModel.objects.values() 
        data_a = Address.objects.values() 
        return JsonResponse({'images':list(data), 'addresses' : list(data_a)}, status=200)

import json
from django.views import View
from django.http import JsonResponse
from .models import ImageUploadModel
from .models import Address
from .findmk import findmk


class postImg(View):
    def post(self, request):
        print(request.body)
        data = json.loads(request.body)
        ImageUploadModel(
            document=data['document'],
        ).save()

        address = findmk(data['document'])

        Address(
            document=data['document'],
            address=address
        ).save()

        return JsonResponse({'message': 'SUCCESS'}, status=200)

    def get(self, request):
        data = ImageUploadModel.objects.values() 
        data_a = Address.objects.values() 
        return JsonResponse({'images':list(data), 'addresses' : list(data_a)}, status=200)

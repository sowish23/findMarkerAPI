from django.urls import path
from .views import postImg, getAddress

urlpatterns = [
    path('image/', postImg.as_view()),
    path('address/', getAddress.as_view())
]

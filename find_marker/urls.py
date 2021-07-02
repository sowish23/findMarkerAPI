from django.urls import path
from .views import postImg

urlpatterns = [
    path('', postImg.as_view())
]

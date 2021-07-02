from django.urls import path
from .views import postImg
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', postImg.as_view())
]

urlpatterns += \
    static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
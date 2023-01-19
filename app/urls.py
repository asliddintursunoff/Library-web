

from django.urls import path, include

from app.views import BookView

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    path('',BookView.as_view(), name='book'),
    
]

if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
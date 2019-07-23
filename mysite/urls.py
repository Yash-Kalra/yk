from django.contrib import admin
from django.urls import include, path
from django.conf.urls import url, static
from django.conf import settings

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('mypage/', include('mypage.urls')),
    path('admin/', admin.site.urls),
]+static.static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
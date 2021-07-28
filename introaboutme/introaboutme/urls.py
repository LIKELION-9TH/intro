from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.views.static import serve
from django.conf.urls import url
from django.conf import settings
from rest_framework import routers
from board.views import MusicViewSet

router = routers.DefaultRouter()
router.register('music', MusicViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^media/(?P<path>.*)$', serve,
        {'document_root': settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve,
        {'document_root': settings.STATIC_ROOT}),
    url(r'^', include(router.urls)),
]


urlpatterns += static(settings.STATIC_URL,
                      document_root=settings.STATIC_ROOT, insecure=True)
urlpatterns += static(settings.MEDIA_URL,
                      document_root=settings.MEDIA_ROOT, insecure=True)

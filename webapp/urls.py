from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    url('^$', views.home, name='home'),
    url('gallery/', views.gallery, name='gallery'),
    url('detection/', views.detection, name='detection'),
    url('about/', views.about, name='about'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

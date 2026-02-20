"""
Главен URL конфигурационен файл за проекта Cybersecurity Magazine.
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from . import views

handler404 = 'cybersecurity_magazine.views.custom_404'
urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.home, name='home'),

    path('articles/', include('articles.urls')),
    path('store/', include('store.urls')),
    path('subscriptions/', include('subscriptions.urls')),


    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
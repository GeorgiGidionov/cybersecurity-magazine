from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.conf.urls import handler404
from . import views
from rest_framework.authtoken import views as auth_views

from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets


# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["url", "username", "email", "is_staff"]


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r"users", UserViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.


handler404 = 'cybersecurity_magazine.views.custom_404'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('articles/', include('articles.urls')),
    path('store/', include('store.urls')),
    path('subscriptions/', include('subscriptions.urls')),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('accounts/', include('accounts.urls')),
    path("api-auth/", include("rest_framework.urls")),
    path('api/', include('api.urls')),
    path('api-token-auth/', auth_views.obtain_auth_token, name='api_token_auth'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
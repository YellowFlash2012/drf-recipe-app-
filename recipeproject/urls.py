
from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path, include

from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),


    # swagger doc urls
    path('api/schema/', SpectacularAPIView.as_view(), name='api-schema'),
    
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='api-schema'), name='api-docs'),

    # users app urls
    path('api/v1/users/', include('users.urls')),

    # recipe app urls
    path('api/v1/recipes/', include('recipe.urls')),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root = settings.MEDIA_ROOT
    )
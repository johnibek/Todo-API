from django.contrib import admin
from django.urls import path, include
from .views import home
from drf_yasg import openapi
from drf_yasg.views import get_schema_view


schema_view = get_schema_view(
   openapi.Info(
      title="TODO API",
      default_version='1.0.0',
      description="API for todo list app",
   ),
   public=True,
)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('api/', include('api.urls')),
    path('api-auth/', include('rest_framework.urls')),

    # Djoser
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),

    # Swagger
    path('swagger/schema/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger-schema')
]

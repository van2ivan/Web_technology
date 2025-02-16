from django.contrib import admin
from django.urls import path,include
from rest_framework import permissions
from drf_yasg.views import  get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="ContactBook API",
        default_version='v1',
        description='Test description',
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('', schema_view.with_ui('swagger', cache_timeout=0),
         name='schema-swagger-ui'),
    path('admin/', admin.site.urls),
    path('contacts/', include("contactbook_api.urls")),
    path('auth/', include('djoser.urls'))
]

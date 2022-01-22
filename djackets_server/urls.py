"""djackets_server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin

## Import the possibility to use the settings
from django.conf import settings
from django.conf.urls.static import static

## Add 'include', which allows to include paths from that project
from django.urls import path, include

urlpatterns = [
  path('admin/', admin.site.urls),

  ## Add new paths
  path('api/v1/', include('djoser.urls')),
  path('api/v1/', include('djoser.urls.authtoken')),
  
  ## As said, the following path is imported like this to be more clean
  path('api/v1/', include('product.urls')),

  path('api/v1/', include('order.urls'))

  ## We add the following to use the MEDIA_URL
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

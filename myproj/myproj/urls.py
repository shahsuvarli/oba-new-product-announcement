"""myproj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from dbdesign.views import *

urlpatterns = [
    path('', home_view, name='home'),
    path('process/', process_view, name='process'),
    path('create-product/', create_product_view, name='create-product'),
    path('update-product/<str:pk>/', update_product_view, name='update-product'),
    path('confirm-product/<str:pk>/', confirm_product_view, name='confirm-product'),
    path('product/', product_view, name='product'),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




"""back URL Configuration

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
from poate.views import create_data, upload_images,create_data_with_img, getIt, testIt, Cards, LoginView, Idk, Meditations, Breaths, Sounds

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", create_data),
    path("with_imgs/", create_data_with_img),
    path("a/", upload_images),  
    path('getIt/', getIt),      
    path('testIt/', testIt),
    path('idk/', Idk.as_view(), name='Idk'),
    path('login/', LoginView.as_view(), name='login'),
    path('meditations/', Meditations.as_view(), name='Meditations'),
    path('meditations/<str:pk>/delete', Meditations.as_view(), name='delete_meditation'),
    path('breaths/', Breaths.as_view(), name='breaths'),
    path('breaths/<str:pk>/delete', Breaths.as_view(), name='delete_breath'),
    path('cards/', Cards.as_view(), name='cards'),
    path('cards/<str:pk>/delete', Cards.as_view(), name='delete_card'),
    path('sounds/', Sounds.as_view(), name='sounds'),
    path('sounds/<str:pk>/delete', Sounds.as_view(), name='delete_sound'),
]

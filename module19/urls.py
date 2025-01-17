"""
URL configuration for module19 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from task1.views import main_page, second_page, third_page, sign_up_by_django

urlpatterns = [
    path('', main_page, name='main_page'),
    path('main-page/', main_page, name='main_page'),
    path('second-page/', second_page, name='second_page'),
    path('third-page/', third_page, name='third_page'),
    path('register/', sign_up_by_django, name='register'),
    path('admin/', admin.site.urls)

]

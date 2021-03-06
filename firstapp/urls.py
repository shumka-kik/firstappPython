"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
# from django.conf.urls import url

from . import views
from . models import Post, Category



urlpatterns = [
	path('admin/', admin.site.urls),
    path('', views.base, name='base'),
    path('page1/', views.page1, name='page1'),
	path('page2/', views.page2, name='page2'),
    path('post_list/', views.post_list, name='post_list'),
    path('post_detail/(?P<pk>\d+)/$', views.PostDetailView.as_view(), name='post_detail'),
]
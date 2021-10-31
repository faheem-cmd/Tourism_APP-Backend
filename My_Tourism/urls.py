"""My_Tourism URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.contrib import admin
from django.urls import path, re_path
from django.views.static import serve
from rest_framework.urlpatterns import format_suffix_patterns
from tourism import views
from knox import views as knox_views

from tourism.views import RegisterAPI
from tourism.views import LoginAPI
from tourism.views import EmployeeCreateApi
from tourism.views import EmployeeApi
from tourism.views import EmployeeUpdateApi
from tourism.views import EmployeeDeleteApi

from tourism.views import UserAPIView,feedbackViews,PopularAPIView,HistoryAPIView,ReviewAPIView

urlpatterns = [
    path('', admin.site.urls),
    path('api/places/', views.placesList.as_view()),
    path('reels/', views.reelsList.as_view()),
    path('registers/', RegisterAPI.as_view(), name='register'),
    path('logins/', LoginAPI.as_view(), name='login'),
    path('logouts/', knox_views.LogoutView.as_view(), name='logout'),
    path('api/users/', UserAPIView.as_view()),
    path('popular/', PopularAPIView.as_view()),
    path('history/', HistoryAPIView.as_view()),
    path('reviews/', ReviewAPIView.as_view()),
    path('feedback/', feedbackViews.as_view()),
    path('create/', EmployeeCreateApi.as_view()),
    path('emp/', EmployeeApi.as_view()),
    path('emp/<int:pk>',EmployeeUpdateApi.as_view()),
    path('emp/<int:pk>/delete',EmployeeDeleteApi.as_view()),
    # path('employee/', include('employee.urls')),
    path('api/slider/', views.sliderList.as_view()),
    path('gallery/', views.galleryList.as_view()),
    path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
    re_path(r'^static/(?P<path>.*)/$', serve,
            {'document_root': settings.STATICFILES_DIRS}),
    re_path(r'^media/(?P<path>.*)/$', serve,
            {'document_root': settings.MEDIA_ROOT}),

]

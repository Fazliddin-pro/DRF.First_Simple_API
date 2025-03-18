"""
URL configuration for drfsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path, include, re_path

# from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)


from men.views import MenAPIDelete, MenAPIList, MenAPIUpdate

# router = routers.SimpleRouter()S
# router.register(r'men', MenViewSet, basename='women')

urlpatterns = [
    # path("api/v1/", include(router.urls)),
    path("admin/", admin.site.urls),
    path("api/v1/", include("rest_framework.urls")),
    path("api/v1/menlist/", MenAPIList.as_view()),
    path("api/v1/menlist/<int:pk>/", MenAPIUpdate.as_view()),
    path("api/v1/mendelete/<int:pk>/", MenAPIDelete.as_view()),
    path("api/v1/auth/", include("djoser.urls")),
    re_path(r"^auth/", include("djoser.urls.authtoken")),
    path("api/v1/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/v1/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/v1/token/verify/", TokenVerifyView.as_view(), name="token_verify"),
]

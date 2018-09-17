from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter
from django.conf.urls import url, include
from reviews_app import views
from rest_framework.authtoken import views as authtoken_views


router = DefaultRouter()
router.register(r'reviews', views.ReviewViewSet, base_name='Review')

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^api/', include(router.urls)),
    url(r'^api/register/', views.register_auth),
    url(r'^api/token-auth/', authtoken_views.obtain_auth_token)
]

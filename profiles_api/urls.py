from django.urls import path, include
from rest_framework.routers import DefaultRouter
from profiles_api import views

router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, basename = 'hello-viewset')
router.register('profile-viewset', views.UserProfileViewset)

urlpatterns = [
    path('hello-views/', views.HelloAPIView.as_view()),
    path('', include(router.urls))
]
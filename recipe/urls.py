from django.urls import path, include

from rest_framework.routers import DefaultRouter

from recipe import views

router = DefaultRouter()
router.register('recipes', views.AllUserRecipeViewSet)

router.register('tags', views.TagViewSet)

urlpatterns=[
    path('', include(router.urls)),
]
from django.contrib import admin
from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('projects', ProjectViewSet)

urlpatterns = [
    path('', include(router.urls))
    # path('projects/', Projects.as_view()),
    # path('projects/<int:pk>/', ProjectDetail.as_view()),

]

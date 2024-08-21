from django.urls import path, include
from detection.views import detect_view

urlpatterns = [
    path('', detect_view, name='detect')
]

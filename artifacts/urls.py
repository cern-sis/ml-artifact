from django.urls import path

from .views import *


urlpatterns = [
    path('tags/', TagApiView.as_view()),
    path('model/', MLModelApiView.as_view()),
    path('model/versions', MLModelVersionApiView.as_view()),
    path('dataset/', MLDatasetApiView.as_view()),
    path('dataset/versions', MLDatasetVersionApiView.as_view()),
]

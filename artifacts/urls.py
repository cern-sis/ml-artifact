from django.urls import path

from .model_views import ModelListView, ModelDetailView
from .dataset_views import DatasetListView, DatasetDetailView
from .views import *


urlpatterns = [
    # UI
    path('model/', ModelListView.as_view()),
    path('model/<int:model_id>/', ModelDetailView.as_view()),
    path('dataset/', DatasetListView.as_view()),
    path('dataset/<int:dataset_id>/', DatasetDetailView.as_view()),

    # API
    path('api/tags/', TagApiView.as_view()),
    path('api/model/', MLModelApiView.as_view()),
    path('api/model/versions', MLModelVersionApiView.as_view()),
    path('api/dataset/', MLDatasetApiView.as_view()),
    path('api/dataset/versions', MLDatasetVersionApiView.as_view()),
]

from django.urls import path

from .model_views import ModelListView, ModelDetailView, ModelVersionListView, ModelVersionDetailView
from .dataset_views import DatasetListView, DatasetDetailView, DatasetVersionListView, DatasetVersionDetailView
from .views import *


urlpatterns = [
    # Model UI Views
    path('model/', ModelListView.as_view()),
    path('model/<int:model_id>/', ModelDetailView.as_view()),
    path('model/versions/', ModelVersionListView.as_view()),
    path('model/versions/<uuid:model_version_id>/', ModelVersionDetailView.as_view()),

    # Dataset UI Views
    path('dataset/', DatasetListView.as_view()),
    path('dataset/<int:dataset_id>/', DatasetDetailView.as_view()),
    path('dataset/versions/', DatasetVersionListView.as_view()),
    path('dataset/versions/<uuid:dataset_version_id>/', DatasetVersionDetailView.as_view()),

    # API
    path('api/tags/', TagApiView.as_view()),
    path('api/model/', MLModelApiView.as_view()),
    path('api/model/versions', MLModelVersionApiView.as_view()),
    path('api/dataset/', MLDatasetApiView.as_view()),
    path('api/dataset/versions', MLDatasetVersionApiView.as_view()),
]

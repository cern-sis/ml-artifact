from django.shortcuts import get_object_or_404, render
from rest_framework.views import APIView
from rest_framework import permissions

from .models import MLDataset, MLDatasetVersion, MLModelVersion
from .serializers import MLDatasetSerializer, MLDatasetVersionSerializer, MLModelVersionSerializer

class DatasetListView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        datasets = MLDataset.objects.filter(user=request.user.id)
        serializer = MLDatasetSerializer(datasets, many=True)
        context = {
            'datasets': serializer.data
        }

        return render(request, 'dataset/list.html', context)


class DatasetDetailView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, dataset_id, user_id):
        return get_object_or_404(
            MLDataset,
            id=dataset_id,
            user=user_id)

    def get(self, request, dataset_id):
        dataset = self.get_object(dataset_id, request.user.id)
        serializer = MLDatasetSerializer(dataset)
        versions = MLDatasetVersion.objects.filter(ml_dataset=dataset_id)
        versions_serilizer = MLDatasetVersionSerializer(versions, many=True)
        context = {
            'dataset': serializer.data,
            'versions': versions_serilizer.data
        }

        return render(request, 'dataset/detail.html', context)


class DatasetVersionListView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        dataset_versions = MLDatasetVersion.objects.filter(user=request.user.id)
        serializer = MLDatasetVersionSerializer(dataset_versions, many=True)
        context = {
            "dataset_versions": serializer.data
        }
        return render(request, 'dataset/version_list.html', context)


class DatasetVersionDetailView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, dataset_version_id, user_id):
        return get_object_or_404(
            MLDatasetVersion,
            id=dataset_version_id,
            user=user_id)

    def get(self, request, dataset_version_id):
        dataset_version = self.get_object(dataset_version_id, request.user.id)
        serializer = MLDatasetVersionSerializer(dataset_version)
        model_versions = MLModelVersion.objects.filter(ml_dataset_version=serializer.data.get('id'))
        model_versions_serializer = MLModelVersionSerializer(model_versions, many=True)
        context = {
            "dataset_version": serializer.data,
            "model_version_list": model_versions_serializer.data
        }
        return render(request, 'dataset/version_detail.html', context)

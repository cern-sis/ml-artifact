from django.shortcuts import get_object_or_404, render
from rest_framework.views import APIView
from rest_framework import permissions

from .models import MLDataset, MLDatasetVersion
from .serializers import MLDatasetSerializer, MLDatasetVersionSerializer

class DatasetListView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        ml_datasets = MLDataset.objects.filter(user=request.user.id)
        serializer = MLDatasetSerializer(ml_datasets, many=True)
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
        dataset_model = self.get_object(dataset_id, request.user.id)
        serializer = MLDatasetSerializer(dataset_model)
        context = {
            'dataset': serializer.data
        }

        return render(request, 'dataset/detail.html', context)

from django.shortcuts import get_object_or_404, render
from rest_framework.views import APIView
from rest_framework import permissions

from .models import MLModel, MLModelVersion, Tag
from .serializers import MLModelSerializer, MLModelVersionSerializer, TagSerializer
from .utils import get_slugs

class ModelListView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        models = MLModel.objects.filter(user=request.user.id)
        serializer = MLModelSerializer(models, many=True)
        context = {
            'models': serializer.data
        }

        return render(request, 'model/list.html', context)

    def post(self, request):
        search_query = request.data.get('query')
        fts_slugs = get_slugs(search_query)
        fts_match = []
        for fts_slug in fts_slugs:
            fts_match.append(
                get_object_or_404(MLModel, pk=fts_slug[0]))
        context = {
            'models': fts_match
        }

        return render(request, 'model/list.html', context)


class ModelDetailView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, model_id, user_id):
        return get_object_or_404(
            MLModel,
            id=model_id,
            user=user_id)

    def get_tags(self, tags_data):
        tag_list = []
        for id in tags_data:
            tag = Tag.objects.get(id=id)
            tag_serialize = TagSerializer(tag)
            tag_list.append(tag_serialize.data)
        return tag_list

    def get(self, request, model_id):
        model = self.get_object(model_id, request.user.id)
        serializer = MLModelSerializer(model)
        tag_list = self.get_tags(serializer.data.get('tags'))
        versions = MLModelVersion.objects.filter(ml_model=model_id)
        versions_serilizer = MLModelVersionSerializer(versions, many=True)
        context = {
            'model': serializer.data,
            'versions': versions_serilizer.data,
            'tags': tag_list
        }

        return render(request, 'model/detail.html', context)


class ModelVersionListView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        model_version = MLModelVersion.objects.filter(user=request.user.id)
        serializer = MLModelVersionSerializer(model_version, many=True)
        context = {
            "model_versions": serializer.data
        }
        return render(request, 'model/version_list.html', context)


class ModelVersionDetailView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, model_version_id, user_id):
        return get_object_or_404(
            MLModelVersion,
            id=model_version_id,
            user=user_id)

    def get(self, request, model_version_id):
        dataset_version = self.get_object(model_version_id, request.user.id)
        serializer = MLModelVersionSerializer(dataset_version)
        context = {
            "model_version": serializer.data
        }
        return render(request, 'model/version_detail.html', context)

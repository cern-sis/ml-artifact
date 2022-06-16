from django.shortcuts import get_object_or_404, render
from rest_framework.views import APIView
from rest_framework import permissions

from .models import MLModel
from .serializers import MLModelSerializer
from .utils import get_slugs

class ModelListView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        ml_model = MLModel.objects.filter(user=request.user.id)
        serializer = MLModelSerializer(ml_model, many=True)
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

    def get(self, request, model_id):
        ml_model = self.get_object(model_id, request.user.id)
        serializer = MLModelSerializer(ml_model)
        context = {
            'model': serializer.data
        }

        return render(request, 'model/detail.html', context)

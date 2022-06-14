from django.shortcuts import get_object_or_404, render

from .models import *
from .utils import get_slugs


def detail(request, artifact_id):
    get_artifact = get_object_or_404(MLModel, pk=artifact_id)
    context = {
        'model': get_artifact,
    }
    return render(request, 'artifacts/detail.html', context)


def index(request):
    if request.method == 'POST':
        query = request.POST['query']
        slugs = get_slugs(query)
        matching_artifacts = []
        for slug in slugs:
            matching_artifacts.append(
                get_object_or_404(MLModel, pk=slug[0]))
        context = {
            'models': matching_artifacts,
        }
        return render(request, 'artifacts/index.html', context)
    return render(request, 'artifacts/index.html')

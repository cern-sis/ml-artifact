from executing import Source
from rest_framework import serializers

from .models import *


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['name', 'user']


class MLDatasetSerializer(serializers.ModelSerializer):
    class Meta:
        model = MLDataset
        fields = ['name', 'description', 'user']


class MLModelSerializer(serializers.ModelSerializer):
    tags = TagSerializer(read_only=True, many=True)

    class Meta:
        model = MLModel
        fields = ['name', 'description', 'tags', 'user']


class MLDatasetVersionSerializer(serializers.ModelSerializer):
    ml_dataset = serializers.CharField(source='ml_dataset.name')

    class Meta:
        model = MLDatasetVersion
        fields = ['id', 'url', 'version', 'ml_dataset', 'user']


class MLModelVersionSerializer(serializers.ModelSerializer):
    ml_model = serializers.CharField(source='ml_model.name')
    ml_dataset_version = serializers.CharField(source='ml_dataset_version.version')

    class Meta:
        model = MLModelVersion
        fields = ['id', 'url', 'version', 'ml_model', 'ml_dataset_version', 'user']

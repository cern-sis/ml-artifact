from executing import Source
from rest_framework import serializers

from .models import *


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name', 'user']


class MLDatasetSerializer(serializers.ModelSerializer):
    class Meta:
        model = MLDataset
        fields = ['id', 'name', 'description', 'user']


class MLModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = MLModel
        fields = ['id', 'name', 'description', 'tags', 'user']

    def create(self, validated_data):
        tags_data = validated_data.pop('tags')

        ml_model = MLModel.objects.create(**validated_data)
        ml_model.save()

        for tag in tags_data:
            ml_model.tags.add(tag)

        return ml_model

    def update(self, instance, validated_data):
        tags_data = validated_data.pop('tags')

        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.save()

        for tag in tags_data:
            instance.tags.add(tag)

        return instance


class MLDatasetVersionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MLDatasetVersion
        fields = ['id', 'url', 'version', 'ml_dataset', 'user']


class MLModelVersionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MLModelVersion
        fields = ['id', 'url', 'version', 'ml_model', 'ml_dataset_version', 'user']

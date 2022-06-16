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
    ml_dataset = MLDatasetSerializer()

    class Meta:
        model = MLDatasetVersion
        fields = ['id', 'url', 'version', 'ml_dataset', 'user']


    def create(self, validated_data):
        ml_dataset_data = validated_data.pop('ml_dataset')

        ml_dataset_version = MLDatasetVersion.objects.create(**validated_data)
        ml_dataset_version.save()

        ml_dataset_version.ml_dataset = ml_dataset_data

        return ml_dataset_version


class MLModelVersionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MLModelVersion
        fields = ['id', 'url', 'version', 'ml_model', 'ml_dataset_version', 'user']


    def create(self, validated_data):
        ml_model = validated_data.pop('ml_model')
        ml_dataset_version = validated_data.pop('ml_dataset_version')

        ml_model_version = MLModelVersion.objects.create(**validated_data)
        ml_model_version.save()

        ml_model_version.ml_model = ml_model
        ml_model_version.ml_dataset_version = ml_dataset_version

        return ml_model_version

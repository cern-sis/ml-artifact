from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions

from .models import *
from .serializers import *


class TagApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        tags = Tag.objects.filter(user=request.user.id)
        serializer = TagSerializer(tags, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        data = {
            'name': request.data.get('name'),
            'user': request.user.id
        }
        serializer = TagSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MLDatasetApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        tags = MLDataset.objects.filter(user=request.user.id)
        serializer = MLDatasetSerializer(tags, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        data = {
            'name': request.data.get('name'),
            'description': request.data.get('description'),
            'user': request.user.id
        }
        serializer = MLDatasetSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MLModelApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, mlmodel_name, user_id):
        return MLModel.objects.get(name=mlmodel_name, user=user_id)

    def get(self, request, *args, **kwargs):
        ml_model = MLModel.objects.filter(user=request.user.id)
        serializer = MLModelSerializer(ml_model, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):
        data = {
            'name': request.data.get('name'),
            'description': request.data.get('description'),
            'tags': request.data.get('tags'),
            'user': request.user.id
        }
        serializer = MLModelSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, *args, **kwargs):
        mlmodel_name = request.data.get('name')
        mlmodel_instance = self.get_object(mlmodel_name, request.user.id)
        if not mlmodel_instance:
            return Response(
                {"res": "Object does not exists."},
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'name': request.data.get('name'),
            'description': request.data.get('description'),
            'tags': request.data.get('tags'),
            'user': request.user.id
        }
        serializer = MLModelSerializer(instance=mlmodel_instance, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        mlmodel_name = request.data.get('name')
        mlmodel_instance = self.get_object(mlmodel_name, request.user.id)
        if not mlmodel_instance:
            return Response(
                {"res": "Object does not exists."},
                status=status.HTTP_400_BAD_REQUEST
            )
        mlmodel_instance.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )


class MLDatasetVersionApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, mldatasetversion_id, user_id):
        return MLDatasetVersion.objects.get(id=mldatasetversion_id, user=user_id)

    def get(self, request, *args, **kwargs):
        ml_model = MLDatasetVersion.objects.filter(user=request.user.id)
        serializer = MLDatasetVersionSerializer(ml_model, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        data = {
            'url': request.data.get('url'),
            'version': request.data.get('version'),
            'ml_dataset': request.data.get('ml_dataset'),
            'user': request.user.id
        }
        serializer = MLDatasetVersionSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, *args, **kwargs):
        mldatasetversion_id = request.data.get('mldatasetversion_id')
        mldatasetversion_instance = self.get_object(mldatasetversion_id, request.user.id)
        if not mldatasetversion_instance:
            return Response(
                {"res": "Object does not exists."},
                status=status.HTTP_400_BAD_REQUEST
            )
        mldatasetversion_instance.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )


class MLModelVersionApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, mlmodel_id, user_id):
        return MLModelVersion.objects.get(id=mlmodel_id, user=user_id)

    def get(self, request, *args, **kwargs):
        ml_model = MLModelVersion.objects.filter(user=request.user.id)
        serializer = MLModelVersionSerializer(ml_model, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        data = {
            'url': request.data.get('url'),
            'version': request.data.get('version'),
            'ml_model': request.data.get('ml_model'),
            'ml_dataset_version': request.data.get('ml_dataset_version'),
            'user': request.user.id
        }
        serializer = MLModelVersionSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, *args, **kwargs):
        mlmodelversion_id = request.data.get('mlmodelversion_id')
        mlmodelversion_instance = self.get_object(mlmodelversion_id, request.user.id)
        if not mlmodelversion_instance:
            return Response(
                {"res": "Object does not exists."},
                status=status.HTTP_400_BAD_REQUEST
            )
        mlmodelversion_instance.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )

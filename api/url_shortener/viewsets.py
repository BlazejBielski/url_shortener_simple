from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import get_object_or_404

from rest_framework import status


from . import models
from . import serializers


class URLViewSet(ModelViewSet):
    queryset = models.URL.objects.all()
    serializer_class = serializers.URLSerializer

    def list(self, request, *args, **kwargs):
        queryset = models.URL.objects.all()
        urls = self.serializer_class(queryset, many=True)
        return Response(data=urls.data, status=status.HTTP_200_OK)

    def retrieve(self, request, *args, pk=None, **kwargs):
        url = get_object_or_404(queryset=self.get_queryset(), pk=pk)
        return Response(data=self.serializer_class(url).data, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        serializer = serializers.URLSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

from rest_framework import viewsets
from . import models
from classes import serializers
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework.decorators import detail_route


class IsSuperUser(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        else:
            if request.method == 'DELETE':
                return False


class ClassesViewSet (viewsets.ModelViewSet):
    permission_classes = (IsSuperUser, permissions.DjangoModelPermissions)
    queryset = models.Classes.objects.all()
    serializer_class = serializers.ClassesSerializer

    @detail_route(methods=['get']) # this
    def reviews(self, request, pk=None):
        self.pagination_class.page_size = 1
        reviews = models.Review.objects.filter(classes_id=pk)
        page = self.paginate_queryset(reviews)

        if page is not None:
            serializer = serializers.ReviewSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = serializers.ReviewSerializer(
            reviews, many=True)
        return Response(serializer.data)


class ReviewViewSet(mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    viewsets.GenericViewSet):
    queryset = models.Review.objects.all()
    serializer_class = serializers.ReviewSerializer

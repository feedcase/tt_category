from rest_framework import generics
from category_api.models import *
from rest_framework.serializers import *
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.routers import DefaultRouter
from category_api.views import *

__all__ = 'CategoriesSerializer', 'CategoriesViewSet'


class ChildrenSerializer(ModelSerializer):
    class Meta:
        model = Categories
        fields = ['id', 'name', 'children']


class ParentSerializer(ModelSerializer):
    class Meta:
        model = Categories
        fields = ['id', 'name']


class SiblingsSerializer(ModelSerializer):
    class Meta:
        model = Categories.objects.values_list('parent', flat=True)
        fields = ['id', 'name']


class CategoriesSerializer(ModelSerializer):
    children = ChildrenSerializer(many=True, read_only=True)
    parent = ParentSerializer(many=False, read_only=True)
    if parent is not None:
        class Meta:
            model = Categories
            fields = ['id', 'name', 'parent', 'children']
    else:
        siblings = SiblingsSerializer(many=True, read_only=True)

        class Meta:
            model = Categories
            fields = ['id', 'name', 'parent', 'children', 'siblings']


class CategoriesViewSet(ModelViewSet):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer


router = DefaultRouter()
router.register('categories', CategoriesViewSet, 'categories')

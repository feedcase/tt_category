from rest_framework import generics
from category_api.models import *
from rest_framework import serializers
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from category_api.views import *


# class SiblingsSerializer(serializers.ModelSerializer):
#     """Siblings representation"""
#
#     class Meta:
#         model = Categories
#         fields = ['id', 'name']


class ParentSerializer(serializers.ModelSerializer):
    """Parents representation"""

    class Meta:
        model = Categories
        fields = ('id', 'name')


class RecursiveSerializer(serializers.ModelSerializer):
    """Implementation of the representation of children"""

    def to_representation(self, value):
        if self.parent.parent.__class__(value, context=self.context):
            serializer = self.parent.parent.__class__(value, context=self.context)
            return serializer.data


class CategoriesListSerializer(serializers.ModelSerializer):
    """Categories list"""

    children = RecursiveSerializer(many=True)

    class Meta:
        model = Categories
        fields = ('name', 'children')


class CategoryDetailSerializer(serializers.ModelSerializer):
    """Category details"""

    parent = ParentSerializer(many=False)
    children = RecursiveSerializer(many=True)
    # siblings = SiblingsSerializer(many=True)

    class Meta:
        model = Categories
        fields = ('id', 'name', 'parent', 'children')


class CategoryCreateSerializer(serializers.ModelSerializer):
    """Creating category"""

    class Meta:
        model = Categories
        fields = '__all__'

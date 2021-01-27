from django.shortcuts import render
from category_api.models import *
from rest_framework.views import APIView
from category_api.serializer import CategoriesListSerializer, CategoryDetailSerializer, CategoryCreateSerializer
from rest_framework.response import Response


class CategoryListView(APIView):
    def get(self, request):
        categories = Categories.objects.filter(parent=None)
        serializer = CategoriesListSerializer(categories, many=True)
        return Response(serializer.data)


class CategoryDetailsView(APIView):
    def get(self, request, pk):
        category = Categories.objects.get(id=pk)
        serializer = CategoryDetailSerializer(category)
        return Response(serializer.data)


class CategoryCreateView(APIView):
    def post(self, request):
        category = CategoryCreateSerializer(data=request.data)
        if category.is_valid():
            category.save()
        return Response(status=201)

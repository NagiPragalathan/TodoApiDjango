from django.urls import path
from base.models import Category
from base.serializers import CategorySerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view


@api_view(['POST'])
def create_category(request):
    if request.method == 'POST':
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['GET'])
def list_categories(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_category_details(request, category_id):
    if request.method == 'GET':
        category = Category.objects.get(id=category_id)
        serializer = CategorySerializer(category)
        return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def update_category(request, category_id):
    if request.method == 'PUT':
        category = Category.objects.get(id=category_id)
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_category(request, category_id):
    if request.method == 'DELETE':
        category = Category.objects.get(id=category_id)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


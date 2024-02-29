from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from base.models import Todo, Category
from base.serializers import TodoSerializer

@api_view(['POST'])
def create_todo(request):
    if request.method == 'POST':
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            todo_data = serializer.validated_data
            if todo_data.get('category') is None:
                todo_data['category'] = Category.objects.get(id=1)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
    
@api_view(['GET'])
def list_todos(request):
    if request.method == 'GET':
        todos = Todo.objects.all()
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data)
    
@api_view(['GET'])
def get_todo_details(request, todo_id):
    try:
        todo = Todo.objects.get(id=todo_id)
    except Todo.DoesNotExist:
        return Response({"error": "Todo not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TodoSerializer(todo)
        return Response(serializer.data)

@api_view(['PUT'])
def update_todo(request, todo_id):
    try:
        todo = Todo.objects.get(id=todo_id)
    except Todo.DoesNotExist:
        return Response({"error": "Todo not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = TodoSerializer(todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_todo(request, todo_id):
    try:
        todo = Todo.objects.get(id=todo_id)
    except Todo.DoesNotExist:
        return Response({"error": "Todo not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        todo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


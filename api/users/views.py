# api/users/views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET'])
def list_users(request):
    return Response([{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}])

@api_view(['GET'])
def user_detail(request, user_id):
    # In a real app, fetch user by user_id
    if int(user_id) == 1:
        return Response({"id": 1, "name": "Alice", "email": "alice@example.com"})
    return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import UserRegistration # Your model name is correct
from .serializer import UserRegistrationSerializer # Your serializer name is correct

# Handles creating a new user (POST request)
@api_view(['POST'])
def register_user(request):
    serializer = UserRegistrationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Handles listing all users (GET request)
@api_view(['GET'])
def list_user(request):
    users = UserRegistration.objects.all()
    serializer = UserRegistrationSerializer(users, many=True)
    return Response(serializer.data) # Status 200 is the default, so no need to specify it

# Handles retrieving (GET), updating (PUT), and deleting (DELETE) a single user
@api_view(['GET', 'PUT', 'DELETE'])
def user_detail(request, pk):
    """
    Retrieve, update or delete a user.
    """
    try:
        user = UserRegistration.objects.get(pk=pk)
    except UserRegistration.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserRegistrationSerializer(user)
        return Response(serializer.data)

    elif request.method == 'PUT':
        # Using partial=True allows for partial updates (like a PATCH request)
        serializer = UserRegistrationSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
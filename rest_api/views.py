from rest_framework import viewsets
from models import User, Task
from serializers import UserSerializer, TaskSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint to allow viewing and/or editing of Users.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class TaskViewSet(viewsets.ModelViewSet):
    """
    API endpoint to allow viewing and/or editing of Tasks.
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
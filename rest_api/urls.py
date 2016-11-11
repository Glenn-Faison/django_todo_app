from rest_framework import routers
from views import UserViewSet, TaskViewSet


restAPIrouter = routers.DefaultRouter()
restAPIrouter.register(r'users', UserViewSet)
restAPIrouter.register(r'tasks', TaskViewSet)
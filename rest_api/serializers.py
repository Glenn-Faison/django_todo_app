from models import User, Task
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    """
    Convert User info to stream object
    """
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'password']
        write_only_fields = ['password']

    def create(self, validated_data):
        """
        Create and return a new `User` instance, given the validated data.
        """
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        # return language from validated_data dict, else, return instance.url
        instance.url = validated_data.get('url', instance.url)
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.password = validated_data.get('password', instance.password)
        instance.save()
        return instance


class TaskSerializer(serializers.HyperlinkedModelSerializer):
    """
    Convert Task objects to stream
    """
    class Meta:
        model = Task
        fields = ['url', 'owner', 'date_created', 'description', 'task_start_date', 'task_end_date', 'completed']
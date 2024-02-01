from rest_framework import serializers

from fitness_training_project.micro_services.users.repositories.base.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

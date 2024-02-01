from rest_framework import serializers

from fitness_training_project.micro_services.fitness.repositories.event_type.models import EventType


class EventTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = EventType
        fields = "__all__"
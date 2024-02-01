from rest_framework import serializers

from fitness_training_project.micro_services.fitness.repositories.event.models import Event


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = "__all__"

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['user'] = instance.user.username
        response['event_type'] = instance.event_type.title
        response['training_program'] = instance.training_program and instance.training_program.title
        return response

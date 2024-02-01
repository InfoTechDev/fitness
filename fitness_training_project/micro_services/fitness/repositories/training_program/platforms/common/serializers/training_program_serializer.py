from rest_framework import serializers

from fitness_training_project.micro_services.fitness.repositories.training_program.models import TrainingProgram


class TrainingProgramSerializer(serializers.ModelSerializer):

    class Meta:
        model = TrainingProgram
        fields = "__all__"
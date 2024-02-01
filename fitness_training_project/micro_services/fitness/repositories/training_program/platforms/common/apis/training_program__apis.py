from fitness_training_project.micro_services.base.views.generic.view_set import BaseViewSet
from fitness_training_project.micro_services.fitness.repositories.training_program.models import TrainingProgram
from fitness_training_project.micro_services.fitness.repositories.training_program.platforms.common.serializers.training_program_serializer import \
    TrainingProgramSerializer


class TrainingProgramAPI(BaseViewSet):
    queryset = TrainingProgram.objects.all()
    model = TrainingProgram
    serializer_class = TrainingProgramSerializer

from fitness_training_project.micro_services.base.views.generic.view_set import BaseViewSet
from fitness_training_project.micro_services.fitness.repositories.event.models import Event
from fitness_training_project.micro_services.fitness.repositories.event.platforms.common.serializers.event_serializer import \
    EventSerializer


class EventAPI(BaseViewSet):
    queryset = Event.objects.all()
    model = Event
    serializer_class = EventSerializer

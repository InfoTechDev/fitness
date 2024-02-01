from fitness_training_project.micro_services.base.views.generic.view_set import BaseViewSet
from fitness_training_project.micro_services.fitness.repositories.event_type.models import EventType
from fitness_training_project.micro_services.fitness.repositories.event_type.platforms.common.serializers.event_type_serializer import \
    EventTypeSerializer


class EventTypeAPI(BaseViewSet):
    queryset = EventType.objects.all()
    model = EventType
    serializer_class = EventTypeSerializer
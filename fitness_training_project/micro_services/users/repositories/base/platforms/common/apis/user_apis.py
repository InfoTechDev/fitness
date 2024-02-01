from fitness_training_project.micro_services.base.views.generic.view_set import BaseViewSet
from fitness_training_project.micro_services.users.repositories.base.models import User
from fitness_training_project.micro_services.users.repositories.base.platforms.common.serializers.user_serializer import \
    UserSerializer


class UserAPI(BaseViewSet):
    queryset = User.objects.all()
    model = User
    serializer_class = UserSerializer

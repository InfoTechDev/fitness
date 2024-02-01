from django.urls import path, include
from rest_framework import routers

from fitness_training_project.micro_services.fitness.repositories.training_program.platforms.mobile.apis.training_program_mobile_apis import \
    TrainingProgramMobileAPI

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'training-programs', TrainingProgramMobileAPI)

urlpatterns = [
    path('', include(router.urls)),
]

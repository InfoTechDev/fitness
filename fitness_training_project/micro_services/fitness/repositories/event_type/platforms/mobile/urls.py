from django.urls import path, include
from rest_framework import routers

from fitness_training_project.micro_services.fitness.repositories.event_type.platforms.mobile.apis.event_type_mobile_apis import \
    EventTypeMobileAPI

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'event-types', EventTypeMobileAPI)

urlpatterns = [
    path('', include(router.urls)),
]
from django.urls import path, include
from rest_framework import routers

from fitness_training_project.micro_services.fitness.repositories.event.platforms.mobile.apis.event_mobile_apis import \
    EventMobileAPI

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'event', EventMobileAPI)

urlpatterns = [
    path('', include(router.urls)),
]

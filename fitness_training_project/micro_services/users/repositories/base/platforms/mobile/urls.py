from django.urls import path, include
from rest_framework import routers

from fitness_training_project.micro_services.users.repositories.base.platforms.mobile.apis.user_mobile_apis import \
    UserMobileAPI

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'users', UserMobileAPI)

urlpatterns = [
    path('', include(router.urls)),
]

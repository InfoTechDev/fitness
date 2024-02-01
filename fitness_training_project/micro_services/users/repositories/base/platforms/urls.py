from django.urls import path, include

urlpatterns = [
    path('', include('fitness_training_project.micro_services.users.repositories.base.platforms.mobile.urls')),
]
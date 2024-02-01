from django.urls import path, include

urlpatterns = [
    path('', include('fitness_training_project.micro_services.fitness.repositories.training_program.platforms.urls')),
]
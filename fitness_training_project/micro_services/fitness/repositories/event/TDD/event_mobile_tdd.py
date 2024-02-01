from django.test import TestCase

from fitness_training_project.micro_services.fitness.repositories.event.models import Event
from fitness_training_project.micro_services.users.repositories.base.models import User
from fitness_training_project.micro_services.fitness.repositories.event_type.models import EventType
from fitness_training_project.micro_services.fitness.repositories.training_program.models import TrainingProgram


# Define the test case class
class EventModelTestCase(TestCase):
    # Define the setup method
    def setUp(self):
        # Create a user, event type, and training program for testing
        self.user = User.objects.create(username='testuser')
        self.event_type = EventType.objects.create(title='Test Event Type')
        self.training_program = TrainingProgram.objects.create(title='Test Training Program')

    # Define a test case
    def test_event_creation(self):
        # Create an event using the user, event type, and training program
        event = Event.objects.create(user=self.user, device='Test Device', event_type=self.event_type, training_program=self.training_program)
        # Assert that the created event is an instance of the Event model
        self.assertIsInstance(event, Event)
        # Assert that the string representation of the event equals its id
        self.assertEqual(str(event.id), str(event.id))
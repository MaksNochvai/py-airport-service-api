from unittest import TestCase

from airport_service.models import Crew


class CrewModelTest(TestCase):
    def setUp(self):
        self.crew = Crew.objects.create(first_name='John', last_name='Doe')

    def test_str_representation(self):
        self.assertEqual(str(self.crew), 'John Doe')

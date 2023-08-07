from unittest import TestCase

from airport_service.models import AirplaneType


class AirplaneTypeModelTest(TestCase):
    def setUp(self):
        self.airplane_type = AirplaneType.objects.create(name='Type 1')

    def test_str_representation(self):
        self.assertEqual(str(self.airplane_type), 'Type 1')

from django.test import TestCase
from airport_service.models import Airplane, AirplaneType


class AirplaneModelTest(TestCase):
    def setUp(self):
        self.airplane_type = AirplaneType.objects.create(name='Type hjk')
        self.airplane = Airplane.objects.create(
            name='Airplane L',
            rows=10,
            seats_in_row=6,
            airplane_type=self.airplane_type)

    def test_str_representation(self):
        self.assertEqual(str(self.airplane), 'Airplane L')

    def test_capacity_calculation(self):
        self.assertEqual(self.airplane.capacity, 60)

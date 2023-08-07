from django.test import TestCase
from airport_service.models import Route, Airport


class RouteModelTest(TestCase):
    def setUp(self):
        self.source_airport = Airport.objects.create(name='Airport A', closest_big_city='City A')
        self.destination_airport = Airport.objects.create(name='Airport B', closest_big_city='City B')
        self.route = Route.objects.create(
            source=self.source_airport,
            destination=self.destination_airport,
            distance=100)

    def test_str_representation(self):
        self.assertEqual(str(self.route), 'Airport A - Airport B')

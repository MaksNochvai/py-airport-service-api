from datetime import datetime, timedelta
from unittest import TestCase

from airport_service.models import Airport, AirplaneType, Airplane, Route, Flight


class FlightModelTest(TestCase):
    def setUp(self):
        self.source_airport = Airport.objects.create(name='Airport A', closest_big_city='City A')
        self.destination_airport = Airport.objects.create(name='Airport B', closest_big_city='City B')
        self.airplane_type = AirplaneType.objects.create(name='Unique Type')
        self.airplane = Airplane.objects.create(
            name='Airplane A',
            rows=10, seats_in_row=6,
            airplane_type=self.airplane_type
        )
        self.route = Route.objects.create(
            source=self.source_airport,
            destination=self.destination_airport,
            distance=100
        )
        self.flight = Flight.objects.create(
            route=self.route,
            airplane=self.airplane,
            departure_time=datetime.now(),
            arrival_time=datetime.now() + timedelta(hours=2)
        )

    def test_str_representation(self):
        self.assertEqual(str(self.flight), 'Airport A - Airport B')

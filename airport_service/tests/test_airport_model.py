from django.test import TestCase
from airport_service.models import Airport


class AirportModelTest(TestCase):
    def test_create_airport(self):
        airport = Airport.objects.create(
            name="Test Airport",
            closest_big_city="Test City"
        )
        self.assertEqual(airport.name, "Test Airport")
        self.assertEqual(airport.closest_big_city, "Test City")

    def test_unique_name(self):
        airport1 = Airport.objects.create(name="Airport 1", closest_big_city="City 1")
        with self.assertRaises(Exception) as context:
            airport2 = Airport.objects.create(name="Airport 1", closest_big_city="City 2")

        self.assertTrue('UNIQUE constraint failed' in str(context.exception))

from unittest import TestCase
from airport_service.models import Order
from user.models import User


class OrderModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(email="testuser@test.com", password='testpassword')
        self.order = Order.objects.create(user=self.user)

    def test_str_representation(self):
        expected_str = str(self.order.created_at)
        self.assertEqual(str(self.order), expected_str)

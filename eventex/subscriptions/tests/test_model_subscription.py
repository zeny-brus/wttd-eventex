from datetime import datetime

from django.test import TestCase
from eventex.subscriptions.models import Subscription


class SubscriptionModelTest(TestCase):
    def setUp(self):
        self.obj = Subscription(
            name='Fulano Ciclano',
            cpf='12345678901',
            email='fulano@email.com',
            phone='51-9999999990'
        )
        self.obj.save()

    def test_create(self):
        self.assertTrue(Subscription.objects.exists())

    def test_created_at(self):
        """Subscriptions must have an auto created_at attr."""
        self.assertIsInstance(self.obj.created_at, datetime)

from django.test import TestCase
from django.contrib.auth.models import User

from .models import Ticket


class TicketModelTest(TestCase):

    def test_create_ticket(self):

        user = User.objects.create_user(
            username="zahra",
            password="1234"
        )

        ticket = Ticket.objects.create(
            title="Cannot login",
            description="Forgot password",
            priority="HIGH",
            status="OPEN",
            user=user,
        )

        self.assertEqual(ticket.title, "Cannot login")
        self.assertEqual(ticket.priority, "HIGH")
        self.assertEqual(ticket.user.username, "zahra")
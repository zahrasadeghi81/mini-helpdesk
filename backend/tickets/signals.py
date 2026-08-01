import requests

from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Ticket


N8N_WEBHOOK_URL = "http://n8n:5678/webhook-test/new-ticket"

@receiver(post_save, sender=Ticket)
def ticket_created(sender, instance, created, **kwargs):

    if created:

        print("🔥 SIGNAL FIRED")

        data = {
            "id": instance.id,
            "title": instance.title,
            "description": instance.description,
            "priority": instance.priority,
            "status": instance.status,
            "user": instance.user.username,
        }

        print(data)

        try:
            requests.post(
                N8N_WEBHOOK_URL,
                json=data,
                timeout=5
            )

        except requests.exceptions.RequestException as e:
            print("n8n connection failed:", e)
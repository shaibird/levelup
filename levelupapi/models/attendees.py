from django.db import models

class Attendees(models.Model):
    event = models.ForeignKey("event", on_delete=models.CASCADE, related_name="event")
    gamer = models.ForeignKey("Gamer", on_delete=models.CASCADE, default=False, related_name="attendee")
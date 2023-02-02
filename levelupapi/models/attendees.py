from django.db import models

class Attendees(models.Model):
    event = models.ForeignKey("event", on_delete=models.CASCADE, related_name="event")
    player = models.ForeignKey("game", on_delete=models.CASCADE, related_name="game")
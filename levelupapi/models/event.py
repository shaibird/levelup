from django.db import models

class Event(models.Model):

    game = models.ForeignKey("Game", on_delete=models.CASCADE, related_name="game_event")
    organizer = models.ForeignKey("Gamer", on_delete=models.CASCADE, related_name="organizer")
    attendees = models.ManyToManyField("Gamer", related_name="attendees")
    datetime = models.DateTimeField(auto_now=False, auto_now_add=False)
    description = models.CharField(max_length=200)
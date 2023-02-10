from django.db import models

class Game(models.Model):
    """Representation of a playable game that a gamer can create"""
    gametype = models.ForeignKey("GameType", default=1, on_delete=models.CASCADE)
    title = models.CharField(max_length=55)
    maker = models.CharField(max_length=55)
    gamer = models.ForeignKey("Gamer", on_delete=models.CASCADE, related_name="games")
    number_of_players = models.IntegerField()
    skill_level = models.IntegerField()
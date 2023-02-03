from django.db import models

class Game(models.Model):
    title = models.CharField(max_length=100)
    gamer = models.ForeignKey("Gamer", null=True, on_delete=models.CASCADE, related_name="gamer")
    game_type = models.ForeignKey("GameType", on_delete=models.CASCADE, related_name="game")
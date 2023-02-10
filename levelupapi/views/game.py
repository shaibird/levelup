from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from levelupapi.models import Game, Gamer, GameType
from django.core.exceptions import ValidationError


class GameView(ViewSet):
    """Level up game types view"""
    def create(self, request):
        """Handle POST operations

        Returns:
            Response -- JSON serialized game instance
        """
        gamer = Gamer.objects.get(user=request.auth.user)
        serializer = CreateGameSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(gamer=gamer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk):
        """Handle GET requests for single game type

        Returns:
            Response -- JSON serialized game type
        """
        game = Game.objects.get(pk=pk)
        serializer = GameSerializer(game)
        return Response(serializer.data)

    def list(self, request):
        """Handle GET requests to get all game types

        Returns:
            Response -- JSON serialized list of game types
        """
        games = Game.objects.all()
        serializer = GameSerializer(games, many=True)
        return Response(serializer.data)

class CreateGameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ['id', 'gametype','title', 'maker', 'gamer', "number_of_players", "skill_level"]

class GameMakerSerializer(serializers.ModelSerializer):

    model = Gamer
    fields = ('id', 'full_name', 'bio')


class GameSerializer(serializers.ModelSerializer):
    """JSON serializer for game types
    """
    # gamer = GameMakerSerializer(many=False)

    class Meta:
        model = Game
        fields = ('id', 'gametype','title', 'maker', 'gamer', "number_of_players", "skill_level")
        depth = 1
from ..models.player import Player
from ..views.player_view import PlayerView


class PlayerController:


    def __init__(self):
        self.view = PlayerView()
        self.players = []

    def new_player(self):
        player = Player(
                        self.view.first_name_player(),
                        self.view.last_name_player(),
                        self.view.birth_date_player(),
                        )
                        
        return player

t = PlayerController()
t.new_player()
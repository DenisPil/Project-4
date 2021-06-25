from models.player import Player
from views.player_view import PlayerView


class PlayerController:


    def __init__(self):
        self.view = PlayerView()
        self.list_player = []


    def new_player(self):
        player = Player(
                        self.view.set_first_name_player(),
                        self.view.set_last_name_player(),
                        self.view.set_birth_date_player(),
                        )
        self.list_player.append(player)
        print(self.list_player)                
        return player

t = PlayerController()
t.new_player()
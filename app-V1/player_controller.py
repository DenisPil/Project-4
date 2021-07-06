from model.player import Player
from controller.grab import Input


class PlayerController:
    def __init__(self):
        pass

    def run(self):
        self.new_player = self.add_new_player()

    def add_new_player(self):

        """
        control_input = Input()
        first_name = control_input.get_input_str("Le prénom du joueur :")
        last_name = control_input.get_input_str("Le nom du joueur :")
        gender = control_input.get_gender("Le genre du joueur H ou F :")
        elo = control_input.get_input_int("L'ELO du joueur :")
        birthday = control_input.get_input_date("Veuillez saisir la date de naissance dans le format 01/01/1901")
        """

        player = Player(first_name="",
                        last_name=Player.player_id,
                        gender="genre",
                        elo=Player.player_id,
                        ranking_points=0,
                        birthday="birthday"
                        )

        player.create_dict()
        return player

"""p = PlayerController()
p.run()"""

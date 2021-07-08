from model.tournament import Tournament
from controller.grab import Input
from player_controller import PlayerController
from model.round import Round
from round_controller import RoundController

class TournamentController:
    def __innit__(self):
        pass

    def run(self):
        self.add_new_tournament()

    def add_new_tournament(self):

        control_input = Input()
        round_controller = RoundController()

        """Création des informations de base d'un tournoi"""

        # name = control_input.get_input_str("le nom")
        # place = control_input.get_input_str("la ville")
        # time_ctrl = control_input.get_rythme("le rythme de la partie Bullet = 1, Blitz = 2")
        # start_date = control_input.get_input_date("le début de tournoi")
        # end_date = control_input.get_input_date("la fin de tournoi")

        tournament = Tournament(name="name",
                                place="place",
                                time_ctrl="time_ctrl",
                                start_date="start_date",
                                end_date="end_date"
                                )

        """Ajout de joueurs au tournoi"""

        while len(tournament.list_players) != 8:
            value = input("Voulez vous ajouter un nouveau joueur, ou un joueur de la BDD. 1=new 2=BDD : ")
            if value == "1":
                player = PlayerController().add_new_player()
                tournament.list_players.append(player)
            else:
                value = input()

        list_rounds = tournament.create_rounds()
        round_1 = list_rounds[0]
        matchs_in_round_1 = round_1.create_matchs_in_round()
        result = round_1.get_winner(matchs_in_round_1)
        tournament.set_ranking_points(result)

t = TournamentController()
t.run()

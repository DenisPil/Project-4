from model.tournament import Tournament
from controller.grab import Input
from player_controller import PlayerController
# from model.round import Round
# from round_controller import RoundController

class TournamentController:
    def __innit__(self):
        self.tournament = None
        self.control_input = Input()
        self.player = PlayerController()

    def start(self):
        self.add_new_tournament()

    def start_tournament(self):
        self.tournament.create_rounds()
        self.add_players()

    def add_new_tournament(self):

        """Création des informations de base d'un tournoi"""

        # name = self.control_input.get_input_str("le nom")
        # place = self.control_input.get_input_str("la ville")
        # time_ctrl = self.control_input.get_rythme("le rythme de la partie Bullet = 1, Blitz = 2")
        # start_date = self.control_input.get_input_date("le début de tournoi")
        # end_date = self.control_input.get_input_date("la fin de tournoi")

        self.tournament = Tournament(name="name",
                                     location="location",
                                     time_ctrl="time_ctrl",
                                     start_date="start_date",
                                     end_date="end_date"
                                     )

    def add_players(self):
        """Ajout de joueurs au tournoi"""

        while len(self.tournament.list_players) != 8:
            value = input("Voulez vous ajouter un nouveau joueur, ou un joueur de la BDD. 1=new 2=BDD : ")
            if value == "1":
                player = self.player.add_new_player()
                self.tournament.list_players.append(player)
            else:
                value = input()

    def round_1(self):

        round_1 = self.tournament.list_rounds[0]
        round_1.create_first_match()
        round_1.set_winner()
        round_1.set_ranking_points()
        round_1.last_opponent()

    def round_2(self):
        round_2 = self.tournament.list_rounds[1]
        round_2.create_matches()
        round_2.set_winner()
        round_2.set_ranking_points()
        round_2.last_opponent()

    def round_3(self):
        round_3 = self.tournament.list_rounds[2]
        round_3.create_matches()
        round_3.set_winner()
        round_3.set_ranking_points()
        round_3.last_opponent()

    def round_4(self):
        round_4 = self.tournament.list_rounds[3]
        round_4.create_matches()
        round_4.set_winner()
        round_4.set_ranking_points()
        round_4.last_opponent()

t = TournamentController()
t.start()
t.start_tournament()

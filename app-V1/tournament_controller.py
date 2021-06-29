from model.tournament import Tournament
from controller.grab import Input
from player_controller import PlayerController
from model.round import Round

class TournamentController:
    def __innit__(self):
        pass

    def run(self):
        self.add_new_tournament()

    def add_new_tournament(self):

        control_input = Input()
        model_round = Round()

        """Création des informations de base d'un tournoi"""

        #name = control_input.get_input_str("le nom")
        #place = control_input.get_input_str("la ville")
        #time_ctrl = control_input.get_rythme("le rythme de la partie Bullet = 1, Blitz = 2")
        #start_date = control_input.get_input_date("le début de tournoi")
        #end_date = control_input.get_input_date("la fin de tournoi")

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

        """
         Les joueurs sont dans le tournoi, il faut donc créer les rounds.
         - Trier les joueurs selon leur elo
         - attribuer les joueurs pour les rounds
         - création des rounds
        """
        sorted_elo = tournament.sort_elo(tournament.list_players)
        list_match = tournament.player_attribution(sorted_elo)
        round = tournament.create_rounds(list_match)
        model_round.list_round = round
        test = model_round.add_ranking_points(model_round.player_1)
        

        """
        print(tournament.name,
              tournament.place,
              tournament.time_ctrl,
              tournament.start_date,
              )"""

t = TournamentController()
t.run()

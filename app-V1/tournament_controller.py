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

        """
         Les joueurs sont dans le tournoi, il faut donc créer les rounds.
         - Trier les joueurs selon leur elo
         - attribuer les joueurs pour les rounds
         - création des rounds
        """

        sorted_elo = tournament.sort_elo(tournament.list_players)
        
        list_match_r1 = tournament.player_attribution(sorted_elo)

        round_1 = tournament.create_rounds(list_match_r1)
        # print(round_1[0], '\n',round_1[1], '\n',round_1[2], '\n',round_1[3])
        winner_round = tournament.set_ranking_points(round_1)
        for elem in tournament.list_players:
            print(elem)
        """
        Le Round est fini.
        -Savoir qui a gagné
        -Lui attribuer des points
        """
        """
        tournament.get_winner(list_match_r1)  # voir avec thim je triche je travail pas sur l'instance mais la liste
        """
        """
        Attribuer un deuxieme adversaire pour le 2 round
        - Connaitre l'ancien adversaire
        - Connaitre le nombres de poitns de tournoi
        - Attribuer les joueurs
        - Créer le Round 2
        """"""
        rework_list = tournament.rework_list(list_match_r1)
        last_opponent_r1 = tournament.last_opponent(rework_list)
        sorted_ranking = tournament.sorted_ranking_points(last_opponent_r1)
        list_match_r2 = tournament.next_player_attribution(sorted_ranking)
        round_2 = tournament.create_rounds(list_match_r2)
        # print(round_2[0], round_2[1], round_2[2], round_2[3])  voir avec thim il affiche toujours le round1
        """
        """
        Le Round 2 est fini.
        -Savoir qui a gagné
        -Lui attribuer des points
        """
        """
        tournament.get_winner(list_match_r2)
        last_opponent_r2 = tournament.last_opponent(list_match_r2)
        print(last_opponent_r2)
        """
t = TournamentController()
t.run()

from models.tournament import Tournament
from controllers.grab import Input
from player_controller import PlayerController
from views.view import View
from views.home_menu_view import HomeMenuView
from utils.menus import Menu
# from controllers.application_controller import HomeMenuController

class TournamentController:
    def __init__(self):
        self.tournament = None
        self.view = View()
        self.control_input = Input()
        self.player = PlayerController()
        self.input = Input()
        self.rounds = None
        self.menu = Menu()
        self.view_menu = HomeMenuView(self.menu)

        self.display_info = {"new_tournament": "Création d'un nouveau tournoi.\nRemplir les informations demandé.",
                             "name": "Le nom du tournoi :",
                             "location": "Le lieu du tournoi",
                             "ask_rythme": "Dans qu'elle mode de jeu, sera joué le tournoi ?\n1 = Bullet, 2 = Blitz :",
                             "rythme_bullet": "Le tournoi sera en mode Bullet, 1 minute part round !",
                             "rythme_Blitz": "Le tournoi sera en mode Blitz, 10 minutes part round !",
                             "ask_date": "Le tournoi ce déroule sur une journée ?\n 1 oui  2 non : ",
                             "date_one_day": "entrée la date du tournoi dans le format suivant '01/01/1901' :",
                             "date_start": "entrée la date de début de tournoi dans le format suivant '01/01/1901' :",
                             "date_end": "entrée la date de fin de tournoi dans le format suivant '01/01/1901' :",
                             "date_error": "la date de fin ne peut être anterieure a la date de début, nouvelle date de fin :",
                             "add_player": "Voulez vous ajouter un nouveau joueur ou un joueur de la BDD. 1=new 2=BDD :",
                             "winner_is": "Qui est le gagnant du match ?\n '1' pour le joueur 1, '2' pour le joueur 2, '0' pour match_nul :"
                             }

    def add_new_tournament(self):

        """Création des informations de base d'un tournoi"""
        """self.view.show(self.display_info["new_tournament"])
        self.view.show(self.display_info["name"])
        name = self.control_input.get_input_str()
        self.view.show(self.display_info["location"])
        location = self.control_input.get_input_str()
        self.view.show(self.display_info["ask_rythme"])
        time_ctrl = self.control_input.get_rythme()
        self.view.show(self.display_info["ask_date"])
        date = self.control_input.set_date()
        if date == '1':
            self.view.show(self.display_info["date_one_day"])
            start_date = self.control_input.get_input_date()
            end_date = start_date
        else:
            self.view.show(self.display_info["date_start"])
            start_date = self.control_input.get_input_date()

            valid_date = False
            while valid_date == False:
                self.view.show(self.display_info["date_end"])
                end_date = self.control_input.get_input_date()
                if end_date < start_date:
                    self.view.show(self.display_info["date_error"])
                    valid_date = False
                else:
                    valid_date = True"""

        self.tournament = Tournament(name="name",
                                     location="location",
                                     time_ctrl='time_ctrl',
                                     start_date='start_date',
                                     end_date='end_date'
                                     )
        # print(self.tournament)

    def add_players(self):
        """Ajout de joueurs au tournoi"""

        while len(self.tournament.list_players) != 8:
            self.view.show(self.display_info["add_player"])
            value = self.input.get_input_int()
            if value == 1:
                player = self.player.add_new_player()
                print(player)
                self.tournament.list_players.append(player)
            else:
                value = input()

    def round_initialization(self):
            self.rounds = self.tournament.create_rounds()
            if self.rounds.num_rounds == 1:
                self.rounds.create_first_match()
                self.display_matches()
            elif self.rounds.num_rounds <= 4:
                self.rounds.create_matches()
                self.display_matches()

    def display_matches(self):
        for match in self.rounds.list_matches:
            player_1 = match["Joueur 1"]
            player_2 = match["Joueur 2"]
            match_num = match['Match']
            self.view.show_matches(match_num,
                                   player_1.first_name,
                                   player_1.last_name,
                                   player_2.first_name,
                                   player_2.last_name
                                   )

    def display_ranking_points(self):
        for player in self.rounds.list_players:
            self.view.show(player)

    def set_winner(self):
        for match in self.rounds.list_matches:
            player_1 = match["Joueur 1"]
            player_2 = match["Joueur 2"]
            match_num = match['Match']
            self.view.show_players(match_num, player_1, player_2)
            self.view.show(self.display_info["winner_is"])
            value = self.input.get_input_int()
            if value == 1:
                match["winner"] = True
            elif value == 2:
                match["winner"] = False
            else:
                value == 0
                match["winner"] = None
        self.set_ranking_points()

    def set_ranking_points(self):
        for elem in self.rounds.list_matches:
            player_1 = elem["Joueur 1"]
            player_2 = elem["Joueur 2"]
            result = elem["winner"]
            if result is True:
                points = 1
                player_1.ranking_points += points
                player_1.elo += points
            elif result is False:
                points = 1
                player_2.ranking_points += points
                player_2.elo += points
            else:
                points = 0.5
                player_1.ranking_points += 0.5
                player_2.ranking_points += 0.5
                player_1.elo += points
                player_2.elo += points

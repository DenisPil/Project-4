from models.tournament import Tournament
from controllers.grab import Input
from controllers.player_controller import PlayerController
from views.view import View
from views.home_menu_view import HomeMenuView
from utils.menus import Menu
from utils.constants import PLAYER_MAX, ROUND_MAX

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

        self.display_info = {
            "new_tournament": "Création d'un nouveau tournoi.\nRemplir les informations demandé.",
            "name": "Le nom du tournoi :",
            "location": "Le lieu du tournoi",
            "ask_rythme": "Dans qu'elle mode de jeu, sera joué le tournoi ?\n1 = Bullet, 2 = Blitz :",
            "ask_date": "Le tournoi ce déroule sur une journée ?\n 1 oui  2 non : ",
            "date_one_day": "entrée la date du tournoi dans le format suivant '01/01/1901' :",
            "date_start": "entrée la date de début de tournoi dans le format suivant '01/01/1901' :",
            "date_end": "entrée la date de fin de tournoi dans le format suivant '01/01/1901' :",
            "date_error": "la date de fin ne peut être anterieure a la date de début, nouvelle date de fin :",
            "add_player": "Voulez vous ajouter un nouveau joueur ou un joueur de la BDD. 1=new 2=BDD :",
            "winner_is":
            "Qui est le gagnant du match ?\n '1' pour le joueur 1, '2' pour le joueur 2, '0' pour match_nul :",
            "check": "les informations sont elles correcte ? \n 1 pour oui, 2 pour non :",
            "invalid_info": "Qu'elles informations n'est pas valide ?",
            "info": "'1' le nom, '2' le lieu, '3' le rythme du tournoi, '4' la date",
            "database id": "Enter l'ID du joueur à ajouter",
            "error id": "L'ID rentrée n'est pas valide"
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
                                     time_ctrl="time_ctrl",
                                     start_date="start_date",
                                     end_date="end_date",
                                     )
        self.check_info_tournament()
        self.tournament.serialize()

    def check_info_tournament(self):
        self.view.show(self.tournament)
        self.view.show(self.display_info["check"])
        valid_info = self.input.get_input_int()
        if valid_info == 1:
            pass
        if valid_info == 2:
            self.view.show(self.display_info["invalid_info"])
            self.view.show(self.display_info["info"])
            info = self.input.get_input_int()
            if info == 1:
                self.view.show(self.display_info["name"])
                self.tournament.name = self.input.get_input_str()
            elif info == 2:
                self.view.show(self.display_info["location"])
                self.tournament.location = self.input.get_input_str()
            elif info == 3:
                self.view.show(self.display_info["ask_rythme"])
                self.tournament.time_ctrl = self.input.get_gender()
            elif info == 4:
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
                            valid_date = True

    def add_players(self):
        """Ajout de joueurs au tournoi"""

        while len(self.tournament.list_players) != PLAYER_MAX:
            self.view.show(self.display_info["add_player"])
            value = self.input.get_input_int()
            if value == 1:
                player = self.player.add_new_player()
                self.view.show(player)
                self.tournament.list_players.append(player)
            elif value == 2:
                self.view.show(self.display_info["database id"])
                while True:
                    try:
                        player_id = self.input.get_input_int()
                        player = self.player.add_database_player(player_id)
                        self.view.show(player)
                        self.tournament.list_players.append(player)
                    except TypeError:
                        self.view.show(self.display_info["error id"])
            else:
                value = input()
        self.tournament.serialize_list_of_players()
        self.tournament.serialize()

    def round_initialization(self):

        self.rounds = self.tournament.create_rounds()
        if self.rounds.num_rounds == 1:
            self.rounds.create_first_match()
            self.rounds.serialize_list_of_matches_and_rounds()
            self.tournament.serialize_list_of_rounds()
            self.display_matches()
        elif self.rounds.num_rounds <= ROUND_MAX:
            self.rounds.create_matches()
            self.display_matches()

    def display_matches(self):
        for match in self.rounds.list_matches:
            player_1 = match["Joueur 1"]
            player_2 = match["Joueur 2"]
            match_num = match["Match"]
            self.view.show_matches(
                match_num,
                player_1.first_name,
                player_1.last_name,
                player_2.first_name,
                player_2.last_name,
            )

    def display_ranking_points(self):
        for player in self.rounds.list_players:
            self.view.show(player)

    def set_winner(self):
        for match in self.rounds.list_matches:
            player_1 = match["Joueur 1"]
            player_2 = match["Joueur 2"]
            match_num = match["Match"]
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

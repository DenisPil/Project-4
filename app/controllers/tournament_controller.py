from models.tournament import Tournament
from controllers.grab import Input
from controllers.player_controller import PlayerController
from views.view import View
from views.home_menu_view import HomeMenuView
from utils.menus import Menu
from utils.constants import PLAYER_MAX, ROUND_MAX


class TournamentController:

    """
        Création de l'instance du tournoi.
    """

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
            "ask_rythme": "Dans qu'elle mode de jeu, sera joué le tournoi ?\n1 = Bullet, 2 = Blitz, 3 = Rapide :",
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
            "error id": "L'ID rentrée n'est pas valide",
            "select_tournament": "Plus de détail entrer le nom du tournoi :"
        }

    def create_tournament(self):

        """
            Méthode qui va créer le tournoi. L'utilisateur rentre les informations
            de base du tournoi.
        """

        self.view.show(self.display_info["new_tournament"])
        self.view.show(self.display_info["name"])
        name = self.control_input.get_input_str()
        self.view.show(self.display_info["location"])
        location = self.control_input.get_input_str()
        self.view.show(self.display_info["ask_rythme"])
        time_ctrl = self.control_input.get_rythme()
        self.view.show(self.display_info["ask_date"])
        date = self.control_input.get_input_int()
        if date == 1:
            self.view.show(self.display_info["date_one_day"])
            start_date = self.control_input.get_input_date()
            end_date = start_date
        else:
            self.view.show(self.display_info["date_start"])
            start_date = self.control_input.get_input_date()
            self.view.show(self.display_info["date_end"])
            end_date = self.control_input.get_input_date()
            if end_date < start_date:
                self.view.show(self.display_info["date_error"])
                end_date = self.control_input.get_input_date()

        self.tournament = Tournament(name=name,
                                     location=location,
                                     time_ctrl=time_ctrl,
                                     start_date=str(start_date),
                                     end_date=str(end_date),
                                     list_rounds=list(),
                                     list_players=list()
                                     )

        self.check_info_tournament()
        self.tournament.serialize()

    def check_info_tournament(self):

        """
            Méthode qui affiche les attributs d'un tournoi pour que l'utilisateur les valides
            ou les modifies au besoin.
        """

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
                date = self.control_input.get_input_int()
                if date == 1:
                    self.view.show(self.display_info["date_one_day"])
                    start_date = self.control_input.get_input_date()
                    end_date = start_date
            else:
                self.view.show(self.display_info["date_start"])
                start_date = self.control_input.get_input_date()
                self.view.show(self.display_info["date_end"])
                end_date = self.control_input.get_input_date()
                if end_date < start_date:
                    self.view.show(self.display_info["date_error"])
                    end_date = self.control_input.get_input_date()
            self.tournament.serialize()

    def add_players(self):

        """
            Méthode qui ajoute des joueurs au tournoi.
            Il est demandé a l'utilisateur si il souhaite ajouter un joueur
            a partir de la base de donnée ou créer un nouveau joueur.
        """
        while len(self.tournament.list_players) != PLAYER_MAX:
            self.view.show(self.display_info["add_player"])
            value = self.input.get_input_int()
            if value == 1:
                player = self.player.add_new_player()
                self.view.show(player)
                self.tournament.list_players.append(player)
            elif value == 2:
                self.view.show(self.display_info["database id"])
                player_id = self.input.get_input_int()
                player = self.player.add_database_player(player_id)
                player.ranking_points = 0
                self.view.show(player)
                self.tournament.list_players.append(player)
            else:
                value = input()
        self.tournament.serialize()

    def round_initialization(self):

        """
            Méthode qui innitialise la création des rounds et des matches.
        """

        self.rounds = self.tournament.create_rounds()
        if self.rounds.num_rounds == 1:
            self.rounds.create_first_match()
            self.rounds.start_time = self.rounds.set_time()
            self.tournament.serialize()
            self.display_matches()
        elif self.rounds.num_rounds <= ROUND_MAX:
            self.rounds.create_matches()
            self.rounds.start_time = self.rounds.set_time()
            self.tournament.serialize()
            self.display_matches()

    def display_matches(self):

        """
            Méthode qui affiche les matches d'un round
        """

        for match in self.rounds.list_matches:
            player_1 = match["Joueur 1"]
            player_2 = match["Joueur 2"]
            match_num = match["Match"]
            self.view.show_matches(match_num, player_1, player_2)

    def display_ranking_points(self):

        """
            Méthode qui permet d'afficher la liste des joueurs
            en fonction de leur points de tournoi
        """

        for player in self.rounds.list_players:
            self.view.show(player)

    def set_winner(self):

        """
            Méthode qui permet de selectionner le joueur gagnant
            à la fin d'un match
        """

        self.rounds.end_time = self.rounds.set_time()
        for match in self.rounds.list_matches:
            player_1 = match["Joueur 1"]
            player_2 = match["Joueur 2"]
            match_num = match["Match"]
            self.view.show_matches(match_num, player_1, player_2)
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
        self.tournament.serialize()

    def set_ranking_points(self):

        """
            Méthode qui permet d'attribuer les points de tournoi
            à la fin d'un round.
        """

        for elem in self.rounds.list_matches:
            player_1 = elem["Joueur 1"]
            player_2 = elem["Joueur 2"]
            result = elem["winner"]
            if result is True:
                points = 1
                player_1.ranking_points += points
                player_1.elo += points
                elem["winner"] = "Joueur 1"
                player_1.serialize()
            elif result is False:
                points = 1
                player_2.ranking_points += points
                player_2.elo += points
                elem["winner"] = "Joueur 2"
                player_2.serialize()
            else:
                points = 0.5
                player_1.ranking_points += 0.5
                player_2.ranking_points += 0.5
                player_1.elo += points
                player_2.elo += points
                elem["winner"] = "Match nul"
                player_1.serialize()
                player_2.serialize()

    def deserialize_tournament(self):

        """
            Méthode qui permet de créer les instances des tournois
            à partir de la liste des tournois serialisés.
            Renvoie une liste d'instances de tournoi.
        """

        list_tournament = Tournament().serialized_tournament_list()
        all_tournament = list()
        for elem in list_tournament:
            tournament = Tournament(name=elem['nom'],
                                    location=elem['lieu'],
                                    time_ctrl=elem['rythme'],
                                    start_date=elem['date de debut'],
                                    end_date=elem['date de fin'],
                                    list_rounds=elem['liste des rounds'],
                                    list_players=elem['liste des joueurs'])
            all_tournament.append(tournament)
        return all_tournament

    def display_tournament_from_database(self):

        """
            Méthode qui permet d'afficher la liste des tournois
            avec les informations de base.
        """

        for tournament in self.deserialize_tournament():
            self.view.show_tournament(name=tournament.name,
                                      location=tournament.location,
                                      start_date=tournament.start_date,
                                      end_date=tournament.end_date,
                                      time_ctrl=tournament.time_ctrl,
                                      )
        self.view.show(self.display_info['select_tournament'])
        self.select_tournament()

    def select_tournament(self):

        """
            Méthode qui permet de selectionner un tournoi
            à partir de la liste de tournoi déjà instanciés.
            Compléte les informations de base avec les instances
            de joueurs et des rounds.
        """

        list_tournament = self.deserialize_tournament()
        select_tournament = self.input.get_input_str()
        for tournament in list_tournament:
            if select_tournament == tournament.name:
                self.tournament = tournament
                self.tournament.list_players = self.player.deserialize__players_from_tournament(tournament.list_players)
                rounds_instance_list = self.tournament.deserialize_rounds_from_database(players=tournament.list_players)
                self.tournament.list_rounds = rounds_instance_list

    def display_info_tournament_rounds(self):

        """
            Méthode qui permet d'afficher les rounds archivés.
        """

        for round in self.tournament.list_rounds:
            self.view.show(("\n" + "Round n°" + str(round.num_rounds) + "\n"))
            for match in round.list_matches:
                winner = match["winner"]
                player_1 = match["Joueur 1"]
                player_2 = match["Joueur 2"]
                match_num = match["Match"]
                self.view.show_archived_matches(match_num, player_1, player_2, winner)

    def display_info_tournament_players(self):

        """
            Méthode qui affiche les joueurs d'un tournoi archivé.
        """

        for player in self.tournament.list_players:
            self.view.show(player)

    def unfinished_tournament(self):

        """
            Méthode qui permet de finir un tournoi archivé
            mais innachevé.
            Renvoie un booléen sur le statut du tournoi.
        """

        tournament_status = False
        if len(self.tournament.list_rounds) < ROUND_MAX:
            tournament_status = True
        return tournament_status

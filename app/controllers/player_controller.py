from models.player import Player
from controllers.grab import Input
from views.view import View
from views.home_menu_view import HomeMenuView
from utils.menus import Menu


class PlayerController:

    """
        Création de l'instance d'un joueur.
    """

    def __init__(self):
        self.player = None
        self.view = View()
        self.input = Input()
        self.menu = Menu()
        self.viewmenu = HomeMenuView(self.menu)

        self.display_information = {"first_name": "Le prénom du joueur :",
                                    "last_name": "Le nom :",
                                    "gender": "Le genre ? 'H' si c'est un homme, 'F' si c'est une femme :",
                                    "elo": "les points ELO du joueur :",
                                    "birthday": "Veuillez saisir la date de naissance dans le format 01/01/1901",
                                    "check": "les informations sont elles correcte ? \n 1 pour oui, 2 pour non :",
                                    "invalid_info": "Qu'elles informations n'est pas valide ?",
                                    "info": "'1' le prénom, '2' le nom, '3' le genre, '4' l'anniverssaire, '5' l'elo "
                                    }

    def add_new_player(self):

        """
            Méthode qui demande a l'utilisateur de rentrer les informations d'un joueur lors de ça création.
            Renvoie une instance de joueur.
        """

        """self.view.show(self.display_information["first_name"])
        first_name = self.input.get_input_str()
        self.view.show(self.display_information["last_name"])
        last_name = self.input.get_input_str()
        self.view.show(self.display_information["gender"])
        gender = self.input.get_gender()
        self.view.show(self.display_information["elo"])
        elo = self.input.get_input_int()
        self.view.show(self.display_information["birthday"])
        birthday = self.input.get_input_date()"""

        self.player = Player(first_name="first_name",
                             last_name="last_name",
                             gender="gender",
                             elo=Player.player_id,
                             ranking_points=0,
                             birthday="birthday",
                             ID=Player.player_id
                             )
        Player.player_id += 1
        self.check_player_info()
        self.player.serialize()
        return self.player

    def add_database_player(self, player_id):

        """
            Méthode qui récupére l'ID d'un joueur, pour créer une instance de joueur a partir de la base de donnée.
            Cette méthode est utiliser pour ajouter un joueur a un tournoi.
            Renvoie une instance de joueur.

            Argument:
                player_id = L'id du joueur qui correspond a son doc_id de la base de donnée.
        """

        player = Player().add_player_from_database(doc_id=player_id)
        return player

    def check_player_info(self):

        """
            Méthode qui affiche les attributs d'un joueur pour que l'utilisateur les valides
            ou les modifies au besoin.
        """

        self.view.check_info_player(ID=self.player.ID,
                                    first_name=self.player.first_name,
                                    last_name=self.player.last_name,
                                    gender=self.player.gender,
                                    birthday=self.player.birthday,
                                    elo=self.player.elo,
                                    )

        self.view.show(self.display_information["check"])
        valid_info = self.input.get_input_int()
        if valid_info == 1:
            pass
        if valid_info == 2:
            self.view.show(self.display_information["invalid_info"])
            self.view.show(self.display_information["info"])
            info = self.input.get_input_int()
            if info == 1:
                self.view.show(self.display_information["first_name"])
                self.player.first_name = self.input.get_input_str()
            elif info == 2:
                self.view.show(self.display_information["last_name"])
                self.player.last_name = self.input.get_input_str()
            elif info == 3:
                self.view.show(self.display_information["gender"])
                self.player.gender = self.input.get_gender()
            elif info == 4:
                self.view.show(self.display_information["birthday"])
                self.player.birthday = self.input.get_input_date()
            elif info == 5:
                self.view.show(self.display_information["elo"])
                self.player.elo = self.input.get_input_int()

    def display_players_from_database(self):

        """
            Méthode qui affiche la liste de tous les joueurs de la base de donnée.
        """

        for player in Player().deserialize_players_in_database():
            self.view.check_info_player(ID=player.ID,
                                        first_name=player.first_name,
                                        last_name=player.last_name,
                                        gender=player.gender,
                                        birthday=player.birthday,
                                        elo=player.elo,
                                        )

    def deserialize__players_from_tournament(self, player_list):

        """
            Méthode qui créer les instances de joueurs d'un tournoi a partir de la liste
            de joueurs serialisées du tournoi.
            Renvoie une liste d'instances de joueurs

            Argument:
                player_list = liste des joueurs serialisés d'un tournoi
        """

        all_player_instance = list()
        for elem in player_list:
            player = Player(ID=elem['ID'],
                            first_name=elem['prenom'],
                            last_name=elem['nom'],
                            gender=elem['genre'],
                            birthday=elem['anniversaire'],
                            elo=elem['ELO'],
                            ranking_points=elem['points de tournoi']
                            )
            all_player_instance.append(player)
        return all_player_instance

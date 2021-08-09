from views.home_menu_view import HomeMenuView
from utils.menus import Menu
from controllers.player_controller import PlayerController
from controllers.tournament_controller import TournamentController
from utils.constants import ROUND_MAX


class ApplicationController:

    """
        Controleur principale de l'application qui déclenche toutes les étapes
    """

    def __init__(self):
        self.controller = None

    def start(self):
        """
         Méthode qui gére la navigation dans le menu.
         Créer l'instance de mes controlleurs en "cascade".
        """
        self.controller = HomeMenuController()
        while self.controller:
            self.controller = self.controller()


class HomeMenuController:

    """
        Affiche le menu principale et demande à l'utilisateur de choisir une option
    """

    def __init__(self):
        self.menu = Menu()
        self.view = HomeMenuView(self.menu)

    def __call__(self):

        """
            Méthode qui ajoute les entrées au menu de cette classe.
            Affiche le menu et demande à l'utilisateur de choisir une option.
            Renvoie l'instance du controlleur choisi par l'utilisateur
        """

        self.menu.header("_________________________________", "")
        self.menu.header("Menu", "Principal")
        self.menu.add("auto", "Création d'un tournoi.", CreateTournamentMenuController)
        self.menu.add("auto", "Ajouter des joueurs", AddPlayerMenuController)
        self.menu.add("auto", "Archive", ArchiveMenuController)
        # Demander a la vue d'afficher le menu et de récup la réponse
        user_choice = self.view.get_user_choice()
        # retourner le controller associé au choix de l'utilisateur au controleur principal
        return user_choice.handler


class CreateTournamentMenuController:

    """
        Controlleur du menu de création de tournoi.
    """

    tournament_controller = TournamentController()
    player_controller = PlayerController()

    def __init__(self):
        self.menu = Menu()
        self.view = HomeMenuView(self.menu)

    def __call__(self):

        """
            Méthode qui ajoute les entrées au menu de cette classe.
            Affiche le menu et demande à l'utilisateur de choisir une option.
            Renvoie l'instance du controlleur choisi par l'utilisateur
        """

        self.menu.header("_________________________________", "")
        self.menu.header("Menu", "Nouveau tournoi:")
        self.menu.add("auto", "créer un nouveau tournoi", NewTournamentController)
        self.menu.add("auto", "Retour Menu principal", HomeMenuController)

        user_choice = self.view.get_user_choice()
        return user_choice.handler


class NewTournamentController:

    """
        Controlleur de création de tournoi.
    """

    def __init__(self):
        self.menu = Menu()
        self.view = HomeMenuView(self.menu)
        self.tournament_controller = CreateTournamentMenuController.tournament_controller

    def __call__(self):

        """
            Méthode qui ajoute les entrées au menu de cette classe.
            Affiche le menu et demande à l'utilisateur de choisir une option.
            Renvoie l'instance du controlleur choisi par l'utilisateur
        """

        self.tournament_controller.create_tournament()
        self.menu.header("_________________________________", "")
        self.menu.header("Menu du tournoi :", self.tournament_controller.tournament.name)
        self.menu.add("auto", "Ajouter des joueurs au tournoi", AddPlayerInTournamentController)
        self.menu.add("auto", "Retour Menu principal", HomeMenuController)
        user_choice = self.view.get_user_choice()
        return user_choice.handler


class StartRoundController:

    """
        Controlleur qui innitialse les rounds.
    """

    def __init__(self):
        self.menu = Menu()
        self.view = HomeMenuView(self.menu)
        self.tournament_controller = CreateTournamentMenuController.tournament_controller
        self.num_round = self.tournament_controller.tournament.num_rounds

    def __call__(self):

        """
            Méthode qui ajoute les entrées au menu de cette classe.
            Affiche le menu et demande à l'utilisateur de choisir une option.
            Renvoie l'instance du controlleur choisi par l'utilisateur
        """

        self.tournament_controller.round_initialization()
        self.menu.header("_________________________________", "")
        self.menu.header("Tournoi :", self.tournament_controller.tournament.name)
        self.menu.header("Numéro du round ", self.num_round)
        self.menu.add("auto", "Fin de Round rentrer les résultats", SetWinnerMatchController)
        self.menu.add("auto", "Retour au menu.", HomeMenuController)
        user_choice = self.view.get_user_choice()
        return user_choice.handler


class AddPlayerInTournamentController:

    """
        Controlleur qui ajoute des joueurs pour un tournoi.
    """

    def __init__(self):
        self.menu = Menu()
        self.view = HomeMenuView(self.menu)
        self.tournament = CreateTournamentMenuController.tournament_controller

    def __call__(self):

        """
            Méthode qui ajoute les entrées au menu de cette classe.
            Affiche le menu et demande à l'utilisateur de choisir une option.
            Renvoie l'instance du controlleur choisi par l'utilisateur
        """

        self.tournament.add_players()
        self.menu.header("_________________________________", "")
        self.menu.header("Menu", "Nouveau Joueur")
        self.menu.add("auto", "Commencer le tournoi", StartRoundController)
        self.menu.add("auto", "Retour au menu.", HomeMenuController)
        user_choice = self.view.get_user_choice()
        return user_choice.handler


class SetWinnerMatchController:

    """
        Controlleur qui a la fin d'un round demande a l'utilisateur de saisir le gagnant des matches.
        Il controlle l'état du tournoi pour savoir si le dernier round à était jouer ou non.
    """

    def __init__(self):
        self.menu = Menu()
        self.view = HomeMenuView(self.menu)
        self.tournament_controller = CreateTournamentMenuController.tournament_controller
        self.num_round = self.tournament_controller.tournament.num_rounds

    def __call__(self):

        """
            Méthode qui ajoute les entrées au menu de cette classe.
            Les entrées sont différente selon l'avancé du tournoi.
            Affiche le menu et demande à l'utilisateur de choisir une option.
            Renvoie l'instance du controlleur choisi par l'utilisateur
        """

        if self.num_round <= ROUND_MAX:
            self.tournament_controller.set_winner()
            self.menu.header("_________________________________", "")
            self.menu.header("Résultat du Tournoi :", self.tournament_controller.tournament.name)
            self.menu.add("auto", "Commencer le prochain Round", StartRoundController)
            self.menu.add("auto", "Afficher les resultats!", DisplayRankingPointsController)
            self.menu.add("auto", "Retour au menu.", HomeMenuController)
            user_choice = self.view.get_user_choice()
            return user_choice.handler
        elif self.num_round > ROUND_MAX:
            self.tournament_controller.set_winner()
            self.menu.header("_________________________________", "")
            self.menu.header("Fin du Tournoi :", self.tournament_controller.tournament.name)
            self.menu.add("auto", "Afficher le résultat final !", DisplayEndTournamentController)
            self.menu.add("auto", "Retour au menu.", HomeMenuController)
            user_choice = self.view.get_user_choice()
            return user_choice.handler


class AddPlayerMenuController:

    """
        Controlleur du menu qui permet d'ajouter des joueurs a la base de donné.
    """

    def __init__(self):
        self.menu = Menu()
        self.view = HomeMenuView(self.menu)

    def __call__(self):

        """
            Méthode qui ajoute les entrées au menu de cette classe.
            Affiche le menu et demande à l'utilisateur de choisir une option.
            Renvoie l'instance du controlleur choisi par l'utilisateur
        """

        self.menu.header("_________________________________", "")
        self.menu.header("Menu", "Nouveau Joueur")
        self.menu.add("auto", "Ajouter de joueur.", AddPlayerController)
        self.menu.add("auto", "Retour au menu.", HomeMenuController)
        user_choice = self.view.get_user_choice()
        return user_choice.handler


class AddPlayerController:

    """
        Controlleur qui ajoute des joueurs a la base de donnée
    """

    def __init__(self):
        self.menu = Menu()
        self.view = HomeMenuView(self.menu)
        self.players = CreateTournamentMenuController.player_controller

    def __call__(self):

        """
            Méthode qui ajoute les entrées au menu de cette classe.
            Affiche le menu et demande à l'utilisateur de choisir une option.
            Renvoie l'instance du controlleur choisi par l'utilisateur
        """

        self.players.add_new_player()
        self.menu.header("_________________________________", "")
        self.menu.add("auto", "Ajouter de joueur.", AddPlayerController)
        self.menu.add("auto", "Retour au menu.", HomeMenuController)
        user_choice = self.view.get_user_choice()
        return user_choice.handler


class DisplayRankingPointsController:

    """
        Controlleur qui affiche le classement des joueurs dans un tournoi.
    """

    def __init__(self):
        self.menu = Menu()
        self.view = HomeMenuView(self.menu)
        self.tournament_controller = CreateTournamentMenuController.tournament_controller

    def __call__(self):

        """
            Méthode qui ajoute les entrées au menu de cette classe.
            Affiche le menu et demande à l'utilisateur de choisir une option.
            Renvoie l'instance du controlleur choisi par l'utilisateur
        """

        self.tournament_controller.display_ranking_points()
        self.menu.header("_________________________________", "")
        self.menu.header("Menu", "Classement des Joueurs")
        self.menu.add("auto", "Commencer le prochain Round", StartRoundController)
        self.menu.add("auto", "Retour au menu.", HomeMenuController)
        user_choice = self.view.get_user_choice()
        return user_choice.handler


class DisplayEndTournamentController:

    """
        Controlleur qui permet d'afficher le classement final d'un tournoi.
    """

    def __init__(self):
        self.menu = Menu()
        self.view = HomeMenuView(self.menu)
        self.tournament_controller = CreateTournamentMenuController.tournament_controller

    def __call__(self):

        """
            Méthode qui ajoute les entrées au menu de cette classe.
            Affiche le menu et demande à l'utilisateur de choisir une option.
            Renvoie l'instance du controlleur choisi par l'utilisateur
        """

        self.tournament_controller.display_ranking_points()
        self.menu.header("_________________________________", "")
        self.menu.header("Menu", "Classement final des Joueurs")
        self.menu.add("auto", "Retour au menu.", HomeMenuController)
        user_choice = self.view.get_user_choice()
        return user_choice.handler


class ArchiveMenuController:

    """
        Controlleur du menu archive.
    """

    def __init__(self):
        self.menu = Menu()
        self.view = HomeMenuView(self.menu)

    def __call__(self):

        """
            Méthode qui ajoute les entrées au menu de cette classe.
            Affiche le menu et demande à l'utilisateur de choisir une option.
            Renvoie l'instance du controlleur choisi par l'utilisateur
        """

        self.menu.header("_________________________________", "")
        self.menu.header("Menu", "Archive")
        self.menu.add("auto", "Liste des joueurs.", ArchivePlayersController)
        self.menu.add("auto", "Liste des tournois.", ArchiveTournamentController)
        self.menu.add("auto", "Retour au menu.", HomeMenuController)
        user_choice = self.view.get_user_choice()
        return user_choice.handler


class ArchivePlayersController:

    """
        Controlleur qui permet d'afficher tous les joueurs contenue dans la base de donnée.
    """

    def __init__(self):
        self.menu = Menu()
        self.view = HomeMenuView(self.menu)
        self.player_controller = CreateTournamentMenuController.player_controller

    def __call__(self):

        """
            Méthode qui ajoute les entrées au menu de cette classe.
            Affiche le menu et demande à l'utilisateur de choisir une option.
            Renvoie l'instance du controlleur choisi par l'utilisateur
        """

        self.player_controller.display_players_from_database()
        self.menu.header("_________________________________", "")
        self.menu.header("Menu", "Archive : Liste des joueurs dans la base de donnée")
        self.menu.add("auto", "Retour au menu.", HomeMenuController)
        user_choice = self.view.get_user_choice()
        return user_choice.handler


class ArchiveTournamentController:

    """
        Controlleur qui permet d'afficher tous les tournois contenue dans la base de donnée.
    """

    def __init__(self):
        self.menu = Menu()
        self.view = HomeMenuView(self.menu)
        self.tournament_controller = CreateTournamentMenuController.tournament_controller

    def __call__(self):

        """
            Méthode qui ajoute les entrées au menu de cette classe.
            Affiche le menu et demande à l'utilisateur de choisir une option.
            Renvoie l'instance du controlleur choisi par l'utilisateur
        """

        self.tournament_controller.display_tournament_from_database()
        self.menu.header("_________________________________", "")
        self.menu.header("Archive : Info complémentaire du tournoi: ", self.tournament_controller.tournament.name)
        self.menu.add("auto", "Finir le tournoi.", UnfinishedTournamentController)
        self.menu.add("auto", "Liste des joueurs.", ArchiveTournamentShowPlayersController)
        self.menu.add("auto", "Liste des rounds.", ArchiveTournamentShowRoundsController)
        self.menu.add("auto", "Retour au menu.", HomeMenuController)
        user_choice = self.view.get_user_choice()
        return user_choice.handler


class ArchiveTournamentShowPlayersController:

    """
        Controlleur qui permet d'afficher les joueurs d'un tournoi contenue dans la base de donnée.
    """

    def __init__(self):
        self.menu = Menu()
        self.view = HomeMenuView(self.menu)
        self.tournament_controller = CreateTournamentMenuController.tournament_controller

    def __call__(self):

        """
            Méthode qui ajoute les entrées au menu de cette classe.
            Affiche le menu et demande à l'utilisateur de choisir une option.
            Renvoie l'instance du controlleur choisi par l'utilisateur
        """

        self.tournament_controller.display_info_tournament_players()
        self.menu.header("_________________________________", "")
        self.menu.header("Archive : Liste des joueurs du tournoi : ", self.tournament_controller.tournament.name)
        self.menu.add("auto", "Liste des rounds.", ArchiveTournamentShowRoundsController)
        self.menu.add("auto", "Retour liste des tournois.", ArchiveTournamentController)
        self.menu.add("auto", "Retour au menu.", HomeMenuController)
        user_choice = self.view.get_user_choice()
        return user_choice.handler


class ArchiveTournamentShowRoundsController:

    """
        Controlleur qui permet d'afficher les rounds et matches d'un tournoi contenue dans la base de donnée.
    """

    def __init__(self):
        self.menu = Menu()
        self.view = HomeMenuView(self.menu)
        self.tournament_controller = CreateTournamentMenuController.tournament_controller

    def __call__(self):

        """
            Méthode qui ajoute les entrées au menu de cette classe.
            Affiche le menu et demande à l'utilisateur de choisir une option.
            Renvoie l'instance du controlleur choisi par l'utilisateur
        """

        self.tournament_controller.display_info_tournament_rounds()
        self.menu.header("_________________________________", "")
        self.menu.header("Archive : Liste des rounds du tournoi : ", self.tournament_controller.tournament.name)
        self.menu.add("auto", "Liste des joueurs.", ArchiveTournamentShowPlayersController)
        self.menu.add("auto", "Retour liste des tournois.", ArchiveTournamentController)
        self.menu.add("auto", "Finir le tournoi.", UnfinishedTournamentController)
        self.menu.add("auto", "Retour au menu.", HomeMenuController)
        user_choice = self.view.get_user_choice()
        return user_choice.handler


class UnfinishedTournamentController:

    """
        Controlleur qui permet de finir un tournoi enregistrer dans la base de donnée,
        si le tournoi n'est pas fini.
    """

    def __init__(self):
        self.menu = Menu()
        self.view = HomeMenuView(self.menu)
        self.tournament_controller = CreateTournamentMenuController.tournament_controller

    def __call__(self):

        """
            Méthode qui ajoute les entrées au menu de cette classe.
            L'affichage évolue en fonction de l'état du tournoi (si il est fini ou non)
            Affiche le menu et demande à l'utilisateur de choisir une option.
            Renvoie l'instance du controlleur choisi par l'utilisateur
        """

        unfinishe = self.tournament_controller.unfinished_tournament()
        if unfinishe is True:
            self.menu.header("_________________________________", "")
            self.menu.header("Menu : Rerprise du tournoi : ", self.tournament_controller.tournament.name)
            self.menu.add("auto", "reprendre.", StartRoundController)
            self.menu.add("auto", "Retour au menu.", HomeMenuController)
            user_choice = self.view.get_user_choice()
            return user_choice.handler
        elif unfinishe is False:
            self.menu.header("_________________________________", "")
            self.menu.header("Menu : Tournoi fini impossible de continuer", self.tournament_controller.tournament.name)
            self.menu.add("auto", "Retour liste des tournois.", ArchiveTournamentController)
            self.menu.add("auto", "Retour au menu.", HomeMenuController)
            user_choice = self.view.get_user_choice()
            return user_choice.handler

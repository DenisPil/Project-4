from views.home_menu_view import HomeMenuView
from utils.menus import Menu

class ApplicationController:
    """
    self.controller : le controlleur courant de navigation
    """
    def __init__(self):
        self.controller = None

    def start(self):
        """
        Gére la navigation dans le menu
        """
        self.controller = HomeMenuController()
        while self.controller:
            self.controller = self.controller()


class HomeMenuController:

    """
    Ajoute les entrées au menu de cette classe.
    Affiche le menu et demande à l'utilisateur de choisir une option
    """

    def __init__(self):
        self.menu = Menu()
        self.view = HomeMenuView(self.menu)

    def __call__(self):
        # 1. construire un menu
        # ("auto"=la clés, "Ajout de nouveaux joueurs"= l'option, 
        # lié a la clé, et le controlleur associée a l'option)
        self.menu.header("Menu", "Principal")
        self.menu.add("auto", "Création d'un tournoi.", NewTournamentMenuController)
        self.menu.add("auto", "Ajouter des joueurs", AddPlayerMenuController)

        user_choice = self.view.get_user_choice()
        return user_choice.handler


class NewTournamentMenuController:

        def __init__(self):
            self.menu = Menu()
            self.view = HomeMenuView(self.menu)

        def __call__(self):
            self.menu.header("Menu", "Nouveau tournoi:")
            self.menu.add("auto", "Ajouter des joueurs", AddPlayerMenuController) 
            self.menu.add("auto", "Retour Menu principal", HomeMenuController)

            user_choice = self.view.get_user_choice()
            return user_choice.handler

class AddPlayerMenuController:
    
    def __init__(self):
        self.menu = Menu()
        self.view = HomeMenuView(self.menu)
        
    def __call__(self):
        self.menu.header("Menu", "Nouveau Joueur")
        self.menu.add("auto", "Ajout de joueur.", AddPlayerController())
        self.menu.add("auto", "Retour au menu.", HomeMenuController())
        # 2. Demander a la vue d'afficher le menu et de récup la réponse
        user_choice = self.view.get_user_choice()
        # 3. retourner le controller associé au choix de l'utilisateur au controleur principal
        return user_choice.handler

class AddPlayerController:

    def __init__(self):
        self.menu = Menu()
        self.view = HomeMenuView(self.menu)
        
    def __call__(self):
        pass


t = ApplicationController()
t.start()
from models.player import Player
from controllers.grab import Input
from views.view import View
from views.home_menu_view import HomeMenuView
from utils.menus import Menu



class PlayerController:
    def __init__(self):
        self.player = None
        self.view = View()
        self.input = Input()
        self.menu = Menu()
        self.view = HomeMenuView(self.menu)

        self.display_information = {"first_name": "Le prénom du joueur :",
                                    "last_name": "Le nom :",
                                    "gender": "Le genre ? 'H' si c'est un homme, 'F' si c'est une femme :",
                                    "elo": "les points ELO du joueur :",
                                    "birthday": "Veuillez saisir la date de naissance dans le format 01/01/1901"
                                    }

        """    def __call__(self):
        # 1. construire un menu
        # ("auto"=la clés, "Ajout de nouveaux joueurs"= l'option, 
        # lié a la clé, et le controlleur associée a l'option)
        self.menu.header("Menu", "ajout de jouuerr r")
        self.menu.add("auto", "ajout joueur.", self.add_new_player())
        self.menu.add("auto", "retour menu", self.view)

        user_choice = self.view.get_user_choice()
        return user_choice.handler"""

    def add_new_player(self):

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

        self.player = Player(first_name="",
                             last_name=Player.player_id,
                             gender="genre",
                             elo=Player.player_id,
                             ranking_points=0,
                             birthday="birthday"
                             )

        return self.player

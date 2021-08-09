from controllers.grab import Input


class HomeMenuView:

    """
        Classe qui affiche le menu.
    """

    def __init__(self, menu):
        self.menu = menu
        self.input = Input()

    def display_menu(self):

        """
            Méthode qui permet d'afficher des entrées du menu.
        """

        for key, entry in self.menu.items():
            print(f"{key} : {entry} ")
        print("")

    def get_user_choice(self):

        """
            Méthode qui demande à l'utilisateur de choisir un menu.
            Renvoie une instance d'objet qui est une entrée de menu désignée par choice.
        """
        while True:
            self.display_menu()
            choice = self.input.get_input_str()
            if choice in self.menu:
                return self.menu[choice]

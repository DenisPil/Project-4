from controllers.grab import Input


class HomeMenuView:

    def __init__(self, menu):
        self.menu = menu
        self.input = Input()

    def display_menu(self):
        for key, entry in self.menu.items():
            print(f"{key} : {entry} ")
        print("")

    def get_user_choice(self):

        while True:
            # afficher le menu à l'utilisateur
            self.display_menu()
            # delander à l'utilisateur de faire un choix
            choice = self.input.get_input_str()
            # valider  de l'utilisateur
            if choice in self.menu:
                # retourner le choix de l'utilisateur
                return self.menu[choice]

    def show(self, info):
        print(info)
import datetime
from views.view import View


class Input:

    """
        Classe qui gère toutes les entrées utilisateur.
    """

    def __init__(self):
        self.view = View()
        self.display_info = {"error date": "La date n'est pas valide :",
                             "error": "L'information n'est pas valide :"
                             }

    def get_input_str(self):

        """
            Méthode qui gère toutes les valeurs de type 'str' demandées à l'utilisateur.
            Renvoie une valeur de type 'str'.
        """

        while True:
            try:
                value = str(input("-->"))
                break
            except ValueError:
                self.view.show(self.display_info["error"])
        return value.capitalize()

    def get_input_int(self):

        """
            Méthode qui gère toutes les valeurs de type 'int' demandées à l'utilisateur.
            Renvoie une valeur de type 'int'.
        """

        while True:
            try:
                value = int(input("-->"))
                break
            except ValueError:
                self.view.show(self.display_info["error"])
        return value

    def get_input_date(self):

        """
            Méthode qui gère toutes les valeurs de type 'date' demandées à l'utilisateur.
            Renvoie une valeur de type 'date'.
        """

        while True:
            try:
                value = str(input("-->"))
                datetime.datetime.strptime(value, '%d/%m/%Y')
                break
            except ValueError:
                self.view.show(self.display_info["error date"])
        return value

    def get_gender(self):

        """
            Méthode qui permet de choisir le genre d'un joueur.
            Renvoie une valeur avec le genre du joueur.
        """

        while True:
            try:
                value = input("-->")
                if value.lower() == "h":
                    value = "Homme"
                    break
                elif value.lower() == "f":
                    value = "Femme"
                    break
            except ValueError:
                self.view.show(self.display_info["error"])
        return value

    def get_rythme(self):

        """
            Méthode qui permet à partir de la valeur rentrée par l'utilisateur,
            de choisir un type de partie.
            Renvoie une valeur avec le type de partie
        """

        rythme = ""
        while True:
            try:
                value = int(input("-->"))
                if value == 1:
                    rythme = "Bullet"
                    break
                elif value == 2:
                    rythme = "Blitz"
                    break
                elif value == 3:
                    rythme = "Rapid"
                    break
            except ValueError:
                self.view.show(self.display_info["error"])
        return rythme

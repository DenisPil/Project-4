
class MenuEntry:

    """
        Classe qui modélise les entrées du menu
    """

    def __init__(self, option, handler):

        """
             Arguments:
                option = déscription textuelle de l'option du menu
                handler = objet d'une classe du controlleur d'application
        """

        self.option = option
        self.handler = handler

    def __str__(self):

        """
            Permet d'afficher la description du menu.
        """

        return str(self.option)


class Menu:

    """
        Classe qui construit un menu à plusieurs entrées.
        Permer de lier une entrée de menu à une clé.
    """

    def __init__(self):

        self.entries = {}
        self.autokey = 1

    def add(self, key, option, handler):

        """
            Méthode qui ajoute une entrée au menu.

            Arguments:
                key = La clé permet d'acceder a un menu.
                option = description textuelle du menu.
                handler = correspond à l'option décrite et permet d'acceder au menu choisi
        """

        if key == "auto":
            key = str(self.autokey)
            self.autokey += 1
        self.entries[str(key)] = MenuEntry(option, handler)

    def header(self, header, header_name):

        """
            Méthode qui affiche les entête du menu.

            Arguments:
                header = Affiche la catégorie de menu ou ce trouve l'utilisateur
                header_name = Affiche le nom du menu dans le quelle ce trouve l'utilisateur
        """
        self.entries[str(header)] = MenuEntry(header_name, None)

    def items(self):

        """
            Méthode qui permet de renvoier un itérrateur a travers les clés et les entrées du menu
        """
        return self.entries.items()

    def __contains__(self, choice):

        """
            Méthode qui permet de savoir si une valeur(choice) ce trouve dans le menu.
            Renvoie un booléen (True si choice est bien dans self.entires)

            Arguments:
                choice = le choix saisi par l'utilisateur


        """

        return str(choice) in self.entries

    def __getitem__(self, choice):

        """
            Permet d'obtenir menu[choice] pour obtenir l'entrée correspondant au choix
            Renvoie une instance d'objet MenuEntry, entrée du menu de choice

            Arguments:
            choice =  choix saisi par l'utilisateur
        """

        return self.entries[choice]

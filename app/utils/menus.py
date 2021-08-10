
class MenuEntry:

    """
        Classe qui modélise les entrées du menu
    """

    def __init__(self, option, handler):

        """
             Arguments:
                option = description textuelle de l'option du menu
                handler = objet d'une classe du contrôleur d'application
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
                key = La clé permet d'accéder à un menu.
                option = description textuelle du menu.
                handler = correspond à l'option décrite et permet d'accéder au menu choisi
        """

        if key == "auto":
            key = str(self.autokey)
            self.autokey += 1
        self.entries[str(key)] = MenuEntry(option, handler)

    def header(self, header, header_name):

        """
            Méthode qui affiche les entêtes du menu.

            Arguments:
                header = Affiche la catégorie de menu où se trouve l'utilisateur
                header_name = Affiche le nom du menu dans lequel se trouve l'utilisateur
        """
        self.entries[str(header)] = MenuEntry(header_name, None)

    def items(self):

        """
            Méthode qui permet de renvoyer un itérateur à travers les clés et les entrées du menu
        """
        return self.entries.items()

    def __contains__(self, choice):

        """
            Méthode qui permet de savoir si une valeur (choice) se trouve dans le menu.
            Renvoie un booléen (True si choice est bien dans self.entires)

            Arguments:
                choice = le choix saisi par l'utilisateur


        """

        return str(choice) in self.entries

    def __getitem__(self, choice):

        """
            Permet d'obtenir menu [choice] pour obtenir l'entrée correspondante au choix
            Renvoie une instance d'objet MenuEntry, entrée du menu de choice

            Argument:
            choice =  choix saisi par l'utilisateur
        """

        return self.entries[choice]

class Player:
    """Modélise un joueur du tournoi d'échec
    """

    def __init__(self, first_name, last_name, birth_date):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date

    def __str__(self):
        info_player = ("Le joueur {} {} année de naissance: {}").format(
                self.first_name,
                self.last_name,
                self.birth_date)

        return info_player

from tinydb import TinyDB, Query


class Player:

    """
        Modélisation d'un joueur.
    """

    db = TinyDB("chess.json")
    players_table = db.table("players")
    tournament_table = db.table("tournament")

    next_id = len(players_table)
    player_id = next_id + 1

    def __init__(self,
                 first_name=None,
                 last_name=None,
                 gender=None,
                 elo=None,
                 ranking_points=None,
                 birthday=None,
                 ID=None
                 ):

        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.elo = elo
        self.ID = ID
        self.birthday = birthday
        self.ranking_points = ranking_points

    def __str__(self):

        """
            Permet d'afficher un joueur avec ses attributs.
        """

        return (f"ID : {self.ID}, Joueur : {self.first_name}  {self.last_name}, "
                f"elo : {self.elo}, points de tournoi : {self.ranking_points}")

    def serialize(self):

        """
            Serialise un joueur pour la base de donnée.
        """

        user = Query()
        self.players_table.upsert({"prenom": self.first_name,
                                   "nom": self.last_name,
                                   "genre": self.gender,
                                   "anniversaire": self.birthday,
                                   "ELO": self.elo,
                                   "points de tournoi": self.ranking_points,
                                   "ID": self.ID,
                                   }, (user.ID == self.ID))

    def add_player_from_database(self, player_id):

        """
            Méthode qui ajoute un joueur de la base de donnée a un tournoi.
            Renvoie une instance de joueur.

            Argument:
                player_id = L'id du joueur qui correspond a son doc_id de la base de donnée.
        """

        player = self.players_table.get(doc_id=player_id)
        player_instance = Player(first_name=player['prenom'],
                                 last_name=player['nom'],
                                 gender=player['genre'],
                                 birthday=player['anniversaire'],
                                 elo=player['ELO'],
                                 ranking_points=player['points de tournoi'],
                                 ID=player['ID']
                                 )
        return player_instance

    def deserialize_players_in_database(self):

        """
        Méthode qui deserialise tous les joueurs pour les archives
        Renvoie une liste de toutes les instances de joueurs
        contenue dans la base de donnée.
        """

        serialized_players = self.players_table.all()
        all_player_instance = list()
        for elem in serialized_players:
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

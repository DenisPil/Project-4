from .round import Round
from tinydb import TinyDB, Query


class Tournament:

    """
        Modélisation d'un tournoi.
    """

    db = TinyDB("chess.json")
    tournament_table = db.table("tournament")
    players_table = db.table("players")

    def __init__(self,
                 name=None,
                 location=None,
                 time_ctrl=None,
                 start_date=None,
                 end_date=None,
                 list_rounds=list(),
                 list_players=list()
                 ):

        self.name = name
        self.location = location
        self.time_ctrl = time_ctrl
        self.start_date = start_date
        self.end_date = end_date
        self.list_rounds = list_rounds
        self.list_players = list_players
        self.num_rounds = (len(self.list_rounds) + 1)
        self.nb_players = len(self.list_players)

    def create_rounds(self):

        """
            Méthode qui crée les rounds a partir de la classe 'Round',
            et les ajoutes à la liste de rounds du tournoi.
            Renvoie une instance de round.
        """

        rounds = Round(num_rounds=self.num_rounds, list_players=self.list_players)
        self.list_rounds.append(rounds)
        self.num_rounds += 1
        return rounds

    def serialize(self):

        """
            Méthode qui sérialise un tournoi pour la base de donnée.
        """
        user = Query()
        self.tournament_table.upsert({"nom": self.name,
                                      "lieu": self.location,
                                      "Nombre de joueurs": self.nb_players,
                                      "rythme": self.time_ctrl,
                                      "date de debut": self.start_date,
                                      "date de fin": self.end_date,
                                      "liste des joueurs": self.serialize_list_of_players(),
                                      "liste des rounds": self.serialize_list_of_rounds()}, (user.nom == self.name))

    def serialize_list_of_players(self):

        """
            Méthode qui sérialise la liste des joueurs d'un tournoi, qui sera ajoutée
            à la sérialisation du tournoi.
            Renvoie la liste des joueurs sérialisés du tournoi.
        """

        list_players_serialized = list()
        for player in self.list_players:
            for dbplayer in self.players_table:
                id_player_db = dbplayer.doc_id
                if player.ID == dbplayer.doc_id:
                    serialized_player = self.players_table.get(doc_id=id_player_db)
                    list_players_serialized.append(serialized_player)
        return list_players_serialized

    def serialize_list_of_rounds(self):

        """
            Méthode qui sérialise la liste des rounds d'un tournoi, qui sera ajoutée
            à la sérialisation du tournoi.
            Renvoie la liste des rounds sérialisés du tournoi.
        """

        serialized_round = list()
        for round in self.list_rounds:
            match = round.serialize_round()
            round_dict = {'round ': round.num_rounds, 'match': match}
            serialized_round.append(round_dict)
        return serialized_round

    def serialized_tournament_list(self):

        """
            Méthode qui crée une liste avec tous les tournois sérialisés
            Renvoie une liste des tournois sérialisés contenue dans la base de donnée.
        """

        serialized_tournament = self.tournament_table.all()
        return serialized_tournament

    def deserialize_rounds_from_database(self, players):

        """
            Méthode qui à partir des informations sérialisées des rounds
            d'un tournoi, crée des instances de rounds.
            Renvoie une liste d'instance de round contenue dans le tournoi.

            Argument:
                players = liste d'instance de joueurs du tournoi.
        """

        all_rounds = list()
        for key, round in enumerate(self.list_rounds):
            serialized_matches = round['match']
            num_rounds = key + 1
            round = Round(num_rounds=num_rounds, list_players=players)
            match = round.deserialize_round(serialized_matches)
            round.list_matches = match
            all_rounds.append(round)
        return all_rounds

    def __str__(self):

        """
            Méthode qui affiche les informations de base d'un tournoi.
        """
        return (f"Nom du tournoi : {self.name}, lieu :{self.location}, type de partie :{self.time_ctrl}, "
                f"date du début :{self.start_date}, date de fin: {self.end_date}")

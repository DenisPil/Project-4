from .round import Round
from tinydb import TinyDB, Query
import json

class Tournament:

    db = TinyDB("chess.json")
    tournament_table = db.table("tournament")
    players_table = db.table("players")

    def __init__(self, name, location, time_ctrl, start_date, end_date):

        self.name = name
        self.location = location
        self.time_ctrl = time_ctrl
        self.start_date = start_date
        self.end_date = end_date
        self.num_rounds = 0
        self.list_rounds = list()
        self.list_players = list()
        self.list_players_serialized = list()
        self.nb_players = len(self.list_players)

    def set_nb_players(self):
        self.nb_players = len(self.list_players)
        return self.nb_players

    def create_rounds(self):
        self.num_rounds += 1  # fait attention peut etre a revoir
        rounds = Round(num_rounds=self.num_rounds, list_players=self.list_players)
        self.list_rounds.append(rounds)
        self.serialize_list_of_rounds()
        
        return rounds

    def serialize(self):
        user = Query()
        self.tournament_table.upsert({"nom": self.name,
                                      "lieu": self.location,
                                      "Nombre de joueurs": self.nb_players,
                                      "rythme": self.time_ctrl,
                                      "date de début": self.start_date,
                                      "date de fin": self.end_date,
                                      "liste des joueurs": self.list_players_serialized}, (user.nom == self.name))
                                      # "liste des rounds": self.list_rounds}, (user.nom == self.name))

    def serialize_list_of_players(self):
        for player in self.list_players:
            for dbplayer in self.players_table:
                id_player = dbplayer.doc_id
                if player.ID == dbplayer.doc_id:
                    serialized_player = self.players_table.get(doc_id=id_player)
                    self.list_players_serialized.append(serialized_player)

    def serialize_list_of_rounds(self):
        test = self.list_rounds[0].serialized_rounds
        print (test,'-9-9-9-9-9-9-9-9-9-9-9-9-9-9')
        print(self.list_rounds[0].list_matches, '8-8-8-8-8-8-8-8--8-')

    def __str__(self):
        return (f"""Nom du tournoi : {self.name}, lieu :{self.location}, type de partie :{self.time_ctrl}, date du début :{self.start_date}, date de fin: {self.end_date}""")

    def __getitem__(self, choice):
        return self.player_1[choice]

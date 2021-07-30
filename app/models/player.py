from tinydb import TinyDB, Query


class Player:

    db = TinyDB("chess.json")
    players_table = db.table("players")

    next_id = len(players_table)
    player_id = next_id + 1

    def __init__(self, first_name, last_name, gender, elo, ranking_points, birthday, ID):

        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.elo = elo
        self.ID = ID
        self.birthday = birthday
        self.ranking_points = ranking_points

    def __str__(self):
        return f"ID : {self.ID}, Joueur : {self.first_name}  {self.last_name}, elo : {self.elo}, points de tournoi : {self.ranking_points}"

    def serialize(self):
        user = Query()
        self.players_table.upsert({"prenom": self.first_name,
                                   "nom": self.last_name,
                                   "genre": self.gender,
                                   "anniversaire": self.birthday,
                                   "ELO": self.elo,
                                   "points de tournoi": self.ranking_points,
                                   "ID": self.ID,
                                   }, (user.ID == self.ID))
        Player.player_id += 1

    def add_player_from_database(self, info):
        player = self.players_table.get(doc_id=info)
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

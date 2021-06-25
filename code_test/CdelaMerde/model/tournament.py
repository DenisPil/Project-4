import datetime
from datetime import datetime
from operator import itemgetter
import view

list_players = [{'nom': 'dupont', 'prénom': 'loulou', 'gender': 'Homme', 'anniversaire': '14/07/1988', 'elo': '1187', 'id': 1},
                {'nom': 'dupuit', 'prénom': 'lou', 'gender': 'Femme', 'anniversaire': '29/1999', 'elo': '1200', 'id': 2},
                {'nom': 'dubois', 'prénom': 'fifi', 'gender': 'Homme', 'anniversaire': '30/07/1967', 'elo': '1198', 'id': 3},
                {'nom': 'ducon', 'prénom': 'riri', 'gender': 'Femme', 'anniversaire': '13/07/1985', 'elo': '1245', 'id': 4},
                {'nom': 'domino', 'prénom': 'mimi', 'gender': 'Homme', 'anniversaire': '02/07/1975', 'elo': '1278', 'id': 5},
                {'nom': 'dimano', 'prénom': 'marie', 'gender': 'Femme', 'anniversaire': '15/07/1981', 'elo': '1180', 'id': 6},
                {'nom': 'domina', 'prénom': 'jeanjean', 'gender': 'Homme', 'anniversaire': '24/07/2001', 'elo': '1210', 'id': 7},
                {'nom': 'damasio', 'prénom': 'alain', 'gender': 'Homme', 'anniversaire': '28/09/1969', 'elo': '1289', 'id': 8}]


class Tournament:

    

    def __init__(self, name=None, place=None, nb_players=None, time_ctrl=None, start_date=None, end_date="", player_1=None, player_2=None):

        self.name = name
        self.place = place
        self.nb_players = nb_players
        self.time_ctrl = time_ctrl
        self.start_date = start_date
        self.end_date = end_date
        self.tournament_info = []
        self.rounds = []
        self.players = list_players
        self.player_1 = player_1
        self.player_2 = player_2

    def set_nb_players(self):
        self.nb_players = len(list_players)
        return self.nb_players

    def set_rythme(self, rythme):
        if rythme == "2":
            self.time_ctrl = ("Blitz")
        else:
            self.time_ctrl = ("Bullet")

    def create_dict(self):
        self.info = {
            "Nom du tournoi": self.name,
            "Lieu": self.place,
            "Nombre de joueurs": self.nb_players,
            "Rythme du tournoi": self.time_ctrl,
            "Date du tournoi": (self.start_date, self.end_date),
            "Joueurs": self.players,
            "Round": self.rounds
        }
        self.tournament_info.append(self.info)

    def sort_elo(self):
        list_name_elo = []
        for elem in list_players:
            elo = elem["elo"]
            id_player = elem["prénom"]
            dictp = (id_player, elo)
            list_name_elo.append(dictp)
        getcount = itemgetter(1)
        self.sorted_elo = (sorted(list_name_elo, key=getcount))
        return self.sorted_elo

    def player_attribution(self):
        self.list_match = []
        p = self.sort_elo()
        a = p[0:4]
        b = p[4:8]
        i = 0
        while i != 4:
            dict_match = {"player_1": a[i], "player_2": b[i]}
            self.list_match.append(dict_match)
            i += 1
        return self.list_match

    def create_rounds(self):
        list_match = self.player_attribution()
        for elem in list_match:
            rounds_obj = Tournament(player_1=elem["player_1"][0], player_2=elem["player_2"][0])
            self.rounds.append(rounds_obj)
        return self.rounds
    
    def __str__(self):
        self.num_rounds =+ 1
        return f"Round {self.num_rounds}, Joueur N°1 : {self.player_1}, Joueur N°2 : {self.player_2}"


class Round:

    def __init__(self, num_rounds=None, player_1=None, player_2=None):
        self.start_time = self.set_time()
        self.end_time = self.set_time()
        self.num_rounds = num_rounds
        self.players_ranking = []
        self.player_1 = player_1
        self.player_2 = player_2
        self.win = None

    def set_time(self):
        self.time_now = datetime.now().time()
        return self.time_now

    def add_ranking_points(self):
        t = input("w 1, l 2")
        if t == '1':
            print("win")
            self.win = True
        else:
            print("lose")
            self.win = False
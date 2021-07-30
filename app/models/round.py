from datetime import datetime
from operator import attrgetter
from tinydb import TinyDB, Query

class Round:


    def __init__(self, list_players, num_rounds=int):
        self.start_time = self.set_time()
        self.end_time = self.set_time()
        self.num_rounds = num_rounds
        self.list_matches = list()
        self.list_players = list_players
        self.player_1_result = None
        self.num_match = 1
        self.serialized_rounds = list()

    def set_time(self):
        self.time_now = datetime.now().time()
        return self.time_now

    def create_first_match(self):
        self.serialize_list_of_matches_and_rounds()
        self.list_players.sort(key=lambda value: value.elo, reverse=True)
        sort_list_a = self.list_players[0:4]
        sort_list_b = self.list_players[4:8]
        i = 0
        while i != 4:
            match = {"Match": self.num_match,
                     "Joueur 1": sort_list_a[i],
                     "Joueur 2": sort_list_b[i],
                     "winner": self.player_1_result
                     }
            self.list_matches.append(match)
            self.num_match += 1
            i += 1

        self.num_match = 1

    def create_matches(self):
        sort_elo = sorted(self.list_players, key=attrgetter('elo'), reverse=True)
        sort_points = sorted(sort_elo, key=attrgetter('ranking_points'), reverse=True)
        length = len(sort_points)
        for elem in range(0, length, 2):
            player_1 = sort_points[elem]
            player_2 = sort_points[elem + 1]
            match = {"Match": self.num_match,
                     "Joueur 1": player_1,
                     "Joueur 2": player_2,
                     "winner": self.player_1_result
                     }
            self.num_match += 1
            self.list_matches.append(match)
        self.num_match = 1

    def serialize_list_of_matches_and_rounds(self):

        for elem in self.list_matches:
            p1 = elem['Joueur 1']
            p2 = elem['Joueur 2']
            m = elem['Match']
            test = {"m": m,
                    "p1": p1.ID,
                    "p2": p2.ID}
            print(p1, "aeaezeaezaeazeazeffazdc")
            self.serialized_rounds.append(test)
        print(self.serialized_rounds, "GGGGGGGGGGGGGGGGGGGGGGGGGGGGGG")    





    """
    __getitem__
    Cet opérateur est appelé lorsqu’on cherche à accéder à un élément
    de l’objet self d’indice i comme si c’était une liste.
    """
    """
     __str__
    Convertit un objet en une chaîne de caractère qui sera affichée
    par la fonction print ou obtenu avec la fonction str.
    """

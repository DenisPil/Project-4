from datetime import datetime
from operator import attrgetter

class Round:

    def __init__(self, list_players, num_rounds=0):
        self.start_time = self.set_time()
        self.end_time = self.set_time()
        self.num_rounds = num_rounds
        self.list_match = []
        self.list_players = list_players
        self.player_1_result = None
        self.num_match = 1

    def set_time(self):
        self.time_now = datetime.now().time()
        return self.time_now

    def create_first_match(self):
        self.list_players.sort(key=lambda value: value.elo, reverse=True)
        sort_list_a = self.list_players[0:4]
        sort_list_b = self.list_players[4:8]
        i = 0
        while i != 4:
            match = {"Match ": self.num_match,
                     "Joueur 1": sort_list_a[i],
                     "Joueur 2": sort_list_b[i],
                     "winner": self.player_1_result
                     }
            self.list_match.append(match)
            self.num_match += 1
            i += 1

    def create_matches(self):
        sort_elo = sorted(self.list_players, key=attrgetter('elo'), reverse=True)
        sort_points = sorted(sort_elo, key=attrgetter('ranking_points'), reverse=True)
        length = len(sort_points)
        for elem in range(0, length, 2):
            player_1 = sort_points[elem]
            player_2 = sort_points[elem + 1]
            match = {"Match ": self.num_match,
                     "Joueur 1": player_1,
                     "Joueur 2": player_2,
                     "winner": self.player_1_result
                     }
            self.num_match += 1
            self.list_match.append(match)

    def set_winner(self):
        for match in self.list_match:
            player_1 = match["Joueur 1"]
            player_2 = match["Joueur 2"]
            print("LE NUM DU ROUND :", self.num_rounds, "joueur 1 :", player_1, "joueur 2 :", player_2)
            value = input("le joueur-1 a gagné ou perdu ou nul  G/P/N :")
            if value == 'g':
                match["winner"] = True
            elif value == 'p':
                match["winner"] = False
            else:
                value == 'n'
                match["winner"] = None

    def set_ranking_points(self):

        for elem in self.list_match:

            player_1 = elem["Joueur 1"]
            player_2 = elem["Joueur 2"]
            result = elem["winner"]
            if result is True:
                player_1.ranking_points += 1
                player_1.elo += player_1.ranking_points
            elif result is False:
                player_2.ranking_points += 1
                player_2.elo += player_2.ranking_points
            else:
                player_1.ranking_points += 0.5
                player_2.ranking_points += 0.5
                player_1.elo += player_1.ranking_points
                player_2.elo += player_2.ranking_points

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
    def __str__(self):
        return f"Round {self.num_rounds}, Players : {self.list_match}  , résultat {self.player_1_result} "
        # Joueur N°1 : {self.player_1}, Joueur N°2 : {self.player_2},

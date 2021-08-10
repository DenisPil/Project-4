from datetime import datetime
from operator import attrgetter


class Round:

    """
        Modélisation d'un round.
    """

    def __init__(self, list_players, num_rounds=int):
        self.start_time = None
        self.end_time = None
        self.num_rounds = num_rounds
        self.list_matches = list()
        self.list_players = list_players
        self.player_1_result = None
        self.num_match = 1
        self.serialized_rounds = list()

    def set_time(self):

        """
            Méthode qui permet de connaitre l'heure du début et de fin d'un round.
            Renvoie une valeur avec l'heure.
        """

        time_now = datetime.now().time()
        return time_now

    def create_first_match(self):

        """
            Méthode qui crée les matchs du premier round.
        """

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

        """
            Méthode qui crée les matchs des round 2, 3 et 4.
        """

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

    def serialize_round(self):

        """
            Méthode qui sérialise les rounds.
            Renvoie une liste des rounds sérialisés
        """

        serialized_round = list()
        for match in self.list_matches:
            start_time = self.start_time
            end_time = self.end_time
            p1 = match['Joueur 1']
            p2 = match['Joueur 2']
            match_num = match['Match']
            match_winner = match['winner']
            matches = {"match": match_num,
                       "heure du match": (str(start_time), str(end_time)),
                       "Joueur 1": (p1.ID),
                       "Joueur 2": (p2.ID),
                       "le gagnant": match_winner
                       }
            serialized_round.append(matches)
        return serialized_round

    def deserialize_round(self, round):

        """
            Méthode qui désérialise un round.
            Renvoie la liste des matchs du round.

            Argument:
                round = un dictionnaire des matchs du round.
        """

        list_matches = list()
        for elem in round:
            start_time = elem['heure du match']
            p1 = elem['Joueur 1']

            p2 = elem['Joueur 2']
            match_num = elem['match']
            match_winner = elem['le gagnant']
            player_1 = [player for player in self.list_players if p1 == player.ID]
            player_2 = [player for player in self.list_players if p2 == player.ID]
            match = {"Match": match_num,
                     "Joueur 1": player_1[0],
                     "Joueur 2": player_2[0],
                     "winner": match_winner,
                     "heure du match": start_time
                     }
            list_matches.append(match)
        return list_matches

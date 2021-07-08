from operator import itemgetter
from model.round import Round


class Tournament:

    def __init__(self, name, place, time_ctrl, start_date, end_date, player_1=None, player_2=None):

        self.name = name
        self.place = place
        self.nb_players = int
        self.time_ctrl = time_ctrl
        self.start_date = start_date
        self.end_date = end_date
        self.player_1 = player_1
        self.player_2 = player_2
        self.num_rounds = 1
        self.ranking_points = 0
        self.num_match_in_round = 1
        self.tournament_info = []
        self.list_rounds = []
        self.list_players = []

    def set_nb_players(self):
        self.nb_players = len(self.list_players)
        return self.nb_players

    def create_rounds(self):
        while self.num_rounds != 5:
            rounds = Round(num_rounds=self.num_rounds, list_players=self.list_players)
            self.list_rounds.append(rounds)
            self.num_rounds += 1
        return self.list_rounds

    def set_ranking_points(self, matchs):
        for elem in matchs:
            print(elem)
            player_1 = elem[3]
            player_2 = elem[5]
            result = elem[7]
            if result is True:
                player_1.ranking_points += 2
                player_2.ranking_points -= 2

            elif result is False:
                player_1.ranking_points -= 2
                player_2.ranking_points += 2
            else:
                player_1.ranking_points += 1
                player_2.ranking_points += 1
            print("J1 :", player_1, "J2 :", player_2)

    """
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
        return self.tournament_info

    def rework_list(self, list_match):
        for elem in list_match:
            player_1 = elem["player_1"]
            player_2 = elem["player_2"]
            player_1.pop("elo")
            player_2.pop("elo")
            key = {"adversaire ID": []}
            key2 = {"adversaire ID": []}
            player_1.update(key)
            player_2.update(key2)
        return list_match

    def last_opponent(self, list_match):
        print(list_match, 'LA LIST EN ENTREE')
        list_players = []
        for elem in list_match:
            player_1 = elem["player_1"]
            player_2 = elem["player_2"]
            player_1["adversaire ID"].append(player_2["ID"])
            player_2["adversaire ID"].append(player_1["ID"])
            list_players.append(player_1)
            list_players.append(player_2)
        return list_players

    def sorted_ranking_points(self, list_match):
        getcount = itemgetter("ranking_points")
        sorted_ranking = (sorted(list_match, key=getcount, reverse=True))
        return sorted_ranking

    def next_player_attribution(self, player_list):
        dict_match = {}
        list_match = []
        i = 0
        while i != len(player_list):
            if player_list[i]["ID"] == player_list[i + 1]["adversaire ID"]:
                dict_match = {"player_1": player_list[i], "player_2": player_list[i + 1]}

                list_match.append(dict_match)
            elif player_list[i]["ID"] == player_list[i - 2]["adversaire ID"]:
                dict_match = {"player_1": player_list[i], "player_2": player_list[i - 2]}
                list_match.append(dict_match)

            elif player_list[i]["ID"] == player_list[i - 3]["adversaire ID"]:
                dict_match = {"player_1": player_list[i], "player_2": player_list[i - 3]}
                list_match.append(dict_match)

            else:
                if player_list[i]["ID"] != player_list[i + 1]["adversaire ID"]:
                    dict_match = {"player_1": player_list[i], "player_2": player_list[i + 1]}
                    list_match.append(dict_match)
            i += 2
        # print(list_match)
        return list_match
        """

    def __str__(self):
        return f"ID : {self.list_players}"

    def __getitem__(self, choice):
        return self.player_1[choice]

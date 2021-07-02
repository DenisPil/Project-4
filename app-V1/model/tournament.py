from operator import itemgetter
from model.round import Round

list_players = [{'nom': 'dupont', 'prénom': 'loulou', 'gender': 'Homme',
                 'anniversaire': '14/07/1988', 'elo': '1101', 'id': 1},
                {'nom': 'dupuit', 'prénom': 'lou', 'gender': 'Femme',
                'anniversaire': '29/1999', 'elo': '1102', 'id': 2},
                {'nom': 'dubois', 'prénom': 'fifi', 'gender': 'Homme',
                'anniversaire': '30/07/1967', 'elo': '1103', 'id': 3},
                {'nom': 'ducon', 'prénom': 'riri', 'gender': 'Femme',
                'anniversaire': '13/07/1985', 'elo': '1104', 'id': 4},
                {'nom': 'domino', 'prénom': 'mimi', 'gender': 'Homme',
                'anniversaire': '02/07/1975', 'elo': '1105', 'id': 5},
                {'nom': 'dimano', 'prénom': 'marie', 'gender': 'Femme',
                'anniversaire': '15/07/1981', 'elo': '1106', 'id': 6},
                {'nom': 'domina', 'prénom': 'jeanjean', 'gender': 'Homme',
                'anniversaire': '24/07/2001', 'elo': '1107', 'id': 7},
                {'nom': 'damasio', 'prénom': 'alain', 'gender': 'Homme',
                'anniversaire': '28/09/1969', 'elo': '1108', 'id': 8}]


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
        self.num_rounds = 0
        self.ranking_points = 0
        self.tournament_info = []
        self.rounds = []
        self.list_players = list_players
        self.winner = None

    def set_nb_players(self):
        self.nb_players = len(self.list_players)
        return self.nb_players

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

    def sort_elo(self, list_players):
        list_name_elo = []
        for elem in list_players:
            elo = elem["elo"]
            first_name_player = elem["prénom"]
            last_name_player = elem["nom"]
            id_player = elem["id"]
            dictp = {"nom": first_name_player + " " + last_name_player, "elo": elo, 'ID': id_player}
            list_name_elo.append(dictp)
        getcount = itemgetter("elo")
        self.sorted_elo = (sorted(list_name_elo, key=getcount))
        return self.sorted_elo

    def player_attribution(self, sorted_elo):
        self.list_match = []
        sort_list = sorted_elo
        sort_list_a = sort_list[0:4]
        sort_list_b = sort_list[4:8]
        i = 0
        while i != 4:
            dict_match = {"player_1": sort_list_a[i], "player_2": sort_list_b[i]}
            self.list_match.append(dict_match)
            i += 1
        return self.list_match

    def create_rounds(self, list_match):
        self.num_rounds += 1
        for elem in list_match:
            rounds_obj = Round(player_1=elem["player_1"],
                               player_2=elem["player_2"])
            self.rounds.append(rounds_obj)
        return self.rounds

    def get_winner(self, list_round):
        for game in list_round:
            print("Joueur 1 :", game["player_1"], "Joueur 2 :", game["player_2"])
            player_1 = game["player_1"]
            player_2 = game["player_2"]
            # print(game['elo'], "le test")
            value = input("le joueur-1 a gagné ou perdu ou nul  G/P/N :")
            if value == 'g':
                print("le joueur-1 a gagné")
                self.winner = True
                player_1.update({"ranking_points": + 2})
                player_2.update({"ranking_points": + 0})
                # print(game['elo'])
            elif value == 'p':
                print("le joueur-1 a perdu")
                self.winner = False
                player_1.update({"ranking_points": + 0})
                player_2.update({"ranking_points": + 2})
            else:
                value == 'n'
                print("match nul")
                self.winner = None
                player_1.update({"ranking_points": + 1})
                player_2.update({"ranking_points": + 1})
        return self.winner

    def rework_list(self, list_match):
        for elem in list_match:
            player_1 = elem["player_1"]
            player_2 = elem["player_2"]
            player_1.pop("elo")
            player_2.pop("elo")
            key = {"adversaire ID": []}
            player_1.update(key)
            player_2.update(key)
        return list_match

    def last_opponent(self, list_match):
        print(list_match, 'LA LIST EN ENTRE')
        list_players = []
        for elem in list_match:
            print(elem, "LES ELEMENTS DE LA LISTE")
            player_1 = elem["player_1"]
            player_2 = elem["player_2"]
            player_1["adversaire ID"] = player_2["ID"]
            # player_2["adversaire ID"].append(player_1["ID"])
            print(player_1["adversaire ID"], "ADVERSSSAIRE IIIIDDDDD PP1")
            print(player_2["adversaire ID"], "ADVERSSSAIRE IIIIDDDDD  PP2")
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

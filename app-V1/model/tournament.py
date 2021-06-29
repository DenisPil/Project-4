from operator import itemgetter
from model.round import Round

list_players = [{'nom': 'dupont', 'prénom': 'loulou', 'gender': 'Homme',
                 'anniversaire': '14/07/1988', 'elo': '1101', 'id': 1},
                {'nom': 'dupuit', 'prénom': 'lou', 'gender': 'Femme',
                'anniversaire': '29/1999', 'elo': '1112', 'id': 2},
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
            id_player = elem["prénom"]
            dictp = {"nom": id_player, "elo": elo}
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
            # print(self.rounds, "dans create rounds")
        return self.rounds



"""t = Tournament("","","","","")
p =t.sort_elo(list_players)
print(p)"""


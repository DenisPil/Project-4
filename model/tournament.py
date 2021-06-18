import datetime
from datetime import datetime
from operator import itemgetter


list_players = [{'nom': 'dupont', 'prénom': 'loulou', 'gender': 'Homme', 'anniversaire': '14/07/1988', 'elo': '1187', 'id': 1},
                {'nom': 'dupuit', 'prénom': 'lou', 'gender': 'Femme', 'anniversaire': '29/1999', 'elo': '1200', 'id': 2},
                {'nom': 'dubois', 'prénom': 'fifi', 'gender': 'Homme', 'anniversaire': '30/07/1967', 'elo': '1198', 'id': 3},
                {'nom': 'ducon', 'prénom': 'riri', 'gender': 'Femme', 'anniversaire': '13/07/1985', 'elo': '1245', 'id': 4},
                {'nom': 'domino', 'prénom': 'mimi', 'gender': 'Homme', 'anniversaire': '02/07/1975', 'elo': '1278', 'id': 5},
                {'nom': 'dimano', 'prénom': 'marie', 'gender': 'Femme', 'anniversaire': '15/07/1981', 'elo': '1180', 'id': 6},
                {'nom': 'domina', 'prénom': 'jeanjean', 'gender': 'Homme', 'anniversaire': '24/07/2001', 'elo': '1210', 'id': 7},
                {'nom': 'damasio', 'prénom': 'alain', 'gender': 'Homme', 'anniversaire': '28/09/1969', 'elo': '1289', 'id': 8}]


class Tournament:

    tournament_info = []

    def __init__(self, name=None, place=None, nb_players=None, time_ctrl=None, date=None):

        self.name = name
        self.place = place
        self.nb_players = nb_players
        self.time_ctrl = time_ctrl
        self.date = date

    def set_name(self):
        self.name = input("Le nom du tournoi : ")
        return self.name

    def set_place(self):
        self.place = input("Où a lieu le Tournoi : ")
        return self.place

    def set_nb_players(self):
        self.nb_players = len(list_players)
        return self.nb_players

    def set_rythme(self):

        print("Dans qu'elle mode de jeu, sera joué le tournoi ?")
        rythme = input(" 1 pour Bullet, 2 pour Blitz :")
        if rythme == "2":
            blitz = input("Le tournoi sera en mode Blitz quelle durée part partie ? : ")
            print("la durée de chaque partie est de", blitz, "min.")
            self.time_ctrl = ("Blitz")
            print("Blitz", blitz, "minutes.")
        else:
            self.time_ctrl = ("Bullet")
            print("Partie en mode Bullet, 1 minute.")
        return self.time_ctrl

    def set_date(self):

        print("Le tournoi ce déroule sur une journée ?")
        duration = input("1 oui  2 non : ")
        if duration == "1":
            print("entrée la date de début et la date de fin du tournoi : ")
            start = input("rentrer une date de début de tournoi dans le format suivant '01/01/1901' : ")
            try:
                datetime.datetime.strptime(start, '%d/%m/%Y')
                end = start
            except ValueError:
                print("Veuillez saisir une date valide sous la forme 01/01/1901")
                start = input()
            print(start)
        else:
            print("entrée la date de début et la date de fin du tournoi : ")
            start = input("rentrer une date de début de tournoi dans le format suivant '01/01/1901' : ")
            try:
                datetime.datetime.strptime(start, '%d/%m/%Y')

            except ValueError:
                print("Veuillez saisir une date valide sous la forme 01/01/1901")
                start = input()

            end = input("rentrer une date de fin de tournoi dans le format suivant '01/01/1901' : ")    
            try:
                datetime.datetime.strptime(end, '%d/%m/%Y')

            except ValueError:
                print("Veuillez saisir une date valide sous la forme 01/01/1901")
                end = input()
            if start > end:
                print("la date de fin ne peut être avant le début de tournoi ! entrer une nouvelle date de fin de tournoi : ")                   
                end = input("rentrer une date de fin de tournoi qui ce termine aprés le : ", start)
            print("la date de début de tournoi est le : ", start, "la date de fin est le : ", end)

        self.date = (start, end)
        return (self.date)

    def create_dict(self):
        self.info = {
            "Nom du tournoi": self.name,
            "Lieu": self.place,
            "Nombre de joueurs": self.nb_players,
            "Rythme du tournoi": self.time_ctrl,
            "Date du tournoi": self.date
        }
        self.tournament_info.append(self.info)

    def set_all_info(self):
        self.set_name()
        self.set_place()
        self.set_nb_players()
        self.set_rythme()
        self.set_date()
        self.create_dict()


class Round:


    def __init__(self, num_rounds=None, player_1=None, player_2=None):
        self.start_time = self.get_time()
        self.end_time = self.get_time()
        self.num_rounds = num_rounds
        self.players_ranking = []
        self.player_1 = player_1
        self.player_2 = player_2

    def get_time(self):
        self.time_now = datetime.now().time()
        return self.time_now
        
    def sort_elo(self):
        list_name_elo = []
        for elem in list_players:
            elo = elem["elo"]
            id_player = elem["prénom"]
            dictp = (id_player, elo)
            list_name_elo.append(dictp)
        getcount = itemgetter(1)
        list(map(getcount, list_name_elo))
        self.sorted_elo = (sorted(list_name_elo, key=getcount))
        return self.sorted_elo

    def player_attribution(self):
        self.list_match = []
        p = self.sort_elo(self)  # voir avec Thim pour le deuxieme self "TypeError: sort_elo() missing 1 required positional argument: 'self'"
        a = p[0:4]
        b = p[4:8]
        i = 0
        while i != 4:
            dict_match = {"player_1": a[i], "player_2": b[i]}
            self.list_match.append(dict_match)
            i += 1
        return self.list_match

    @classmethod
    def create_rounds(cls):
        list_match = Round.player_attribution(cls)
        rounds = []
        for elem in list_match:
            rounds_obj = cls(player_1=elem["player_1"][0], player_2=elem["player_2"][0])
            rounds.append(rounds_obj)
        return rounds

    def __str__(self):
        self.num_rounds =+ 1
        return f"Round {self.num_rounds}, Joueur N°1 = {self.player_1}, Joueur N°2 = {self.player_2}"

    def add_ranking_points(self):
        test = Round.create_rounds()
        print(test[1])




    def player_ranking(self):
        pass

t=Round()
t.add_ranking_points()

"""
test = Round()
print(test.sort_elo())
"""

#Création du round 1
"""
t = Round.create_rounds() #factory
for j in t: 
    print(j)
"""


#Création du tournoi 
"""
t = Tournament()
t.set_all_info()
print(Tournament.tournament_info)
"""
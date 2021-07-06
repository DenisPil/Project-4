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
        self.num_rounds = 0
        self.ranking_points = 0
        self.tournament_info = []
        self.rounds = []
        self.list_players = []
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
            elo = elem[0]["elo"]
            first_name_player = elem[0]["prénom"]
            last_name_player = elem[0]["nom"]
            ranking_points = elem[0]["points de tournoi"]
            id_player = elem[0]["id"]
            dictp = {"nom": str(first_name_player) + " " + str(last_name_player), "elo": elo, "points de tournoi": ranking_points, 'ID': id_player}
            list_name_elo.append(dictp)
        getcount = itemgetter("elo")
        self.sorted_elo = (sorted(list_name_elo, key=getcount, reverse=True))
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
                               player_2=elem["player_2"]
                               )
            self.rounds.append(rounds_obj)
            Round().list_rounds = self.rounds
        return self.rounds

    # player_1["ranking_points"] += 2  # bonne méthode


    """
                    Tim donc je travail sur "self.list_players" le "i" représente le numéro.
                    Dans l'instance d'un joueur,
                    je veux lui ajouter des points de tournoi.
                    Je fais les modifs de points de tournoi, 
                    ensuite j'affiche "self.list_players[i][0]" et les informations sont bien la
                    mais a la fin du processuce quand je veux afficher self.list_players, et bien il y a plus rien.
                    Si je comprend bien c est que l'objet "self.list_players[i][0]" n'est pas "self.list_players".
                    C'est un dict qui est créé grace a une instance de joueur mais au final, si je modifie ce dict cela ne modifie
                    pas l'instance et c'est 
                    le coeur du pb je n'arrive pas a modifier une information de l'instance.
                    J'ai besoin de savoir comment faire je perd tellement de temps a tourner en rond...
                    En dessous de la méthode il y a le résultat de ma console 
                

    """


    def set_ranking_points(self, round):
        for elem in round:
            round_winner = Round().get_winner()
            if round_winner is True:
                print(elem)
                print("le joueur-1 a gagné")
                i = 0
                print(self.list_players," liste d'instances de mes joueurs")
                print(self.list_players[i], "l'instance d'un joueur, j'utilise __srt__ pour qu'elle soit lisible")
                print(self.list_players[i][0], "a partir de l'instance j'accede au dict qui contient toutes les infos")             
                while i != 8:

                    if self.list_players[i][0]["id"] == elem["ID"][0]:
                        self.list_players[i][0]["points de tournoi"] += 2
                        print(self.list_players[i][0],"le dict créé a partir de mon instance")
                        print(self.list_players[i],"mon instance de joueur")   
                    if self.list_players[i][0]["id"] == elem["ID"][1]:
                        self.list_players[i][0]["points de tournoi"] -= 2
                    i += 1
            elif round_winner is False:
                print("le joueur-1 a perdu")
                i = 0
                while i != 8:
                    if self.list_players[i][0]["id"] == elem["ID"][0]:
                        self.list_players[i][0]["points de tournoi"] -= 2
                    if self.list_players[i][0]["id"] == elem["ID"][1]:
                        self.list_players[i][0]["points de tournoi"] += 2
                    i += 1
            else:
                round_winner is None
                print("match-nul")
                i = 0
                while i != 8:
                    if self.list_players[i][0]["id"] == elem["ID"][0]:
                        self.list_players[i][0]["points de tournoi"] += 1
                    if self.list_players[i][0]["id"] == elem["ID"][0]:
                        self.list_players[i][0]["points de tournoi"] += 1
                    i += 1  

        return self.list_players            

""" voila le résultat dans ma console

ligne 83
Round 1, Joueur N°1 : {'nom': ' 8', 'elo': 8, 'points de tournoi': 0, 'ID': 8}, Joueur N°2 : {'nom': ' 4', 'elo': 4, 'points de tournoi': 0, 'ID': 4}                    
le joueur-1 a gagné ou perdu ou nul  G/P/N :g

ligne 84
le joueur-1 a gagné

ligne 86
[<model.player.Player object at 0x0000013A62726D00>, <model.player.Player object at 0x0000013A62726CD0>, <model.player.Player object at 0x0000013A62726D60>, <model.player.Player object 
at 0x0000013A62726D90>,
<model.player.Player object at 0x0000013A62726DC0>, <model.player.Player object at 0x0000013A62726DF0>, <model.player.Player object at 0x0000013A62726E20>, 
<model.player.Player object at 0x0000013A62726E50>]  liste d'instances de mes joueurs

ligne 87
l'instance d'un joueur, j'utilise __srt__ pour qu'elle soit lisible
ID : 1, Nom : 1, prénom : , genre : genre,anniversaire :birthday, elo : 1, points de tournoi : 0  

ligne 88
a partir de l'instance j'accede au dict qui contient toutes les infos  
{'id': 1, 'nom': 1, 'prénom': '', 'genre': 'genre', 'anniversaire': 'birthday', 'elo': 1, 'points de tournoi': 0} 
 
ligne 107
le dict créé a partir de mon instance
{'id': 8, 'nom': 8, 'prénom': '', 'genre': 'genre', 'anniversaire': 'birthday', 'elo': 8, 'points de tournoi': 2} le dict créé a partir de mon instance

ligne 108
mon instance de joueur
ID : 8, Nom : 8, prénom : , genre : genre,anniversaire :birthday, elo : 8, points de tournoi : 0  
                    """



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


    def __str__(self):
        return f"ID : {self.list_players}"


    def __getitem__(self, choice):
        return self.player_1[choice]
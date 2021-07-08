from datetime import datetime


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

    def create_matchs_in_round(self):
        self.list_players.sort(key=lambda value: value.elo, reverse=True)
        sort_list_a = self.list_players[0:4]
        sort_list_b = self.list_players[4:8]
        i = 0
        while i != 4:
            match = ["Match :", self.num_match,
                     "J1:", sort_list_a[i],
                     "J2:", sort_list_b[i],
                     "winner:", self.player_1_result
                     ]
            self.list_match.append(match)
            self.num_match += 1
            i += 1
        return self.list_match

    def get_winner(self, matchs):
        for match in matchs:
            player_1 = match[3]
            player_2 = match[5]
            print("joueur 1 :", player_1, "joueur 2 :", player_2)
            value = input("le joueur-1 a gagné ou perdu ou nul  G/P/N :")
            if value == 'g':
                match[7] = True
            elif value == 'p':
                match[7] = False
            else:
                value == 'n'
                match[7] = None
        return matchs

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
        return f"Round {self.num_rounds}, Players : {self.list_match}  , résultat {self.player_1_win_round} "
        # Joueur N°1 : {self.player_1}, Joueur N°2 : {self.player_2},

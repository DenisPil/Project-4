from datetime import datetime


class Round:

    def __init__(self, num_rounds=None, player_1=None, player_2=None, list_round=[]):
        self.start_time = self.set_time()
        self.end_time = self.set_time()
        self.num_rounds = num_rounds
        self.players_ranking = []
        self.player_1 = player_1
        self.player_2 = player_2
        self.winner = None
        self.list_round = list_round
        #print(self.player_1)


    def set_time(self):
        self.time_now = datetime.now().time()
        return self.time_now

    def add_ranking_points(self, player ):
        for game in self.list_round:
            print(player)
            print(game)


    """   t = input("le joueur-1 a gagné ou perdu ou nul  G/P/N")
        if t == 'G':
            print("win")
            self.win = True
        elif t == 'P':
            print("P")
            self.win = False
        else:
            t == 'N'
            print("match nul")
            self.win = None"""

    def __repr__(self):
        return f"__repr__ {self.list_round} "

    def __str__(self):
        self.num_rounds =+ 1
        return f"Round {self.num_rounds}, Joueur N°1 : {self.player_1}, Joueur N°2 : {self.player_2}"


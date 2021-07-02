from datetime import datetime


class Round:

    def __init__(self, player_1=None, player_2=None, list_round=[]):
        self.start_time = self.set_time()
        self.end_time = self.set_time()
        self.num_rounds = 0
        self.players_ranking = []
        self.player_1 = player_1
        self.player_2 = player_2
        self.winner = None
        self.list_round = list_round
        # print(self.player_1, "Round self.player_1 ")
        self.num_rounds += 1

    def set_time(self):
        self.time_now = datetime.now().time()
        return self.time_now

    def __str__(self):

        return f"Round {self.num_rounds}, Joueur N°1 : {self.player_1}, Joueur N°2 : {self.player_2}"

    """
    def __contains__(self, choice):
        return str(choice) in self.player_1

    def __getitem__(self, choice):
        return self.player_1[choice]
    """

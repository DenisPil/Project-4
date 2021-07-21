from models.round import Round


class Tournament:

    def __init__(self, name, location, time_ctrl, start_date, end_date):

        self.name = name
        self.location = location
        self.nb_players = int
        self.time_ctrl = time_ctrl
        self.start_date = start_date
        self.end_date = end_date
        self.num_rounds = 0
        self.tournament_info = []
        self.list_rounds = []
        self.list_players = []

    def set_nb_players(self):
        self.nb_players = len(self.list_players)
        return self.nb_players

    def create_rounds(self):
        self.num_rounds += 1
        rounds = Round(num_rounds=self.num_rounds, list_players=self.list_players)
        self.list_rounds.append(rounds)
        
        return rounds

    def __str__(self):
        return (f"Nom du tournoi : {self.name}, lieu :{self.location}, type de partie :{self.time_ctrl}, date du début :{self.start_date}, date de fin: {self.end_date}")

    def __getitem__(self, choice):
        return self.player_1[choice]

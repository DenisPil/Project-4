class Player:

    player_id = 1

    def __init__(self, first_name, last_name, gender, elo, ranking_points, birthday):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.elo = elo
        self.ID = Player.player_id
        self.birthday = birthday
        self.ranking_points = ranking_points
        self.list_players = []

        Player.player_id += 1

    def create_dict(self):
        self.info_player = {
            'id': self.ID,
            'nom': self.last_name,
            'prénom': self.first_name,
            'genre': self.gender,
            'anniversaire': self.birthday,
            'elo': self.elo,
            'points de tournoi': self.ranking_points
        }
        self.list_players.append(self.info_player)
        return self.list_players

    def __str__(self):
        return f"ID : {self.ID}, Nom : {self.last_name}, prénom : {self.first_name}, genre : {self.gender},anniversaire :{self.birthday}, elo : {self.elo}, points de tournoi : {self.ranking_points} "

    def __getitem__(self, choice):
        return self.list_players[choice]

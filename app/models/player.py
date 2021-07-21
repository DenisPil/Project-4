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
        Player.player_id += 1

    def __str__(self):
        return f"ID : {self.ID}, Joueur : {self.first_name} {self.last_name}, elo : {self.elo}, points de tournoi : {self.ranking_points}"

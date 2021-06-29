class Player:

    player_id = 0

    def __init__(self, first_name, last_name, gender, elo, birthday):

        Player.player_id += 1

        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.elo = elo
        self.ID = Player.player_id
        self.birthday = birthday
        self.list_players = []

    def create_dict(self):
        self.info_player = {
            'nom': self.last_name,
            'prénom': self.first_name,
            'genre': self.gender,
            'anniversaire': self.birthday,
            'elo': self.elo,
            'id': self.ID,
        }
        self.list_players.append(self.info_player)
        return self.info_player

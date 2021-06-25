class Player:

    list_players = []
    player_id = 0

    def __init__(self, first_name=None, last_name=None, gender=None, elo=None, birthday=None):

        Player.player_id += 1

        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.elo = elo
        self.ID = Player.player_id
        self.birthday = birthday

    def create_dict(self):
        self.info_player = {
            'nom': self.last_name,
            'prénom': self.first_name,
            'genre': self.gender,
            'anniversaire': self.birthday,
            'elo': self.elo,
            'id': self.ID,
        }
        Player.list_players.append(self.info_player)
        return self.info_player

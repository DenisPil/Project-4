from Player import Player


list_players = [{'nom': 'dupont', 'prénom': 'loulou', 'gender': 'Homme', 'anniversaire': '14/07/1988', 'elo': '1187', 'id': 1},
                {'nom': 'dupuit', 'prénom': 'lou', 'gender': 'Femme', 'anniversaire': '29/1999', 'elo': '1200', 'id': 2},
                {'nom': 'dubois', 'prénom': 'fifi', 'gender': 'Homme', 'anniversaire': '30/07/1967', 'elo': '1198', 'id': 3},
                {'nom': 'ducon', 'prénom': 'riri', 'gender': 'Femme', 'anniversaire': '13/07/1985', 'elo': '1245', 'id': 4},
                {'nom': 'domino', 'prénom': 'mimi', 'gender': 'Homme', 'anniversaire': '02/07/1975', 'elo': '1278', 'id': 5},
                {'nom': 'dimano', 'prénom': 'loulou', 'gender': 'Femme', 'anniversaire': '15/07/1981', 'elo': '1180', 'id': 6},
                {'nom': 'domina', 'prénom': 'jeanjean', 'gender': 'Homme', 'anniversaire': '24/07/2001', 'elo': '1210', 'id': 7},
                {'nom': 'damasio', 'prénom': 'alain', 'gender': 'Homme', 'anniversaire': '28/09/1969', 'elo': '1289', 'id': 8}]


class Player_manager():

    num_instance_player = 0

    def __init__(self): 
        pass

    def new_player(self):

        Player_manager.num_instance_player += 1

        Player.set_all_info()


p12= Player()
p1 = Player_manager()
p12.set_all_info()
print(p12.list_players)
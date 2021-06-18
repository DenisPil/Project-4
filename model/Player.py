import datetime


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

    def set_first_name(self):
        self.first_name = input("Le prénom du joueur : ")
        return self.first_name

    def set_last_name(self):
        self.last_name = input("Le nom du joueur : ")
        return self.last_name

    def set_gender(self):
        choice_gender = input("Tapez 1 si c'est un homme ou 2 si c'est une femme : ")
        if choice_gender == "1":
            self.gender = "Homme"
        else:
            self.gender = "Femme"
        return self.gender

    def set_elo(self):
        self.elo = input("Quel est l'ELO du joueur ? ")
        print(self.elo)
        return self.elo

    def set_birthday(self):
        print("entrée la date de naissance : ")
        self.birthday = input("rentrer une date de naissance dans le format suivant '01/01/1901' : ")
        try:
            datetime.datetime.strptime(self.birthday, '%d/%m/%Y')
        except ValueError:
            print(f"Veuillez saisir une date valide sous la forme 01/01/1901")
            self.birthday = input()
        return self.birthday

    def get_info_player(self):
        print(" ID : {} nom : {} prénom {}, le genre : {}, date de naissance : {}, l'ELO : {}"\
                .format(self.ID, self.last_name, self.first_name, self.gender, self.birthday, self.elo))

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

    def set_all_info(self):
        self.set_first_name()
        self.set_last_name()
        self.set_gender()
        self.set_birthday()
        self.set_elo()
        self.create_dict()

"""
j1 = Player()
j1.set_all_info()

j2 = Player()
j2.set_all_info()

j3 = Player()
j3.set_all_info()

j4 = Player()
j4.set_all_info()

j5 = Player()
j5.set_all_info()

j6 = Player()
j6.set_all_info()

j7 = Player()
j7.set_all_info()

j8 = Player()
j8.set_all_info()


print(Player.list_players)"""















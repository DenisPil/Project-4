class PlayerView:
    def __init__(self, model, control):

        self.model = model
        self.control = control
        self.first_name = 'le prénom'
        self.last_name = 'le nom'
        self.gender = 'le genre'
        self.birthday = 'la date de naissance'
        self.elo = "l'ELO"
        self.id = "l'ID"

    def new_player(self):
        print("Inscription d'un nouveau joueur.")
        print("Remplir les informations demandé.")

    def ask_info(self, info):
        print("Qu'elle est  {} du joueur : ".format(info))
        if info == self.birthday:
            print("Entrer une date dans le format suivant '01/01/1901' : ")
        if info == self.gender:
            print("Tapez 1 si c'est un homme ou 2 si c'est une femme : ")        

    def get_info(self, info, type_info):
        print("{} est {} du joueur".format(info, type_info))

    def get_all_info_player(self, id, last_name, first_name, gender, birthday, elo):
        print(" ID : {} nom : {} prénom {}, le genre : {}, date de naissance : {}, l'ELO : {}".\
                format(id, last_name, first_name, gender, birthday, elo))    
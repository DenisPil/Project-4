class TournamentView:

    def __init__(self, model, control):
        self.model = model
        self.control = control
        self.name = "nom"
        self.place = "lieu"
        self.date = "date"
        self.round = int      

    def show(self, info):
        print(info)

    new_tournament = "Création d'un nouveau tournoi.\nRemplir les informations demandé."    

    ask_rythme = "Dans qu'elle mode de jeu, sera joué le tournoi ?\n1 pour Bullet, 2 pour Blitz :"    
    rythme_bullet = "Le tournoi sera en mode Bullet, 1 minute part round !"
    rythme_Blitz = "Le tournoi sera en mode Blitz, 10 minutes part round !"

    ask_date = "Le tournoi ce déroule sur une journée ?\n 1 oui  2 non : "

    date_one_day = "entrée la date du tournoi dans le format suivant '01/01/1901' :"
    date_start = "entrée la date de début de tournoi dans le format suivant '01/01/1901' :" 
    date_end = "entrée la date de fin de tournoi dans le format suivant '01/01/1901' :"

    def ask_info(self, info):
        print("Qu'elle est  {} du tournoi : ".format(info))
    """
    def rythme(self, rtm):
        if rtm == "1":
            print("Le tournoi sera en mode Bullet, 1 minute part round !")           
        elif rtm == "2":
            print("Le tournoi sera en mode Blitz, 10 minutes part round !")

    def set_date(self, date):
        if date == '1':
            print("entrée la date du tournoi dans le format suivant '01/01/1901' : ")
        elif date == "2":
            print("entrée la date de début de tournoi et la date de fin du tournoi, dans le format suivant '01/01/1901' : ")

    """

class View:
    def __init__(self):
        pass

    def show(self, info):
        print(info)

    def show_players(self, match_num, player_1, player_2):
        print("Le Match: : {}, Le joueur 1 : {}, Le joueur 2 {}".format(match_num, player_1, player_2))

    def show_matches(self,
                     match_num,
                     player_1_first_name,
                     player_1_last_name,
                     player_2_first_name,
                     player_2_last_name
                     ):
        print("Le Match: : {}, Le joueur 1 : {}  {}, Le joueur 2 : {} {}".format(match_num,
                                                                                 player_1_first_name,
                                                                                 player_1_last_name,
                                                                                 player_2_first_name,
                                                                                 player_2_last_name
                                                                                 ))

    def check_info_player(self,
                          first_name,
                          last_name,
                          gender,
                          elo,
                          birthday
                          ):
        print("Nom : {}  {}, le genre : {}, l'anniversaire : {} l'elo : {},  ".format(first_name,
                                                                                      last_name,
                                                                                      gender,
                                                                                      birthday,
                                                                                      elo
                                                                                      ))

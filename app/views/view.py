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
        print("Le Match: : {}, Le joueur 1 : {} {}, Le joueur 2 : {} {}".format(match_num,
                                                                                player_1_first_name,
                                                                                player_1_last_name,
                                                                                player_2_first_name,
                                                                                player_2_last_name
                                                                                ))


    def show_ranking_points(self,
                            player_1_first_name,
                            player_1_last_name,
                            player_1_elo,
                            player_1_ranking_points,
                            player_2_first_name,
                            player_2_last_name,
                            player_2_elo,
                            player_2_ranking_points
                            ):
        print("Le joueur : {} {} Elo : {} Points de tournoi : {}".format(player_1_first_name,
                                                                         player_1_last_name,
                                                                         player_1_elo,
                                                                         player_1_ranking_points,

                                                                           ))
        print("Le joueur : {} {} Elo : {} Points de tournoi : {} ".format(player_2_first_name,
                                                                          player_2_last_name,
                                                                          player_2_elo,
                                                                          player_2_ranking_points,                                                                                                 
                                                                          ))
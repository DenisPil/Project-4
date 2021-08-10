class View:

    """
        Classe qui permet de tout afficher à l'utilisateur.
    """

    def __init__(self):
        pass

    def show(self, info):

        """
            Méthode qui affiche une information à l'utilisateur.

            Argument:
                info = une information pour l'utilisateur.
                ex : demander le nom d'un joueur, le lieu d'un tournoi etc...
        """

        print(info)

    def show_matches(self, match_num, player_1, player_2):

        """
            Méthode qui affiche les joueurs pour le prochain match

            Arguments:
                match_num = le numéro du match
                player_1 = le joueur numéro 1
                player_2 = le joueur numéro 2
        """

        print("Le Match: : {}, Le joueur 1 : {}, Le joueur 2 {}".format(match_num, player_1, player_2))

    def show_archived_matches(self, match_num, player_1, player_2, winner):

        """
            Méthode qui affiche les matchs archivés

            Arguments:
                match_num = le numéro du match
                player_1 = le joueur numéro 1
                player_2 = le joueur numéro 2
                winner =  le gagnant du match
        """

        print("Le Match: : {}, Le joueur 1 : {}, Le joueur 2 : {}, Le gagnant : {}".format(match_num,
                                                                                           player_1,
                                                                                           player_2,
                                                                                           winner
                                                                                           ))

    def check_info_player(self, ID, first_name, last_name, gender, elo, birthday):

        """
            Méthode qui affiche tous les attributs d'un joueur

            Arguments:
                ID = L'identifiant du joueur
                first_name = le prénom du joueur
                last_name = le nom du joueur
                gender = le genre du joueur
                elo = les points elo du joueur
                birthday = la date de naissance du joueur
        """

        print("ID : {} Nom : {}  {}, le genre : {}, l'anniversaire : {} l'elo : {},  ".format(ID,
                                                                                              first_name,
                                                                                              last_name,
                                                                                              gender,
                                                                                              birthday,
                                                                                              elo
                                                                                              ))

    def show_tournament(self, name, location, time_ctrl, start_date, end_date,):

        """
            Méthode qui affiche tous les attributs d'un tournoi

            Arguments:
                name = le nom du tournoi
                location = le lieu du tournoi
                time_ctrl = le type de partie
                start_date = date de début du tournoi
                end_date = date de fin du tournoi.
        """

        print("Le nom: {}, \nle lieu: {} \ntype de match: {} \nla date:{} - {}\n\n".format(name,
                                                                                           location,
                                                                                           time_ctrl,
                                                                                           start_date,
                                                                                           end_date,
                                                                                           ))

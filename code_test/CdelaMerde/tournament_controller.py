from model.tournament import Tournament
from controller.grab import Input
from model.round import Round


class TournamentController:


    def run(self):
        self.add_new_tournament()

    def add_new_tournament(self):
        control_input = Input()
        model_round = Round()

        name = control_input.get_input_str("le nom")
        place = control_input.get_input_str("la ville")
        time_ctrl = control_input.get_rythme("le rythme de la partie Bullet = 1, Blitz = 2")
        start_date = control_input.get_input_date("le début de tournoi")
        end_date = control_input.get_input_date("la fin de tournoi")

        tournament = Tournament(name=name, place=place, time_ctrl=time_ctrl, start_date=start_date, end_date=end_date)
        print(tournament)
    def add_player(self):
        pass




"""    print( tournament.name,
           tournament.place,
           tournament.time_ctrl,
           tournament.start_date,
           tournament.end_date
          )


"""
"""t =TournamentController()
t.run()"""
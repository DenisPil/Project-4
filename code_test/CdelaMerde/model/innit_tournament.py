from model import tournament
from view import tournament_view
from controller import grab


def innit_new_tournament():
    control = grab.Input()
    model = tournament.Tournament()
    display = tournament_view.TournamentView(model=model, control=control)
    """
    display.new_tournament()

    display.ask_info(display.name)
    control.set_info()
    control.check_input_str()
    model.name = control.info

    display.ask_info(display.place)
    control.set_info()
    control.check_input_str()
    model.place = control.info

    model.set_nb_players()

    display.ask_rythme()
    control.set_info()
    control.check_input_str()
    model.set_rythme(control.info)
    display.rythme(control.info)
    """
    display.show(display.ask_date)
    control.set_info()
    control.check_input_str()
    if control.info == "1":
        display.show(display.date_one_day)
        control.set_info()
        control.check_input_date()
        model.start_date = control.info
    else:
        display.show(display.date_start)
        control.set_info()
        control.check_input_date()
        model.start_date = control.info
        display.show(display.date_end)
        control.set_info()
        control.check_input_date()
        model.end_date = control.info

    

    """
    model.sort_elo()
    model.player_attribution()
    model.create_rounds()
    print(model.create_rounds()[0])
    model.create_dict()
    print(model.tournament_info)"""



innit_new_tournament()    
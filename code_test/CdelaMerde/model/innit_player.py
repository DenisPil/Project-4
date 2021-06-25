from model import player
from controller import grab
from view import player_view


def innit_new_player():
    control = grab.Input()
    model = player.Player()
    display = player_view.PlayerView(model=model, control=control)

    display.new_player()

    display.ask_info(display.first_name)
    control.set_info()
    control.check_input_str()
    model.first_name = control.info

    display.ask_info(display.last_name)
    control.set_info()
    control.check_input_str()
    model.last_name = control.info

    display.ask_info(display.gender)
    control.set_info()
    control.check_gender()
    model.gender = control.info

    display.ask_info(display.birthday)
    control.set_info()
    control.check_input_date()
    model.birthday = control.info

    display.ask_info(display.elo)
    control.set_info()
    control.check_input_str()
    model.elo = control.info

    display.get_all_info_player(
                                    model.ID,
                                    model.last_name,
                                    model.first_name,
                                    model.gender,
                                    model.birthday,
                                    model.elo
                                )

    model.create_dict()


innit_new_player()

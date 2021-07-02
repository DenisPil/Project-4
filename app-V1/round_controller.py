from model.round import Round
from model.tournament import Tournament
from controller.grab import Input
from player_controller import PlayerController


class RoundController:
    def __init__(self):
        pass

    def start_round(self):
        start = Round()
        return start

    def end_round(self):
        end = Round()
        return end

    def winner(self, list_round):
        round = Round()
        win = round.get_winner(list_round)
        return win

"""
t = RoundController()
"""

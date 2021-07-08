from player_controller import PlayerController
from tournament_controller import Tournament

class HomeController:
    def __init__(self):
        self.menu = "1,2,3"

    def run(self):
        print("run")
        running = True
        while running:
            print(self.menu)
            val = input("entrez une valeur")
            val = int(val)
            if val == 1:
                player_ctrl = PlayerController()
                player = player_ctrl.run()
                # self.tournament.add(player)
            else:
                running = False

t = HomeController()
t.run()

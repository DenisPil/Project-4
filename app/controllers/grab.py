import datetime
from views.view import View

class Input:

    def __init__(self):
        self.view = View()

        self.display_info = {"error date": "La date n'est pas valide :",
                             "error": "L'information n'est pas valide :"
                             }

    def get_input_str(self):
        while True:
            try:
                value = str(input("-->"))
                break
            except ValueError:
                self.view.show(self.display_info["error"])
        return value.capitalize()

    def get_input_int(self):
        while True:
            try:
                value = int(input("-->"))
                break
            except ValueError:
                self.view.show(self.display_info["error"])
        return value

    def get_input_date(self):
        while True:
            try:
                value = str(input("-->"))
                datetime.datetime.strptime(value, '%d/%m/%Y')
                break
            except ValueError:
                self.view.show(self.display_info["error date"])
        return value

    def get_gender(self):
        while True:
            try:
                value = input("-->")
                if value.lower() == "h":
                    value = "Homme"
                    break
                elif value.lower() == "f":
                    value = "Femme"
                    break
            except ValueError:
                self.view.show(self.display_info["error"])
        return value

    def get_rythme(self):
        rythme = str
        while True:
            try:
                value = int(input("-->"))
                if value == 1:
                    rythme = "Bullet"
                    break
                elif value == 2:
                    rythme = "Blitz"
                    break
            except ValueError:
                self.view.show(self.display_info["error"])
        return rythme

    def set_date(self):
        while True:
            try:
                value = input("-->")
                if value == '1':
                    break
                elif value == "2":
                    break
            except ValueError:
                self.view.show(self.display_info["error"])
        return value

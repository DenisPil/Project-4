import datetime


class Input:

    def __init__(self):
        pass

    def get_input_str(self, info):
        value = ""
        while value == "":
            print(info)
            value = input()
        return value.capitalize()

    def get_input_int(self, info):
        value = 0
        while value == 0:
            print(info)
            value = input()
        return value

    def get_input_date(self, info):
        date = False
        while date == False:
            print(info)
            value = input()
            try:
                datetime.datetime.strptime(value, '%d/%m/%Y')
                date = True
            except ValueError:
                value = input()
        return value

    def get_gender(self, info):
        print(info)
        value = input()

        if value.lower() == "h":
            value = "Homme"
        elif value.lower() == "f":
            value = "Femme"
        return value

    def get_rythme(self, info): 
        print(info)
        value = input()

        if value == "1":
            value = "Bullet"
        elif value == "2":
            value = "Blitz"
        return value
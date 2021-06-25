import datetime


class Input:

    def __init__(self, info=None):
        self.info = info

    def set_info(self):
        self.info = input()
        return self.info

    def check_input_str(self):
        while self.info == "":
            print("Erreur, il faut minimum un caractère !!")
            self.info = input()

    def check_input_date(self):
        date = False
        while date == False:
            try:
                datetime.datetime.strptime(self.info, '%d/%m/%Y')
                date = True
            except ValueError:
                print(f"Veuillez saisir une date valide sous la forme 01/01/1901")
                self.info = input()

    def check_gender(self):
        if self.info == "1":
            gender = "Homme"
            self.info = gender

        elif self.info == "2":
            gender = "Femme"
            self.info = gender

    def set_rythme(self): 
        if self.info == "1":
            rythme = "Bullet"
            self.info = rythme

        elif self.info == "2":
            rythme = "Blitz"
            self.info = rythme
        

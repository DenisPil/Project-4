
class MenuEntry:
    def __init__(self, option, handler):
        self.option = option
        self.handler = handler

    # affiche une représentation textuel d'un objet (pour debug)
    def __repr__(self):
        return f"MenuEntry({self.option}, {self.handler})"

    def __str__(self):
        return str(self.option)


class Menu:

    def __init__(self):
        self.entries = {}
        self.autokey = 1

    def add(self, key, option, handler):
        if key == "auto":
            key = str(self.autokey)
            self.autokey += 1

        self.entries[str(key)] = MenuEntry(option, handler)

    def header(self, header,  header_name):

        self.entries[str(header)] = MenuEntry(header_name, None)   
          

    # renvoie un itérrateur a travers les clés et les entrées dans mon menu
    def items(self):
        return self.entries.items()    

    def __contains__(self, choice):
        return str(choice) in self.entries

    def __getitem__(self, choice):
        return self.entries[choice]


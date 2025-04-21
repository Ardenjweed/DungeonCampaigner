from token_creation import TokenCreation

class Token:
    def __init__(self):
        self.profile = None
        self.name = ""
        self.description = ""
        self.notes = ""
        self.initiative = 0
        self.health = 0
        self.ac = 0
        self.weapon = None
        self.strength = 0
        self.dexterity = 0
        self.constitution = 0
        self.intelligence = 0
        self.wisdom = 0
        self.charisma = 0
        self.create_token()

    def create_token(self):
        token_window = TokenCreation(self)
        token_window.exec()

    def get_pfp(self):
        return self.profile


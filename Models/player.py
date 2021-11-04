class Player(object):

    connexion = None

    def __init__(self, id=0, familly_name=None, first_name=None, rank=None):
        self.id = id
        self.familly_name = familly_name
        self.first_name = first_name
        self.rank = rank

        # All tournaments which player is resgistered
        self.tournaments = {}

















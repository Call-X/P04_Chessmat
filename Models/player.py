class Player(object):

    connexion = None

    def __init__(
        self,
        id=0,
        familly_name=None,
        first_name=None,
        age=None,
        gender=None,
        rank=None,
        point=0,
    ):
        self.id = id
        self.familly_name = familly_name
        self.first_name = first_name
        self.age = age
        self.gender = gender
        self.rank = rank
        self.point = point

        # All tournaments which player is resgistered
        self.tournaments = {}

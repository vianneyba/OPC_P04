import uuid


class Tournament:
    """Model d'un tournoi"""
    def __init__(self, tournament_dic={}):
        self.id = str(uuid.uuid1())
        self.rounds = []
        self.players = []
        for attr_name, attr_value in tournament_dic.items():
            setattr(self, attr_name, attr_value)

    def serialize(self):
        players_id = []
        for player in self.players:
            players_id.append(player.id)

        serialized = {
            'id': self.id,
            'name': self.name,
            'place': self.place,
            'start_date': self.start_date,
            'nbr_days': self.nbr_days,
            'nbr_rounds': self.nbr_rounds,
            'ctr_time': self.ctr_time,
            'description': self.description,
            'players': self.get_players_id(),
            'rounds': self.get_rounds_id()
        }
        return serialized

    def get_players_id(self):
        players_id = []
        for player in self.players:
            players_id.append(player.id)
        return players_id

    def get_rounds_id(self):
        rounds_id = []
        for round_t in self.rounds:
            rounds_id.append(round_t.id)
        return rounds_id

    def nbr_players(self):
        return len(self.players)

    def __str__(self):
        return(
            f'id: {self.id}\n'
            f'nom: {self.name}\n'
            f'lieu: {self.place}\n'
        )

    def add_player(self, new_player):
        self.players.append(new_player)

    def export_players(self):
        players = []
        for player in self.players:
            players.append(player.serialize())
        return players

    def add_round(self, round):
        self.rounds.append(round)
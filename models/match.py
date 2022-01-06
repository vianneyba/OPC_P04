import uuid


class Match:
    def __init__(self):
        self.id = str(uuid.uuid1())
        self.player_one = None
        self.player_one_pt = 0
        self.player_two = None
        self.player_two_pt = 0

    def serialize(self):
        serialized = {
            'id': self.id,
            'players': self.get_tuple_players()
        }
        return serialized

    def get_tuple_players(self):
        p_one = [self.player_one.id, self.player_one_pt]
        p_two = [self.player_two.id, self.player_two_pt]
        return (p_one, p_two)

    def add_player(self, player, point=0):
        if self.player_one is None:
            self.player_one = player
            self.player_one_pt = point
        else:
            self.player_two = player
            self.player_two_pt = point

    def __str__(self):
        return f'{self.player_one.firstname} ({self.player_one.rating}) VS {self.player_two.firstname} ({self.player_two.rating})'

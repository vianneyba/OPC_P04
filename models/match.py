import uuid


class Match:

    all_matches = []

    def __init__(self, match_dic={}):
        self.player_one = None
        self.player_two = None
        self.player_one_pt = 0
        self.player_two_pt = 0
        if match_dic:
            self.id = match_dic['id']
        else:
            self.id = str(uuid.uuid1())
        self.all_matches.append(self)

    def serialize(self):
        serialized = {
            'id': self.id,
            'players': self.get_tuple_players()
        }
        return serialized

    def add_point(self, player_selected: int, pts: float):
        if player_selected == 1:
            self.player_one_pt += pts
        elif player_selected == 2:
            self.player_two_pt += pts
        elif player_selected == 3:
            self.player_one_pt += pts
            self.player_two_pt += pts

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
        return (
            f'{self.player_one.firstname} ({self.player_one.rating} '
            f'avec {self.player_one_pt})'
            f'VS'
            f'{self.player_two.firstname} ({self.player_two.rating} '
            f'avec {self.player_two_pt})'
        )

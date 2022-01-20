import uuid
from dateutil.parser import parse
from datetime import timedelta


class Tournament:

    all_tournaments = []

    def __init__(self, tournament_dic={}):
        self.id = str(uuid.uuid1())
        self.rounds = []
        self.players = []
        for attr_name, attr_value in tournament_dic.items():
            setattr(self, attr_name, attr_value)
        self.all_tournaments.append(self)

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

    def get_players_by_points(self):
        players = sorted(self.players, key=lambda x: x.points)
        return players

    def get_players_by_rating(self):
        players = sorted(self.players, key=lambda x: x.rating)
        return players

    def get_players_by_lastname(self):
        players = sorted(self.players, key=lambda x: x.lastname)
        return players

    def get_rounds_id(self):
        rounds_id = []
        for round_t in self.rounds:
            rounds_id.append(round_t.id)
        return rounds_id

    def count_players(self):
        return len(self.players)

    def __str__(self):
        return(
            f'id: {self.id}\n'
            f'nom: {self.name}\n'
            f'lieu: {self.place}\n'
        )

    def add_player(self, new_player):
        self.players.append(new_player)

    def get_players(self):
        return self.players

    def get_last_round(self):
        for round in self.rounds:
            if round.end_date is None:
                return round

    def is_finish(self):
        if len(self.rounds) == 0:
            return False
        for round in self.rounds:
            if round.end_date is None:
                return False
        return True

    def add_round(self, round):
        self.rounds.append(round)

    def end_date(self):
        d = parse(self.start_date, fuzzy=False)
        new_d = d + timedelta(days=self.nbr_days-1)
        return new_d.strftime("%d/%m/%Y")

    def get_rounds(self):
        return self.rounds

    def get_all_matches(self):
        list_matches = []
        for r in self.rounds:
            for match in r.matches:
                list_matches.append(match)

        return list_matches

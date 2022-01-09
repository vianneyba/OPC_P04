import uuid
from datetime import datetime


class Round:

    all_rounds = []

    def __init__(self, round_dic={}):
        self.id = str(uuid.uuid1())
        for attr_name, attr_value in round_dic.items():
            setattr(self, attr_name, attr_value)
        self.matchs = []
        self.start_date = datetime.now()
        self.end_date = None
        self.all_rounds.append(self)

    def serialize(self):
        serialized = {
            'id': self.id,
            'name': self.name,
            'start_date': self.start_date,
            'end_date': self.end_date,
            'matchs': self.get_id_rounds()
        }
        return serialized

    def add_match(self, match):
        self.matchs.append(match)

    def get_id_rounds(self):
        ids = []
        for match in self.matchs:
            ids.append(match.id)
        return ids

    def __str__(self):
        return f'id: {self.id}, name: {self.name}'

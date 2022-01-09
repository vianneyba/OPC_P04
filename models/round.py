import uuid
from datetime import datetime
from dateutil.parser import parse


class Round:

    all_rounds = []

    def __init__(self, round_dic={}):
        self.id = str(uuid.uuid1())
        self.start_date = datetime.now()
        self.end_date = None
        for attr_name, attr_value in round_dic.items():
            if attr_name == 'start_date':
                self.start_date = parse(attr_value, fuzzy=False)
            else:
                setattr(self, attr_name, attr_value)
        self.matchs = []
        self.all_rounds.append(self)

    def serialize(self):
        serialized = {
            'id': self.id,
            'name': self.name,
            'start_date': self.start_date.strftime("%d/%m/%Y"),
            'end_date': self.end_date,
            'matchs': self.get_id_rounds()
        }
        return serialized

    def add_match(self, match):
        self.matchs.append(match)

    def set_start_date(self, start_date):
        self.start_date = parse(start_date, fuzzy=False)

    def get_id_rounds(self):
        ids = []
        for match in self.matchs:
            ids.append(match.id)
        return ids

    def __str__(self):
        return f'id: {self.id}, name: {self.name}'

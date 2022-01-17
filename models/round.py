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
            elif attr_name == 'end_date' and attr_value is not None:
                self.end_date = parse(attr_value, fuzzy=False)
            else:
                setattr(self, attr_name, attr_value)
        self.matches = []
        self.all_rounds.append(self)

    def serialize(self):
        if self.end_date:
            end_date = self.end_date.strftime("%H:%M %d/%m/%Y")
        else:
            end_date = None
        serialized = {
            'id': self.id,
            'name': self.name,
            'start_date': self.start_date.strftime("%H:%M %d/%m/%Y"),
            'end_date': end_date,
            'matches': self.get_id_rounds()
        }
        return serialized

    def add_match(self, match):
        self.matches.append(match)

    def set_start_date(self, start_date):
        self.start_date = parse(start_date, fuzzy=False)

    def get_id_rounds(self):
        ids = []
        for match in self.matches:
            ids.append(match.id)
        return ids

    def finish(self):
        self.end_date = datetime.now()

    def __str__(self):
        return f'id: {self.id}, name: {self.name}'

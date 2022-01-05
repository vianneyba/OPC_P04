import uuid
from datetime import datetime


class Round:
    def __init__(self, name):
        self.id = str(uuid.uuid1())
        self.name = name
        self.start_date = datetime.now()
        self.end_date = None
        self.matchs = []

    def serialize(self):
        serialized = {
            'id': self.id,
            'name': self.name,
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

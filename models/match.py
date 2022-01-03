import uuid

class Match:
    def __init__(self, match):
        self.id = str(uuid.uuid1())
        for attr_name, attr_value in round.items():
            setattr(self, attr_name, attr_value)
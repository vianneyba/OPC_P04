from datetime import datetime
import uuid

class Tournament:
    """Model d'un tournoi"""
    def __init__(self, tournament_dic):
        self.id = str(uuid.uuid1())
        for attr_name, attr_value in tournament_dic.items():
            setattr(self, attr_name, attr_value)
    
    def serialize(self):
        serialized = {
            'id': self.id,
            'name': self.name,
            'place': self.place,
            'start_date': self.start_date,
            'nbr_days': self.nbr_days,
            'nbr_rounds':self.nbr_rounds,
            'ctr_time': self.ctr_time,
            'description' : self.description,
            'players': self.players
        }
        return serialized
    
    def nbr_players(self):
        return len(self.players)

    def __str__(self):
        return(
            f'id: {self.id}\n'
            f'nom: {self.name}\n'
            f'lieu: {self.place}\n'
        )
import uuid


class Player:

    all_players = []

    def __init__(self, player_dic={}):
        self.id = str(uuid.uuid1())
        for attr_name, attr_value in player_dic.items():
            setattr(self, attr_name, attr_value)
        self.all_players.append(self)

    def serialize(self):
        serialized = {
            'id': self.id,
            'firstname': self.firstname,
            'lastname': self.lastname,
            'birthday': self.birthday,
            'gender': self.gender,
            'rating': self.rating
        }
        return serialized

    def __str__(self):
        return(
            f'id: {self.id}\n'
            f'prénom: {self.firstname}\n'
            f'nom: {self.lastname}\n'
            f'genre: {self.gender}\n'
            f'classement: {self.rating}'
            f'classement: {self.birthday}'
        )

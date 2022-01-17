from tinydb import TinyDB, Query

db = TinyDB('db.json')


class Management:
    @classmethod
    def get_by_id(self, my_id):
        q = Query()
        return self.table.search(q.id == my_id)[0]

    @classmethod
    def get_all(self):
        return self.table.all()


class PlayerManagement:
    table = db.table('players')

    @classmethod
    def get_all(self, type_order='by_last_name'):
        if type_order == 'by_last_name':
            return sorted(self.table.all(), key=lambda k: k['lastname'])
        elif type_order == 'by_rating':
            return sorted(self.table.all(), key=lambda k: k['rating'])

    @classmethod
    def get_by_id(self, player_id):
        q = Query()
        return self.table.search(q.id == player_id)[0]

    @classmethod
    def get_by_lastname_and_firstname(self, firstname, lastname):
        q = Query()
        return self.table.search((q.lastname == lastname) & (q.firstname == firstname))[0]

    @classmethod
    def save(self, user):
        try:
            self.get_by_id(user['id'])
            Player = Query()
            self.table.update(user, Player.id == user['id'])
        except IndexError:
            self.table.insert(user)


class TournamentManagement(Management):
    table = db.table('tournaments')

    @classmethod
    def get_all(self):
        return self.table.all()

    @classmethod
    def get_by_name(self, name):
        q = Query()
        return self.table.search(q.name == name)[0]

    @classmethod
    def save(self, tournament):
        try:
            self.get_by_id(tournament['id'])
            Tournament = Query()
            self.table.update(tournament, Tournament.id == tournament['id'])
        except IndexError:
            self.table.insert(tournament)


class RoundManagement(Management):
    table = db.table('rounds')

    @classmethod
    def save(self, my_round):
        try:
            self.get_by_id(my_round['id'])
            Round = Query()
            self.table.update(my_round, Round.id == my_round['id'])
        except IndexError:
            self.table.insert(my_round)

    @classmethod
    def get_all(self):
        return self.table.all()


class MatchManagement(Management):
    table = db.table('matches')

    @classmethod
    def save(self, match):
        try:
            self.get_by_id(match['id'])
            Match = Query()
            self.table.update(match, Match.id == match['id'])
        except IndexError:
            self.table.insert(match)

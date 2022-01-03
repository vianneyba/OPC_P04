from tinydb import TinyDB, Query
import uuid
import copy

db = TinyDB('db.json')

class PlayerManagement:
    table = db.table('players')

    @classmethod
    def get_all(self, type_order='by_last_name'):
        all =  self.table.all()

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
        self.table.insert(user)

class TournamentManagement:
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
        self.table.insert(tournament)
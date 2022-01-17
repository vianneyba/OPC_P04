from models.linktracking import LinkTracking
from controllers.validation import Validation
from models.player import Player
from services.services import PlayerManagement as Player_M


class PlayerController:

    lnk = LinkTracking()
    view = None

    def __init__(self, view):
        self.view = view

    @classmethod
    def get_by_id(cls, id_player):
        for player in Player.all_players:
            if player.id == id_player:
                return player

    @classmethod
    def get_all_players_by_rating(self):
        return sorted(Player.all_players, key=lambda x: x.rating)

    def get_player_by_name_and_birthday(player_searched: Player):
        for player in Player.all_players:
            if (
                player.firstname == player_searched['firstname']
                and player.lastname == player_searched['lastname']
                and player.birthday == player_searched['birthday']
            ):
                return player

    @classmethod
    def get_all_players_by_name(self):
        return sorted(Player.all_players, key=lambda x: x.lastname)

    @classmethod
    def import_all_players(self):
        Player.all_players = []
        players = Player_M.get_all()
        for player in players:
            Player(player)

    @classmethod
    def add_player(self, view, nbr=1):
        self.view = view
        player = {}

        view.display_player_new(nbr)

        player['firstname'] = self.field_firstname(self)
        player['lastname'] = self.field_lastname(self)

        self.lnk.init()
        while self.lnk.next is False:
            message = 'date de naissance (jj/mm/yyyy): '
            player['birthday'] = view.field_text(self.lnk, message)
            Validation.tournament_date_start(player['birthday'], self.lnk)

        player_searched = self.get_player_by_name_and_birthday(player)
        if player_searched is not None:
            return player_searched

        self.lnk.init()
        while self.lnk.next is False:
            message = 'entrer son sexe (H/F): '
            player['gender'] = view.field_text(self.lnk, message)
            Validation.gender(player['gender'], self.lnk)

        player['rating'] = self.field_rating(self)

        return Player(player)

    def field_firstname(self, txt=None):
        self.lnk.init()
        while self.lnk.next is False:
            if txt:
                message = f'nouveau prénom ({txt}): '
            else:
                message = 'entrer son prénom: '
            firstname = self.view.field_text(self.lnk, message)
            Validation.first_name(firstname, self.lnk)
        return firstname

    def field_lastname(self, txt=None):
        self.lnk.init()
        while self.lnk.next is False:
            if txt:
                message = f'nouveau nom ({txt}): '
            else:
                message = 'entrer son nom: '
            lastname = self.view.field_text(self.lnk, message)
            Validation.last_name(lastname, self.lnk)
        return lastname

    def field_rating(self, txt=None):
        self.lnk.init()
        while self.lnk.next is False:
            if txt:
                message = f'nouveau classement ({txt}): '
            else:
                message = 'entrer son classement: '
            rating = self.view.field_text(self.lnk, message)
            rating = Validation.rating(rating, self.lnk)
        return rating

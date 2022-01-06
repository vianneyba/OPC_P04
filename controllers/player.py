from models.linktracking import LinkTracking
from controllers.validation import Validation
from models.player import Player


class PlayerController:

    lnk = LinkTracking()

    @classmethod
    def add_player(self, view, nbr=1):
        player = Player()

        view.display_player_new(nbr)

        self.lnk.init()
        while self.lnk.next is False:
            message = 'entrer son prénom: '
            player.firstname = view.field_text(self.lnk, message)
            Validation.first_name(player.firstname, self.lnk)

        self.lnk.init()
        while self.lnk.next is False:
            message = 'entrer son nom: '
            player.lastname = view.field_text(self.lnk, message)
            Validation.last_name(player.lastname, self.lnk)

        self.lnk.init()
        while self.lnk.next is False:
            message = 'entrer son sexe (H/F): '
            player.gender = view.field_text(self.lnk, message)
            Validation.gender(player.gender, self.lnk)

        self.lnk.init()
        while self.lnk.next is False:
            message = 'date de naissance (jj/mm/yyyy): '
            player.birthday = view.field_text(self.lnk, message)
            Validation.tournament_date_start(player.birthday, self.lnk)

        self.lnk.init()
        while self.lnk.next is False:
            message = 'entrer son classement: '
            rating = view.field_text(self.lnk, message)
            player.rating = Validation.rating(rating, self.lnk)

        return player

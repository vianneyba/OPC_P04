from models.linktracking import LinkTracking
from controllers.validation import Validation
from models.player import Player

class PlayerController:
    linktracking = LinkTracking()

    @classmethod
    def add_player(self, menu_view, nbr=1):
        new_player = Player()

        menu_view.display_player_new(nbr)
    
        self.linktracking.init()
        while self.linktracking.next == False:
            new_player.firstname = menu_view.display_player_first_name(self.linktracking)
            Validation.first_name(new_player.firstname, self.linktracking)

        self.linktracking.init()
        while self.linktracking.next == False:
            new_player.lastname = menu_view.display_player_last_name(self.linktracking)
            Validation.last_name(new_player.lastname, self.linktracking)

        self.linktracking.init()
        while self.linktracking.next == False:
            new_player.gender = menu_view.display_player_gender(self.linktracking)
            Validation.gender(new_player.gender, self.linktracking)
        
        self.linktracking.init()
        while self.linktracking.next == False:
            new_player.birthday = menu_view.display_player_birthday(self.linktracking)
            Validation.tournament_date_start(new_player.birthday, self.linktracking)

        self.linktracking.init()
        while self.linktracking.next == False:
            rating = menu_view.display_player_rating(self.linktracking)
            new_player.rating = Validation.rating(rating, self.linktracking)          

        return new_player
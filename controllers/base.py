from models.player import Player
from models.tournament import Tournament
from models.player import Player
from services.services import PlayerManagement, TournamentManagement
from controllers.player import PlayerController
from models.linktracking import LinkTracking

class Controller:
    def __init__(self, menu_view):
        """"""
        self.menu_view = menu_view
        self.linktracking = LinkTracking()

    def run(self):
        while True:
            if self.linktracking.page == '':
                select= self.menu_view.display_menu()
                if select == '2': self.linktracking.page = 'player'
                elif select.lower() == 'q': break

            if self.linktracking.page == 'player':
                select = self.menu_view.display_menu_player()
                if select == '1': self.linktracking.sub_page = 'add_player'
                elif select == '2': self.linktracking.sub_page = 'list_player_by_last_name'
                elif select == '3': self.linktracking.sub_page = 'list_player_by_rating'
                elif select.lower() == 'q': 
                    self.linktracking.page = ''
                    self.linktracking.sub_page = ''

                if self.linktracking.sub_page == 'add_player':
                    new_player= PlayerController.add_player(self.menu_view)
                    PlayerManagement.save(new_player.serialize())
                elif self.linktracking.sub_page == 'list_player_by_last_name':
                    players = PlayerManagement.get_all('by_last_name')
                    self.menu_view.display_list_players(players)
                elif self.linktracking.sub_page == 'list_player_by_rating':
                    players = PlayerManagement.get_all('by_rating')
                    self.menu_view.display_list_players(players)                
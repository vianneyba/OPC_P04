from services.services import PlayerManagement
from controllers.player import PlayerController
from controllers.tournament import TournamentController as Tournament_C
from models.linktracking import LinkTracking


class Controller:
    def __init__(self, menu_view):
        self.list_tournament = []
        self.menu_view = menu_view
        self.lnk = LinkTracking()

    def run(self):
        while True:
            if self.lnk.page == '':
                select = self.menu_view.display_menu()
                if select == '1':
                    self.lnk.page = 'new_tournament'
                elif select == '2':
                    self.lnk.page = 'player'
                elif select == '8':
                    self.lnk.page = 'import'
                elif select == '9':
                    self.lnk.page = 'export'
                elif select.lower() == 'q':
                    break

            if self.lnk.page == 'new_tournament':
                new_tournament = Tournament_C.add_tournament(self.menu_view)
                self.list_tournament.append(new_tournament)
                self.lnk.page = ''
            elif self.lnk.page == 'player':
                select = self.menu_view.display_menu_player()
                if select == '1':
                    self.lnk.sub_page = 'add_player'
                elif select == '2':
                    self.lnk.sub_page = 'list_player_by_last_name'
                elif select == '3':
                    self.lnk.sub_page = 'list_player_by_rating'
                elif select.lower() == 'q':
                    self.lnk.page = ''
                    self.lnk.sub_page = ''

                if self.lnk.sub_page == 'add_player':
                    new_player = PlayerController.add_player(self.menu_view)
                    PlayerManagement.save(new_player.serialize())
                elif self.lnk.sub_page == 'list_player_by_last_name':
                    players = PlayerManagement.get_all('by_last_name')
                    self.menu_view.display_list_players(players)
                elif self.lnk.sub_page == 'list_player_by_rating':
                    players = PlayerManagement.get_all('by_rating')
                    self.menu_view.display_list_players(players)
            elif self.lnk.page == 'export':
                for tournament in self.list_tournament:
                    Tournament_C.save(tournament)
                self.lnk.page = ''
            elif self.lnk.page == 'import':
                self.lnk.page = ''

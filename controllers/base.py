from services.services import PlayerManagement
from controllers.player import PlayerController as Player_C
from controllers.tournament import TournamentController as Tournament_C
from models.linktracking import LinkTracking
from models.tournament import Tournament


class Controller:
    def __init__(self, menu_view):
        self.view = menu_view
        self.lnk = LinkTracking()

    def run(self):
        while True:
            if self.lnk.page == '':
                select = self.view.display_menu()
                if select == '1':
                    self.lnk.page = 'new_tournament'
                elif select == '2':
                    self.lnk.page = 'player'
                elif select == '3':
                    self.lnk.page = 'tournament'
                elif select == '8':
                    self.lnk.page = 'import'
                elif select == '9':
                    self.lnk.page = 'export'
                elif select.lower() == 'q':
                    break

            if self.lnk.page == 'new_tournament':
                Tournament_C.add_tournament(self.view)
                self.lnk.page = ''
            elif self.lnk.page == 'player':
                select = self.view.display_menu_player()
                if select == '1':
                    self.lnk.sub_page = 'add_player'
                elif select == '2':
                    self.lnk.sub_page = 'list_player_by_last_name'
                elif select == '3':
                    self.lnk.sub_page = 'list_player_by_rating'
                elif select == '4':
                    self.lnk.sub_page = 'edit_player'
                elif select.lower() == 'q':
                    self.lnk.page = ''
                    self.lnk.sub_page = ''

                if self.lnk.sub_page == 'add_player':
                    new_player = Player_C.add_player(self.view)
                    PlayerManagement.save(new_player.serialize())
                elif self.lnk.sub_page == 'list_player_by_last_name':
                    players = Player_C.get_all_players_by_name()
                    self.view.display_list_players(players)
                elif self.lnk.sub_page == 'list_player_by_rating':
                    players = Player_C.get_all_players_by_rating()
                    self.view.display_list_players(players)
                elif self.lnk.sub_page == 'edit_player':
                    players = Player_C.get_all_players_by_name()
                    self.view.display_list_players(players, True)
                    number = int(self.view.select_player()) - 1
                    p_select = players[number]

                    player_c = Player_C(self.view)
                    while True:
                        select = self.view.display_edit_player()
                        if select == '1':
                            p_select.firstname = player_c.field_firstname(
                                p_select.firstname
                            )
                        elif select == '2':
                            p_select.lastname = player_c.field_lastname(
                                p_select.lastname
                            )
                        elif select == '4':
                            p_select.rating = player_c.field_rating(
                                p_select.rating
                            )
                        elif select == 'q':
                            self.lnk.sub_page = ''
                            break

            elif self.lnk.page == 'tournament':
                select = self.view.display_menu_tournament()
                if select == '1':
                    self.lnk.sub_page = 'new_tournament'
                elif select == '2':
                    self.lnk.sub_page = 'tournament_list'
                elif select.lower() == 'q':
                    self.lnk.page = ''
                    self.lnk.sub_page = ''

                if self.lnk.sub_page == 'new_tournament':
                    Tournament_C.add_tournament(self.view)
                    self.lnk.page = ''
                elif self.lnk.sub_page == 'tournament_list':
                    t_id = Tournament_C.view_tournaments(self.view)
                    if t_id == 'q':
                        self.lnk.sub_page = ''
                    else:
                        t_id = int(t_id) - 1
                        Tournament_C.menu_edit_tournament(
                            self.view, Tournament.all_tournaments[t_id]
                        )
                    self.lnk.sub_page = ''

            elif self.lnk.page == 'export':
                for tournament in Tournament.all_tournaments:
                    Tournament_C.save(tournament)
                self.lnk.page = ''
            elif self.lnk.page == 'import':
                Player_C.import_all_players()
                Tournament_C.import_all_tournament()
                self.lnk.page = ''

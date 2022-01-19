from services.services import PlayerManagement
from controllers.player import PlayerController as Player_C
from controllers.tournament import TournamentController
from models.linktracking import LinkTracking
from models.tournament import Tournament


class Controller:
    def __init__(self, menu_view):
        self.view = menu_view
        self.lnk = LinkTracking()
        self.tc = TournamentController(self.view)

    def rapport_menu(self):
        select = self.view.display_menu_rapport()

        if select == '1':
            self.lnk.sub_page = self.view.display_menu_order()
            if self.lnk.sub_page == '1':
                players = Player_C.get_all_players_by_rating()
                self.view.display_list_players(players)
            elif self.lnk.sub_page == '2':
                players = Player_C.get_all_players_by_name()
                self.view.display_list_players(players)
            elif self.lnk.sub_page == 'q':
                self.select = ''
        elif select == '2':
            while True:
                tournaments = Tournament.all_tournaments
                self.view.display_list_tournament_online(tournaments)
                t_id = self.view.display_select_tournament()

                try:
                    t_id = int(t_id) - 1
                    players = tournaments[t_id].get_players()
                    print(players)

                    self.lnk.sub_page = self.view.display_menu_order()
                    if self.lnk.sub_page == '1':
                        players = sorted(players, key=lambda x: x.rating)
                        self.view.display_list_players(players)
                        input("suite")
                    elif self.lnk.sub_page == '2':
                        players = sorted(players, key=lambda x: x.lastname)
                        self.view.display_list_players(players)
                        input("suite")
                except ValueError:
                    break
        elif select == '3':
            tournaments = Tournament.all_tournaments
            self.view.display_list_tournament_online(tournaments)
            input("suite")
        elif select == 'q':
            self.lnk.page = ''

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
                elif select == '4':
                    self.lnk.page = 'rapport'
                elif select == '8':
                    self.lnk.page = 'import'
                elif select == '9':
                    self.lnk.page = 'export'
                elif select.lower() == 'q':
                    break

            if self.lnk.page == 'new_tournament':
                self.tc.add_tournament(self.view)
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
                    self.view.display_list_players(players)
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
                    self.tc.add_tournament(self.view)
                    self.lnk.page = ''
                elif self.lnk.sub_page == 'tournament_list':
                    t_id = self.tc.view_tournaments(self.view)
                    if t_id == 'q':
                        self.lnk.sub_page = ''
                    else:
                        t_id = int(t_id) - 1
                        self.tc.menu_edit_tournament(
                            self.view, Tournament.all_tournaments[t_id]
                        )
                    self.lnk.sub_page = ''
            elif self.lnk.page == 'rapport':
                self.rapport_menu()
            elif self.lnk.page == 'export':
                for tournament in Tournament.all_tournaments:
                    self.tc.save(tournament)
                self.lnk.page = ''
            elif self.lnk.page == 'import':
                Player_C.import_all_players()
                self.tc.import_all_tournament()
                self.lnk.page = ''

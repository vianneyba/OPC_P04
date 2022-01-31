from controllers.player import PlayerController
from controllers.tournament import TournamentController
from models.tournament import Tournament
from models.player import Player
from config import DEFAULT_NBR_PLAYER as NBR_PLAYER
import os


class Controller:
    def __init__(self, menu_view):
        self.view = menu_view
        self.tc = TournamentController(self.view)
        self.pc = PlayerController(self.view)
        self.menu = self.view.display_menu()
        self.select = 0
        self.page = 'home'
        self.player_selected = None
        self.ts = None

    def go_menu_home(self):
        self.page = 'home'
        self.menu = self.view.display_menu()

    def go_menu_player(self):
        self.page = 'player'
        self.menu = self.view.display_menu_player()

    def go_menu_rapport(self):
        self.page = 'rapport'
        self.menu = self.view.display_menu_rapport()

    def menu_home(self):
        if self.select == '1':
            self.tc.add_tournament()
        elif self.select == '2':
            self.go_menu_player()
        elif self.select == '3':
            self.page = 'tournament'
            self.menu = self.view.display_menu_tournament()
        elif self.select == '4':
            self.go_menu_rapport()
        elif self.select == '8':
            self.pc.import_all_players()
            self.tc.import_all_tournament()
            print(self.view.display_load())
        elif self.select == '9':
            for tournament in Tournament.all_tournaments:
                self.tc.save(tournament)
            for player in Player.all_players:
                self.pc.save(player)
            print(self.view.display_save())
        elif self.select == '10':
            cmd = 'flake8 --format=html --htmldir=flake8_report'
            os.system(cmd)
            self.go_menu_home()
        elif self.select.lower() == 'q':
            self.page = 'quit'

    def menu_player(self):
        if self.select == '1':
            self.pc.add_player()
        elif self.select == '2':
            players = self.pc.get_all_players_by_name()
            self.view.display_list_players(players)
        elif self.select == '3':
            players = self.pc.get_all_players_by_rating()
            self.view.display_list_players(players)
        elif self.select == '4':
            players = self.pc.get_all_players_by_name()
            self.page = 'edit_player'
            self.view.display_list_players(players)
            try:
                number = int(self.view.select_player()) - 1
                self.player_selected = players[number]
                self.menu = self.view.display_edit_player()
            except ValueError:
                self.go_menu_player()
        elif self.select == '5':
            self.pc.import_all_players()
        elif self.select.lower() == 'q':
            self.player_selected = None
            self.go_menu_home()

    def menu_tournament(self):
        if self.select == '1':
            self.tc.add_tournament()
        elif self.select == '2':
            if len(Tournament.all_tournaments) > 0:
                self.tc.view_tournaments()
                try:
                    select_id = int(self.view.select_tournament()) - 1
                    if len(Tournament.all_tournaments) > select_id:
                        number = select_id
                        self.ts = Tournament.all_tournaments[number]
                        self.menu = self.view.display_edit_tournament_menu(
                            is_close=self.ts.is_finish(),
                            end_player=self.ts.count_players() >= NBR_PLAYER,
                            nb_round=len(self.ts.rounds))
                        self.page = 'edit_tournament'
                except ValueError:
                    self.go_menu_home()
        elif self.select.lower() == 'q':
            self.ts = None
            self.go_menu_home()

    def menu_edit_player(self):
        if self.select == '1':
            self.player_selected.firstname = self.pc.field_firstname(
                self.player_selected.firstname
            )
        elif self.select == '2':
            self.player_selected.lastname = self.pc.field_lastname(
                self.player_selected.lastname
            )
        elif self.select == '3':
            self.player_selected.birthday = self.pc.field_birthday(
                self.player_selected.birthday
            )
        elif self.select == '4':
            self.player_selected.rating = self.pc.field_rating(
                self.player_selected.rating
            )
        elif self.select.lower() == 'q':
            self.go_menu_player()
        if self.player_selected:
            self.view.display_list_players([self.player_selected])

    def menu_edit_tournament(self):
        if self.select == '1':
            if not self.ts.is_finish():
                self.tc.close_round(self.ts.get_last_round())
                if self.ts.nbr_rounds > len(self.ts.rounds):
                    self.tc.create_round(
                        self.ts,
                        f'round {len(self.ts.rounds)+1}',
                        first=False)
        elif self.select == '2':
            self.ts.name = self.tc.field_name(
                self.ts.name)
        elif self.select == '3':
            self.ts.description = self.tc.field_description(
                self.ts.description)
        elif self.select == '4':
            self.ts.ctr_time = self.tc.field_ctr_time(
                self.ts.ctr_time)
        elif self.select == '5':
            self.ts.place = self.tc.field_place(
                self.ts.place)
        elif self.select == '6':
            start_date = self.tc.field_start_date(self.ts.start_date)
            self.ts.set_start_date(start_date)
        elif self.select == '7':
            self.ts.nbr_days = self.tc.field_nbr_days(
                self.ts.nbr_days)
        elif (self.select == '8' and
                self.ts.count_players() < NBR_PLAYER):
            self.tc.add_player(self.ts, self.view, add=True)
        elif self.select == '9':
            self.tc.create_round(self.ts)
        elif self.select == '10':
            self.tc.change_player_rating(self.ts.get_players())
        elif self.select.lower() == 'q':
            self.ts = None
            self.go_menu_home()

    def menu_rapport_player(self):
        if self.select == '1':
            players = self.pc.get_all_players_by_rating()
            self.view.display_list_players(players)
        elif self.select == '2':
            players = self.pc.get_all_players_by_name()
            self.view.display_list_players(players)
        elif self.select.lower() == 'q':
            self.go_menu_rapport()

    def menu_rapport_tournament_player(self):
        players = self.ts.get_players()
        if self.select == '1':
            players = sorted(players, key=lambda x: x.rating)
            self.view.display_list_players(players)
            input("suite")
        elif self.select == '2':
            players = sorted(players, key=lambda x: x.lastname)
            self.view.display_list_players(players)
            input("suite")
        elif self.select.lower() == 'q':
            self.go_menu_rapport()

    def menu_rapport(self):
        if self.select == '1':
            self.menu = self.view.display_menu_order()
            self.page = 'rapport_player'

        elif self.select == '2':
            self.ts = self.tc.select_tournament()
            self.menu = self.view.display_menu_order()
            self.page = 'rapport_tournament_player'

        elif self.select == '3':
            tournaments = Tournament.all_tournaments
            self.view.display_list_tournament_online(tournaments)
            input("suite")
        elif self.select == '4':
            while True:
                tournament = self.tc.select_tournament()

                if tournament:
                    rounds = tournament.get_rounds()
                    self.view.display_round(tournament.name, rounds)
                    input('suite')
                    break
                else:
                    break
        elif self.select == '5':
            while True:
                tournament = self.tc.select_tournament()

                if tournament:
                    self.view.display_list_match(tournament.get_all_matches())
                    input("suite")
                    break
                else:
                    break
        elif self.select.lower() == 'q':
            self.go_menu_home()

    def run(self):
        while True:
            if self.page != 'quit':
                print(self.menu)
                self.select = input('entrer le numéro du menu: ')

            if self.page == 'home':
                self.menu_home()
            elif self.page == 'player':
                self.menu_player()
            elif self.page == 'edit_player':
                self.menu_edit_player()
            elif self.page == 'tournament':
                self.menu_tournament()
            elif self.page == 'edit_tournament':
                self.menu_edit_tournament()
            elif self.page == 'rapport':
                self.menu_rapport()
            elif self.page == 'rapport_player':
                self.menu_rapport_player()
            elif self.page == 'rapport_tournament_player':
                self.menu_rapport_tournament_player()
            elif self.page == 'quit':
                break

from controllers.player import PlayerController
from controllers.tournament import TournamentController, RoundController
from models.linktracking import LinkTracking
from models.tournament import Tournament
from models.player import Player
from config import DEFAULT_NBR_PLAYER


class Controller:
    def __init__(self, menu_view):
        self.view = menu_view
        self.lnk = LinkTracking()
        self.tc = TournamentController(self.view)
        self.pc = PlayerController(self.view)
        self.menu = self.view.display_menu()
        self.select = 0
        self.page = 'home'
        self.player_selected = None
        self.tournament_selected = None

    def menu_home(self):
        if self.select == '1':
            self.tc.add_tournament()
        elif self.select == '2':
            self.page = 'player'
            self.menu = self.view.display_menu_player()
        elif self.select == '3':
            self.page = 'tournament'
            self.menu = self.view.display_menu_tournament()
        elif self.select == '4':
            self.page = 'rapport'
            self.menu = self.view.display_menu_rapport()
        elif self.select == '8':
            self.pc.import_all_players()
            self.tc.import_all_tournament()
        elif self.select == '9':
            for tournament in Tournament.all_tournaments:
                self.tc.save(tournament)
            for player in Player.all_players:
                self.pc.save(player)
        elif self.select == 'q':
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
            number = int(self.view.select_player()) - 1
            self.player_selected = players[number]
            self.menu = self.view.display_edit_player()
        elif self.select == 'q':
            self.player_selected = None
            self.page = 'home'
            self.menu = self.view.display_menu()

    def menu_tournament(self):
        if self.select == '1':
            self.tc.add_tournament()
        elif self.select == '2':
            self.tc.view_tournaments()
            number = int(self.view.select_tournament()) - 1
            self.tournament_selected = Tournament.all_tournaments[number]
            self.menu = self.view.display_edit_tournament_menu(
                is_close=self.tournament_selected.is_finish(),
                end_player=self.tournament_selected.count_players() >= DEFAULT_NBR_PLAYER,
                nb_round=len(self.tournament_selected.rounds))
            self.page = 'edit_tournament'
        elif self.select == 'q':
            self.tournament_selected = None
            self.page = 'home'
            self.menu = self.view.display_menu()

    def menu_edit_player(self):
        if self.select == '1':
            self.player_selected.firstname = self.pc.field_firstname(
                self.player_selected.firstname
            )
        elif self.select == '2':
            self.player_selected.lastname = self.pc.field_lastname(
                self.player_selected.lastname
            )
        elif self.select == '4':
            self.player_selected.rating = self.pc.field_rating(
                self.player_selected.rating
            )
        elif self.select == 'q':
            self.page = 'player'
            self.menu = self.view.display_menu_player()
        self.view.display_list_players([self.player_selected])

    def menu_edit_tournament(self):
        if self.select == '1':
            if not self.tournament_selected.is_finish():
                self.close_round(self.tournament_selected.get_last_round())
                if self.tournament_selected.nbr_rounds > len(self.tournament_selected.rounds):
                    my_round = RoundController.create_round(
                        self.tournament_selected.get_players(),
                        f'round {len(self.tournament_selected.rounds)+1}',
                        first=False
                    )
                    self.tournament_selected.add_round(my_round)
        elif self.select == '2':
            self.tournament_selected.name = self.tc.field_name(
                self.tournament_selected.name)
        elif self.select == '3':
            self.tournament_selected.description = self.tc.field_description(
                self.tournament_selected.description)
        elif self.select == '4':
            self.tournament_selected.ctr_time = self.tc.field_ctr_time(
                self.tournament_selected.ctr_time)
        elif self.select == '5':
            self.tournament_selected.place = self.tc.field_place(
                self.tournament_selected.place)
        elif self.select == '6':
            self.tournament_selected.start_date = self.tc.field_start_date(
                self.tournament_selected.start_date)
        elif self.select == '7':
            self.tournament_selected.nbr_days = self.tc.field_nbr_days(
                self.tournament_selected.nbr_days)
        elif (self.select == '8' and
                self.tournament_selected.count_players() < DEFAULT_NBR_PLAYER):
            self.add_player(self.tournament_selected, self.view, add=True)
        elif self.select == '9':
            self.create_round(self.tournament_selected)
        elif self.select == '10':
            self.change_player_rating(self.tournament_selected.get_players())
        elif self.select == 'q':
            self.tournament_selected = None
            self.page = 'home'
            self.menu = self.view.display_menu()
        self.view.display_list_tournament_online([self.tournament_selected])

    def menu_rapport_player(self):
        if self.select == '1':
            players = self.pc.get_all_players_by_rating()
            self.view.display_list_players(players)
        elif self.select == '2':
            players = self.pc.get_all_players_by_name()
            self.view.display_list_players(players)
        elif self.select == 'q':
            self.page = 'rapport'
            self.menu = self.view.display_menu_rapport()

    def menu_rapport_tournament_player(self):
        players = self.tournament_selected.get_players()
        if self.select == '1':
            players = sorted(players, key=lambda x: x.rating)
            self.view.display_list_players(players)
            input("suite")
        elif self.select == '2':
            players = sorted(players, key=lambda x: x.lastname)
            self.view.display_list_players(players)
            input("suite")
        elif self.select == 'q':
            self.page = 'rapport'
            self.menu = self.view.display_menu_rapport()

    def menu_rapport(self):
        if self.select == '1':
            self.menu = self.view.display_menu_order()
            self.page = 'rapport_player'

        elif self.select == '2':
            self.tournament_selected = self.tc.select_tournament()
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
        elif self.select == 'q':
            self.page = 'home'
            self.menu = self.view.display_menu()

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

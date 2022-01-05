from models.linktracking import LinkTracking
from models.match import Match
from models.round import Round
from models.player import Player
from controllers.validation import Validation
from controllers.player import PlayerController
from services.services import PlayerManagement, RoundManagement, MatchManagement, TournamentManagement
from models.tournament import Tournament


class TournamentController:
    linktracking = LinkTracking()

    @classmethod
    def save(self, tournament):
        print(type(tournament))
        for player in tournament.players:
            print(f'player name= {player.firstname}')
            PlayerManagement.save(player.serialize())

        for round_t in tournament.rounds:
            RoundManagement.save(round_t.serialize())
            for match in round_t.matchs:
                MatchManagement.save(match.serialize())

        TournamentManagement.save(tournament.serialize())

    @classmethod
    def add_tournament(self, menu_view):
        new_tournament = Tournament()

        menu_view.display_tournament_new()

        self.linktracking.init()
        while self.linktracking.next is False:
            new_tournament.name = menu_view.display_tournament_name(self.linktracking)
            Validation.tournament_name(new_tournament.name, self.linktracking)

        self.linktracking.init()
        while self.linktracking.next is False:
            new_tournament.place = menu_view.display_tournament_place(self.linktracking)
            Validation.tournament_place(new_tournament.place, self.linktracking)

        self.linktracking.init()
        while self.linktracking.next is False:
            new_date = menu_view.display_tournament_date_start(self.linktracking)
            new_tournament.start_date = Validation.tournament_date_start(new_date, self.linktracking)

        self.linktracking.init()
        while self.linktracking.next is False:
            nbr_days = menu_view.display_tournament_duration(self.linktracking)
            new_tournament.nbr_days = Validation.tournament_duration(nbr_days, self.linktracking)

        self.linktracking.init()
        while self.linktracking.next is False:
            nbr_rounds = menu_view.display_tournament_rounds(self.linktracking)
            new_tournament.nbr_rounds = Validation.tournament_rounds(nbr_rounds, self.linktracking)

        self.linktracking.init()
        while self.linktracking.next is False:
            ctr_time = menu_view.display_tournament_ctr_time(self.linktracking)
            new_tournament.ctr_time = Validation.tournament_ctr_time(ctr_time, self.linktracking)

        self.linktracking.init()
        while self.linktracking.next is False:
            new_tournament.description = menu_view.display_tournament_description(self.linktracking)
            Validation.tournament_description(new_tournament.description, self.linktracking)

        self.linktracking.init()
        while self.linktracking.next is False:
            while new_tournament.nbr_players() < 2:
                new_player = PlayerController.add_player(menu_view, new_tournament.nbr_players()+1)
                PlayerManagement.save(new_player.serialize())
                new_tournament.add_player(new_player)

            self.linktracking.next = True

        my_round = RoundController.create_round(new_tournament.export_players(), 'round 1')
        new_tournament.add_round(my_round)
        return new_tournament


class RoundController:

    @classmethod
    def create_round(self, players_list, name):
        round_one = Round(name)
        players_list = sorted(players_list, key=lambda x: x['rating'])
        half = len(players_list)//2
        list_one = players_list[:half]
        list_two = players_list[half:]
        while len(list_one) > 1 or len(list_two):
            player_one = list_one.pop(0)
            player_two = list_two.pop(0)
            match = Match()
            match.add_player(Player(player_one))
            match.add_player(Player(player_two))
            round_one.add_match(match)

        return round_one
